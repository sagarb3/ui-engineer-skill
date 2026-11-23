import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import evaluate


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="skill-evaluation-test-")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name) / "run"

    def prepare(self, case="harness.focused-edit", **options):
        evaluate.prepare(case, self.directory, **options)
        return self.directory / "workspace"

    def review(self, status):
        (self.directory / "transcript.txt").write_text("Observed command and result.\n")
        review = evaluate.read_json(self.directory / "review.json")
        for criterion in review["criteria"]:
            criterion["status"] = status
            criterion["evidence"] = [{"path": "transcript.txt", "note": "Observed result."}]
        evaluate.write_json(self.directory / "review.json", review)

    def test_collection_has_complete_reference_and_case_coverage(self):
        result = evaluate.validate()
        self.assertEqual(result["skills"], 10)
        self.assertEqual(result["guides"], 39)
        self.assertEqual(result["cases"], 50)
        self.assertEqual(result["behavioral_evaluations_run"], 0)

    def test_preparation_installs_complete_skill_without_hidden_grading_notes(self):
        workspace = self.prepare()
        source = evaluate.ROOT / "skills/harness"
        installed = workspace / ".github/skills/harness"
        self.assertEqual(evaluate.tree_hash(source), evaluate.tree_hash(installed))
        self.assertFalse((workspace / "review.json").exists())
        self.assertFalse((workspace / "manifest.json").exists())
        self.assertEqual(evaluate.git(workspace, "status", "--porcelain").stdout, "")
        self.assertIn("Apply the installed skill named harness", (self.directory / "prompt.md").read_text())

    def test_baseline_has_no_treatment_installation(self):
        workspace = self.prepare(mode="baseline")
        self.assertFalse((workspace / ".github").exists())
        self.assertNotIn("Apply the installed skill", (self.directory / "prompt.md").read_text())

    def test_existing_destination_is_preserved(self):
        self.directory.mkdir()
        marker = self.directory / "user-draft.txt"
        marker.write_text("Keep this draft.\n")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.prepare()
        self.assertEqual(marker.read_text(), "Keep this draft.\n")

    def test_rejects_path_and_symlink_escape(self):
        with self.assertRaises(ValueError):
            evaluate.local_path(Path(self.temporary.name), "../outside")
        outside = Path(self.temporary.name).parent
        (Path(self.temporary.name) / "link").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            evaluate.local_path(Path(self.temporary.name), "link/outside")

    def test_unrun_case_is_incomplete(self):
        self.prepare()
        result = evaluate.score(self.directory)
        self.assertEqual(result["outcome"], "incomplete")
        self.assertEqual(result["reviewed_criteria"], 0)

    def test_pass_requires_existing_evidence(self):
        self.prepare()
        self.review("passed")
        self.assertEqual(evaluate.score(self.directory)["outcome"], "passed")
        (self.directory / "transcript.txt").unlink()
        with self.assertRaisesRegex(ValueError, "absent or empty"):
            evaluate.score(self.directory)

    def test_failed_criterion_cannot_be_hidden_by_other_passes(self):
        self.prepare()
        self.review("passed")
        review = evaluate.read_json(self.directory / "review.json")
        review["criteria"][0]["status"] = "failed"
        evaluate.write_json(self.directory / "review.json", review)
        self.assertEqual(evaluate.score(self.directory)["outcome"], "failed")

    def test_rubric_is_not_execution_evidence(self):
        self.prepare()
        self.review("passed")
        review = evaluate.read_json(self.directory / "review.json")
        review["criteria"][0]["evidence"][0]["path"] = "review.json"
        evaluate.write_json(self.directory / "review.json", review)
        with self.assertRaisesRegex(ValueError, "not execution evidence"):
            evaluate.score(self.directory)

    def test_missing_or_modified_criteria_are_rejected(self):
        self.prepare()
        review = evaluate.read_json(self.directory / "review.json")
        review["criteria"][0]["description"] = "An unrelated easier standard."
        evaluate.write_json(self.directory / "review.json", review)
        with self.assertRaisesRegex(ValueError, "Criterion changed"):
            evaluate.score(self.directory)
        review["criteria"].pop()
        evaluate.write_json(self.directory / "review.json", review)
        with self.assertRaisesRegex(ValueError, "missing, duplicated, or unknown"):
            evaluate.score(self.directory)

    def test_git_case_sets_up_only_local_changes(self):
        workspace = self.prepare("git-tooling.stage-one-file")
        self.assertEqual(evaluate.git(workspace, "remote").stdout, "")
        self.assertIn(" M app.js", evaluate.git(workspace, "status", "--porcelain").stdout)
        self.assertEqual(evaluate.git(workspace, "diff", "--cached", "--name-only").stdout, "")

    def test_fixture_git_ignores_inherited_git_directory(self):
        with patch.dict(os.environ, {"GIT_DIR": "/nonexistent/foreign-repository"}):
            workspace = self.prepare()
        self.assertTrue((workspace / ".git").is_dir())

    def test_discovery_case_does_not_supply_the_expected_activation(self):
        self.prepare("trim-mode.literal-trigger")
        self.assertNotIn("Apply the installed skill", (self.directory / "prompt.md").read_text())

    def test_follow_up_turns_are_preserved(self):
        self.prepare("trim-mode.mode-stop")
        turns = evaluate.read_json(self.directory / "follow-up-turns.json")
        self.assertEqual(len(turns), 2)
        self.assertIn("Turn off trim mode", turns[-1])


if __name__ == "__main__":
    unittest.main()
