#!/usr/bin/env python3
"""Validate collection data, prepare isolated cases, and summarize evidence reviews."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
CLIENT_DIRS = {
    "copilot": ".github/skills",
    "cursor": ".cursor/skills",
    "codex": ".agents/skills",
    "claude": ".claude/skills",
    "opencode": ".opencode/skills",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_path(base, relative):
    require(isinstance(relative, str) and bool(relative), "Expected a relative path")
    path = Path(relative)
    require(not path.is_absolute() and ".." not in path.parts, "Path escapes its boundary")
    target = (base / path).resolve()
    require(target.is_relative_to(base.resolve()), "Path escapes through a symlink")
    return target


def load_cases(root=ROOT):
    cases = {}
    for path in sorted((root / "evals/cases").glob("*.json")):
        suite = read_json(path)
        require(suite.get("schema_version") == 1, "Unsupported evaluation schema")
        skill = suite.get("skill")
        require(skill == path.stem, "Suite name does not match its file")
        require((root / "skills" / skill / "SKILL.md").is_file(), "Unknown skill")
        require(isinstance(suite.get("cases"), list) and suite["cases"], "Empty suite")
        for case in suite["cases"]:
            identifier = case.get("id", "")
            require(identifier.startswith(skill + ".") and identifier not in cases,
                    "Invalid or duplicate case identifier")
            require(case.get("activation") in ("explicit", "discovery"), "Unknown activation")
            require(isinstance(case.get("category"), str) and case["category"], "Missing category")
            require(isinstance(case.get("prompt"), str) and case["prompt"], "Missing prompt")
            fixture = local_path(root, case.get("fixture"))
            require(fixture.is_relative_to((root / "evals/fixtures").resolve()) and fixture.is_dir(),
                    "Fixture must be inside evals/fixtures")
            require(not any(p.is_symlink() or ".git" in p.relative_to(fixture).parts
                            for p in fixture.rglob("*")), "Unsafe fixture contents")
            criteria = case.get("criteria")
            require(isinstance(criteria, list) and criteria, "Missing review criteria")
            identifiers = [item.get("id") for item in criteria]
            require(all(isinstance(item, str) and item for item in identifiers)
                    and len(set(identifiers)) == len(identifiers), "Invalid review identifiers")
            require(all(isinstance(item.get("description"), str) and item["description"]
                        for item in criteria), "Missing criterion description")
            for turn in case.get("turns", []):
                require(isinstance(turn, str) and turn, "Invalid follow-up turn")
            for relative, content in case.get("working_tree", {}).items():
                target = local_path(fixture, relative)
                require(".git" not in Path(relative).parts and isinstance(content, str),
                        "Unsafe working-tree change")
                require(not any(part in (".github", ".agents", ".cursor", ".claude", ".opencode")
                                for part in target.relative_to(fixture).parts),
                        "Case setup may not replace client instructions")
            require(all(isinstance(branch, str) and re.fullmatch(r"[a-z0-9][a-z0-9-]*", branch)
                        for branch in case.get("setup_branches", [])), "Unsafe branch name")
            cases[identifier] = dict(case, skill=skill)
    return cases


def validate(root=ROOT):
    guides = 0
    skills = sorted(path for path in (root / "skills").iterdir() if path.is_dir())
    require(bool(skills), "No skills found")
    for skill in skills:
        content = (skill / "SKILL.md").read_text(encoding="utf-8")
        require(content.startswith("---\n") and "\n---\n" in content, "Missing frontmatter")
        require(re.search(r"^name: " + re.escape(skill.name) + r"$", content, re.M),
                "Skill name does not match its folder")
        require(re.search(r"^description: .+", content, re.M), "Missing description")
        require("Generated code must contain no AI attribution." in content, "Missing isolation rule")
        index = read_json(skill / "references.json")
        require(index.get("schema_version") == 1 and index.get("skill") == skill.name,
                "Reference index does not match its skill")
        references = index.get("references")
        require(isinstance(references, list) and references, "Empty reference index")
        referenced = set()
        ids = set()
        for item in references:
            require(isinstance(item.get("id"), str) and item["id"] not in ids,
                    "Duplicate or missing reference identifier")
            ids.add(item["id"])
            target = local_path(skill, item.get("path"))
            require(target.is_file() and target.suffix == ".md", "Missing local guide")
            require(target not in referenced, "Duplicate guide path")
            referenced.add(target)
            require(item.get("title") and item.get("when_to_read"), "Incomplete guide metadata")
            require(item["path"] in content, "Guide is not routed from SKILL.md")
        require(referenced == {path.resolve() for path in (skill / "guides").glob("*.md")},
                "Guide directory and index disagree")
        guides += len(referenced)
    cases = load_cases(root)
    require({case["skill"] for case in cases.values()} == {path.name for path in skills},
            "Every skill needs an evaluation suite")
    return {"skills": len(skills), "guides": guides, "cases": len(cases),
            "behavioral_evaluations_run": 0}


def git(workspace, *arguments):
    environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                       GIT_CONFIG_SYSTEM=os.devnull)
    command = ["git", "-c", "core.hooksPath=" + os.devnull, "-c", "commit.gpgSign=false",
               "-c", "user.name=Fixture Maintainer", "-c", "user.email=fixture@example.invalid"]
    return subprocess.run(command + list(arguments), cwd=workspace, env=environment,
                          check=True, capture_output=True, text=True)


def case_hash(case):
    return hashlib.sha256(json.dumps(case, sort_keys=True).encode()).hexdigest()


def tree_hash(directory):
    digest = hashlib.sha256()
    for path in sorted(path for path in directory.rglob("*") if path.is_file()):
        digest.update(path.relative_to(directory).as_posix().encode() + b"\0")
        digest.update(path.read_bytes() + b"\0")
    return digest.hexdigest()


def prepare(identifier, destination, mode="with-skill", client="copilot", root=ROOT):
    validate(root)
    cases = load_cases(root)
    require(identifier in cases, "Unknown evaluation case")
    require(mode in ("with-skill", "baseline") and client in CLIENT_DIRS, "Unknown mode or client")
    require(not destination.exists() and not destination.is_symlink(), "Destination already exists")
    require(not destination.resolve().is_relative_to(root.resolve()),
            "Evaluation runs must be outside the collection checkout")
    destination.mkdir(parents=True)
    workspace = destination / "workspace"
    case = cases[identifier]
    shutil.copytree(local_path(root, case["fixture"]), workspace)
    if mode == "with-skill":
        shutil.copytree(root / "skills" / case["skill"],
                        workspace / CLIENT_DIRS[client] / case["skill"])
    git(workspace, "init", "-q", "-b", "main", "--template=")
    git(workspace, "add", "--all")
    git(workspace, "commit", "-qm", "Set up sample workspace")
    for branch in case.get("setup_branches", []):
        git(workspace, "branch", branch)
    for relative, content in case.get("working_tree", {}).items():
        path = local_path(workspace, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    prompt = case["prompt"]
    if mode == "with-skill" and case["activation"] == "explicit":
        prompt = "Apply the installed skill named " + case["skill"] + ".\n\n" + prompt
    (destination / "prompt.md").write_text(prompt + "\n", encoding="utf-8")
    if case.get("turns"):
        write_json(destination / "follow-up-turns.json", case["turns"])
    write_json(destination / "manifest.json", {"case_id": identifier, "mode": mode,
               "client": client, "case_sha256": case_hash(case),
               "skill_sha256": tree_hash(root / "skills" / case["skill"]),
               "fixture_sha256": tree_hash(local_path(root, case["fixture"]))})
    write_json(destination / "review.json", {"case_id": identifier, "criteria": [
        dict(item, status="unverified", evidence=[]) for item in case["criteria"]]})
    return {"workspace": str(workspace), "prompt": str(destination / "prompt.md"),
            "status": "prepared", "behavioral_evaluations_run": 0}


def score(directory, root=ROOT):
    manifest = read_json(directory / "manifest.json")
    cases = load_cases(root)
    require(manifest.get("case_id") in cases, "Unknown prepared case")
    case = cases[manifest["case_id"]]
    require(manifest.get("case_sha256") == case_hash(case), "Case changed after preparation")
    review = read_json(directory / "review.json")
    require(review.get("case_id") == case["id"], "Review belongs to another case")
    rows = review.get("criteria", [])
    expected = {item["id"] for item in case["criteria"]}
    require(len(rows) == len(expected) and {item.get("id") for item in rows} == expected,
            "Review criteria are missing, duplicated, or unknown")
    for row in rows:
        require(row.get("description") == next(item["description"] for item in case["criteria"]
                                                if item["id"] == row["id"]), "Criterion changed")
        require(row.get("status") in ("passed", "failed", "unverified"), "Unknown verdict")
        evidence = row.get("evidence")
        require(isinstance(evidence, list), "Evidence must be a list")
        if row["status"] != "unverified":
            require(bool(evidence), "A reviewed verdict needs evidence")
        for item in evidence:
            require(isinstance(item, dict) and item.get("note"), "Evidence needs a note")
            path = local_path(directory, item.get("path"))
            require(path.is_file() and path.stat().st_size > 0, "Evidence file is absent or empty")
            require(path.name not in ("review.json", "manifest.json", "prompt.md"),
                    "Rubrics and prompts are not execution evidence")
    statuses = [row["status"] for row in rows]
    outcome = "failed" if "failed" in statuses else "incomplete" if "unverified" in statuses else "passed"
    return {"case_id": case["id"], "mode": manifest["mode"], "outcome": outcome,
            "reviewed_criteria": len(statuses) - statuses.count("unverified"),
            "total_criteria": len(statuses), "grading": "evidence-backed reviewer judgments"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    commands.add_parser("list")
    preparation = commands.add_parser("prepare")
    preparation.add_argument("case")
    preparation.add_argument("destination", type=Path)
    preparation.add_argument("--mode", choices=("with-skill", "baseline"), default="with-skill")
    preparation.add_argument("--client", choices=CLIENT_DIRS, default="copilot")
    grading = commands.add_parser("score")
    grading.add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate()
        elif args.command == "list":
            result = sorted(load_cases())
        elif args.command == "prepare":
            result = prepare(args.case, args.destination, args.mode, args.client)
        else:
            result = score(args.directory)
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
