#!/usr/bin/env python3
"""Audit a local repository package for common GitHub health and security gaps."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from validate_actions_workflow import WorkflowLoader, validate as validate_workflow

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with: python -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".json", ".toml", ".ini", ".cfg", ".conf",
    ".py", ".js", ".ts", ".tsx", ".jsx", ".rs", ".go", ".java", ".rb", ".php",
    ".sh", ".bash", ".zsh", ".ps1", ".xml", ".html", ".css", ".scss", ".env",
}
SECRET_PATTERNS = [
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("github-fine-grained-token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]
SKIP_DIRS = {".git", "node_modules", "vendor", "target", "dist", "build", ".venv", "venv", "__pycache__"}


def add(bucket: list[dict[str, str]], code: str, path: str, message: str) -> None:
    bucket.append({"code": code, "path": path, "message": message})


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"Dockerfile", "Makefile", ".gitignore", ".gitattributes"}


def audit(root: Path) -> dict[str, list[dict[str, str]]]:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    info: list[dict[str, str]] = []

    if not root.is_dir():
        add(errors, "ROOT_NOT_DIRECTORY", str(root), "Repository path is not a directory.")
        return {"errors": errors, "warnings": warnings, "info": info}

    recommended = {
        "README.md": "Add a README that explains purpose, setup, and usage.",
        "LICENSE": "Select and add a license when redistribution terms should be explicit.",
        "CONTRIBUTING.md": "Document development and contribution workflow.",
        "SECURITY.md": "Provide a private vulnerability reporting route.",
    }
    for filename, message in recommended.items():
        if not (root / filename).exists():
            add(warnings, "MISSING_HEALTH_FILE", filename, message)

    if not (root / ".github" / "PULL_REQUEST_TEMPLATE.md").exists() and not (root / "PULL_REQUEST_TEMPLATE.md").exists():
        add(warnings, "MISSING_PR_TEMPLATE", ".github/PULL_REQUEST_TEMPLATE.md", "Consider a concise pull request template for collaborative repositories.")

    issue_template_dir = root / ".github" / "ISSUE_TEMPLATE"
    if not issue_template_dir.exists():
        add(warnings, "MISSING_ISSUE_INTAKE", ".github/ISSUE_TEMPLATE", "No structured issue intake was found.")

    codeowners_candidates = [root / ".github" / "CODEOWNERS", root / "CODEOWNERS", root / "docs" / "CODEOWNERS"]
    if not any(path.exists() for path in codeowners_candidates):
        add(info, "NO_CODEOWNERS", "CODEOWNERS", "No CODEOWNERS file found; this may be acceptable for a single-maintainer repository.")

    workflow_dir = root / ".github" / "workflows"
    if workflow_dir.exists():
        for workflow_path in sorted(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml"))):
            rel = workflow_path.relative_to(root).as_posix()
            try:
                data = yaml.load(workflow_path.read_text(encoding="utf-8"), Loader=WorkflowLoader)
                report = validate_workflow(data)
            except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
                add(errors, "INVALID_WORKFLOW", rel, str(exc))
                continue
            for item in report["errors"]:
                add(errors, "WORKFLOW_ERROR", f"{rel}:{item['path']}", item["message"])
            for item in report["warnings"]:
                add(warnings, "WORKFLOW_WARNING", f"{rel}:{item['path']}", item["message"])
    else:
        add(info, "NO_WORKFLOWS", ".github/workflows", "No GitHub Actions workflows found.")

    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        rel = path.relative_to(root).as_posix()
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size > 100 * 1024 * 1024:
            add(errors, "OVERSIZED_FILE", rel, f"File is {size} bytes; normal GitHub file limits or repository usability may be affected.")
        elif size > 50 * 1024 * 1024:
            add(warnings, "LARGE_FILE", rel, f"File is {size} bytes; consider releases, object storage, or Git LFS.")

        if size > 2 * 1024 * 1024 or not is_text_file(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for secret_type, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                add(errors, "POSSIBLE_SECRET", rel, f"Possible {secret_type} detected. Rotate before removing from history.")

    readme = root / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8", errors="replace")
        if "REPLACE_ME" in text or "<OWNER>" in text or "<REPOSITORY>" in text:
            add(warnings, "UNRESOLVED_PLACEHOLDER", "README.md", "README contains unresolved template placeholders.")

    return {"errors": errors, "warnings": warnings, "info": info}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    args = parser.parse_args()

    report = audit(args.repository.resolve())
    if args.json_output:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for severity in ("errors", "warnings", "info"):
            for item in report[severity]:
                print(f"{severity[:-1].upper()}: {item['code']}: {item['path']}: {item['message']}")
        print(
            "Summary: "
            f"{len(report['errors'])} error(s), "
            f"{len(report['warnings'])} warning(s), "
            f"{len(report['info'])} informational item(s)"
        )

    if report["errors"] or (args.strict and report["warnings"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
