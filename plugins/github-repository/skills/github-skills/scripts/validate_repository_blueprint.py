#!/usr/bin/env python3
"""Validate a github-skills repository blueprint JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = {
    "schema_version",
    "repository",
    "architecture",
    "files",
    "governance",
    "issues_and_projects",
    "pull_requests",
    "rulesets",
    "actions",
    "security",
    "releases",
    "implementation",
    "validation",
}

VISIBILITIES = {"public", "private", "internal", "unspecified"}
REPOSITORY_TYPES = {
    "application",
    "library",
    "sdk",
    "cli",
    "infrastructure",
    "documentation",
    "configuration",
    "dataset",
    "template",
    "skill",
    "monorepo",
    "mixed",
    "other",
}
IMPLEMENTATION_TYPES = {
    "file_change",
    "repository_setting",
    "organization_setting",
    "secret_or_variable",
    "manual_verification",
    "external_system",
}


def add_issue(bucket: list[dict[str, str]], path: str, message: str) -> None:
    bucket.append({"path": path, "message": message})


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def safe_repo_path(value: str) -> bool:
    path = Path(value)
    return not path.is_absolute() and ".." not in path.parts and value.strip() not in {"", "."}


def validate(data: Any) -> dict[str, list[dict[str, str]]]:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    if not isinstance(data, dict):
        add_issue(errors, "$", "Top-level JSON value must be an object.")
        return {"errors": errors, "warnings": warnings}

    missing = sorted(REQUIRED_TOP_LEVEL - set(data))
    for key in missing:
        add_issue(errors, f"$.{key}", "Required top-level key is missing.")

    unknown = sorted(set(data) - REQUIRED_TOP_LEVEL - {"metadata", "notes"})
    for key in unknown:
        add_issue(warnings, f"$.{key}", "Unknown top-level key; confirm consumers support it.")

    if data.get("schema_version") != "1.0":
        add_issue(errors, "$.schema_version", "Expected schema_version to be '1.0'.")

    repository = data.get("repository")
    if not isinstance(repository, dict):
        add_issue(errors, "$.repository", "Must be an object.")
    else:
        for key in ("name", "visibility", "default_branch", "repository_type"):
            if key not in repository:
                add_issue(errors, f"$.repository.{key}", "Required key is missing.")
        if not is_nonempty_string(repository.get("name")):
            add_issue(errors, "$.repository.name", "Must be a non-empty string.")
        if repository.get("visibility") not in VISIBILITIES:
            add_issue(errors, "$.repository.visibility", f"Must be one of {sorted(VISIBILITIES)}.")
        if not is_nonempty_string(repository.get("default_branch")):
            add_issue(errors, "$.repository.default_branch", "Must be a non-empty string.")
        if repository.get("repository_type") not in REPOSITORY_TYPES:
            add_issue(errors, "$.repository.repository_type", f"Must be one of {sorted(REPOSITORY_TYPES)}.")

    architecture = data.get("architecture")
    if not isinstance(architecture, dict):
        add_issue(errors, "$.architecture", "Must be an object.")
    else:
        if not is_nonempty_string(architecture.get("layout")):
            add_issue(errors, "$.architecture.layout", "Must describe the repository layout.")
        for key in ("primary_languages", "package_managers"):
            if key in architecture and not isinstance(architecture[key], list):
                add_issue(errors, f"$.architecture.{key}", "Must be an array.")

    files = data.get("files")
    if not isinstance(files, list):
        add_issue(errors, "$.files", "Must be an array.")
    else:
        seen_paths: set[str] = set()
        for index, item in enumerate(files):
            path = f"$.files[{index}]"
            if not isinstance(item, dict):
                add_issue(errors, path, "File entry must be an object.")
                continue
            file_path = item.get("path")
            if not is_nonempty_string(file_path):
                add_issue(errors, f"{path}.path", "Must be a non-empty repository-relative path.")
            elif not safe_repo_path(file_path):
                add_issue(errors, f"{path}.path", "Must be a safe repository-relative path without '..'.")
            elif file_path in seen_paths:
                add_issue(errors, f"{path}.path", "Duplicate file path.")
            else:
                seen_paths.add(file_path)
            if item.get("action") not in {"create", "update", "move", "delete", "keep"}:
                add_issue(errors, f"{path}.action", "Must be create, update, move, delete, or keep.")
            if not is_nonempty_string(item.get("purpose")):
                add_issue(warnings, f"{path}.purpose", "Add a purpose for agent handoff.")

    for key in ("governance", "issues_and_projects", "pull_requests", "actions", "security", "releases"):
        if key in data and not isinstance(data[key], dict):
            add_issue(errors, f"$.{key}", "Must be an object.")

    rulesets = data.get("rulesets")
    if not isinstance(rulesets, list):
        add_issue(errors, "$.rulesets", "Must be an array.")
    else:
        names: set[str] = set()
        for index, ruleset in enumerate(rulesets):
            path = f"$.rulesets[{index}]"
            if not isinstance(ruleset, dict):
                add_issue(errors, path, "Ruleset entry must be an object.")
                continue
            name = ruleset.get("name")
            if not is_nonempty_string(name):
                add_issue(errors, f"{path}.name", "Must be a non-empty string.")
            elif name in names:
                add_issue(errors, f"{path}.name", "Duplicate ruleset name.")
            else:
                names.add(name)
            if ruleset.get("enforcement") not in {"active", "evaluate", "disabled", "unspecified"}:
                add_issue(errors, f"{path}.enforcement", "Invalid enforcement value.")
            if not isinstance(ruleset.get("targets", []), list):
                add_issue(errors, f"{path}.targets", "Must be an array.")
            if not isinstance(ruleset.get("rules", {}), dict):
                add_issue(errors, f"{path}.rules", "Must be an object.")

    implementation = data.get("implementation")
    if not isinstance(implementation, list):
        add_issue(errors, "$.implementation", "Must be an array.")
    else:
        ids: set[str] = set()
        for index, item in enumerate(implementation):
            path = f"$.implementation[{index}]"
            if not isinstance(item, dict):
                add_issue(errors, path, "Implementation item must be an object.")
                continue
            item_id = item.get("id")
            if not is_nonempty_string(item_id):
                add_issue(errors, f"{path}.id", "Must be a non-empty stable identifier.")
            elif item_id in ids:
                add_issue(errors, f"{path}.id", "Duplicate implementation id.")
            else:
                ids.add(item_id)
            if item.get("type") not in IMPLEMENTATION_TYPES:
                add_issue(errors, f"{path}.type", f"Must be one of {sorted(IMPLEMENTATION_TYPES)}.")
            if not is_nonempty_string(item.get("description")):
                add_issue(errors, f"{path}.description", "Must describe the change.")
            if item.get("status") not in {"planned", "ready", "blocked", "applied", "verified", "skipped"}:
                add_issue(errors, f"{path}.status", "Invalid status.")
            deps = item.get("depends_on", [])
            if not isinstance(deps, list) or not all(isinstance(x, str) for x in deps):
                add_issue(errors, f"{path}.depends_on", "Must be an array of implementation ids.")

        for index, item in enumerate(implementation):
            if isinstance(item, dict) and isinstance(item.get("depends_on"), list):
                for dep in item["depends_on"]:
                    if dep not in ids:
                        add_issue(errors, f"$.implementation[{index}].depends_on", f"Unknown dependency id: {dep}")

    validation = data.get("validation")
    if not isinstance(validation, list):
        add_issue(errors, "$.validation", "Must be an array.")
    else:
        for index, item in enumerate(validation):
            path = f"$.validation[{index}]"
            if not isinstance(item, dict):
                add_issue(errors, path, "Validation item must be an object.")
                continue
            if not is_nonempty_string(item.get("name")):
                add_issue(errors, f"{path}.name", "Must be a non-empty string.")
            if item.get("type") not in {"command", "manual", "github_check", "api_readback", "negative_test"}:
                add_issue(errors, f"{path}.type", "Invalid validation type.")
            if not is_nonempty_string(item.get("expected")):
                add_issue(errors, f"{path}.expected", "Must describe the expected result.")

    security = data.get("security")
    if isinstance(security, dict):
        if security.get("secrets_in_repository") is True:
            add_issue(errors, "$.security.secrets_in_repository", "Repository blueprints must never permit committed secrets.")
        if security.get("actions_default_permissions") in {"write-all", "read-write"}:
            add_issue(warnings, "$.security.actions_default_permissions", "Prefer explicit least-privilege workflow or job permissions.")

    pull_requests = data.get("pull_requests")
    if isinstance(pull_requests, dict):
        if pull_requests.get("required") is True and not rulesets:
            add_issue(warnings, "$.rulesets", "Pull requests are required but no ruleset is defined.")

    return {"errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    args = parser.parse_args()

    try:
        data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.blueprint}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    report = validate(data)
    if args.json_output:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for severity in ("errors", "warnings"):
            for item in report[severity]:
                print(f"{severity[:-1].upper()}: {item['path']}: {item['message']}")
        print(f"Summary: {len(report['errors'])} error(s), {len(report['warnings'])} warning(s)")

    if report["errors"] or (args.strict and report["warnings"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
