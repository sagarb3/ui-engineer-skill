import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts import check_plugins


class PluginTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="plugin-package-test-")
        self.addCleanup(self.temporary.cleanup)
        self.copy = Path(self.temporary.name) / "collection"

    def copy_collection(self):
        shutil.copytree(check_plugins.ROOT, self.copy,
                        ignore=shutil.ignore_patterns(".git", ".DS_Store", "__pycache__", "*.pyc"))
        return self.copy

    def edit_json(self, path, change):
        value = json.loads(path.read_text())
        change(value)
        path.write_text(json.dumps(value))

    def test_complete_catalog_and_reviewed_imports(self):
        result = check_plugins.validate()
        self.assertEqual(result["plugins"], 3)
        self.assertEqual(result["skills"], 13)
        self.assertEqual(result["agents"], 1)
        self.assertEqual(result["addon_review_cases"], 10)
        self.assertEqual(result["locked_imports"], 40)
        self.assertEqual(result["live_model_evaluations_run"], 0)

    def test_catalog_cannot_escape_checkout(self):
        root = self.copy_collection()
        self.edit_json(root / ".github/plugin/marketplace.json",
                       lambda value: value["plugins"][0].update(source="../foreign"))
        with self.assertRaisesRegex(ValueError, "escapes"):
            check_plugins.validate(root)

    def test_manifest_and_catalog_versions_must_agree(self):
        root = self.copy_collection()
        self.edit_json(root / "plugin.json", lambda value: value.update(version="0.3.0"))
        with self.assertRaisesRegex(ValueError, "identity/version"):
            check_plugins.validate(root)

    def test_agent_plugins_manifest_rejects_legacy_component_fields(self):
        root = self.copy_collection()
        self.edit_json(root / "plugin.json", lambda value: value.update(skills="elsewhere"))
        with self.assertRaisesRegex(ValueError, "Unknown Agent Plugins"):
            check_plugins.validate(root)

    def test_import_changes_need_a_reviewed_lock_update(self):
        root = self.copy_collection()
        path = root / "plugins/github-repository/skills/github-skills/references/source-notes.md"
        path.write_text(path.read_text() + "\nUnreviewed change.\n")
        with self.assertRaisesRegex(ValueError, "source-lock review"):
            check_plugins.validate(root)

    def test_missing_preserved_license_fails_validation(self):
        root = self.copy_collection()
        path = root / "plugins/agentic-workflows/LICENSE"
        path.unlink()
        with self.assertRaisesRegex(ValueError, "Imported file is missing"):
            check_plugins.validate(root)

    def test_dispatcher_remains_explicitly_selected(self):
        root = self.copy_collection()
        path = root / "plugins/agentic-workflows/com.github.copilot/agents/agentic-workflows.agent.md"
        path.write_text(path.read_text().replace("infer: false", "infer: true"))
        with self.assertRaisesRegex(ValueError, "explicit selection"):
            check_plugins.validate(root)

    def test_addon_criteria_cannot_be_empty(self):
        root = self.copy_collection()
        self.edit_json(root / "plugins/agentic-workflows/evals/cases.json",
                       lambda value: value.update(cases=[]))
        with self.assertRaisesRegex(ValueError, "no evaluation cases"):
            check_plugins.validate(root)


if __name__ == "__main__":
    unittest.main()
