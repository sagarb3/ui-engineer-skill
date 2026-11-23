#!/usr/bin/env python3
"""Validate GitHub Actions workflow structure and common security hazards."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with: python -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


class WorkflowLoader(yaml.SafeLoader):
    """YAML loader that keeps keys such as `on` as strings."""


for first_char, resolvers in list(WorkflowLoader.yaml_implicit_resolvers.items()):
    WorkflowLoader.yaml_implicit_resolvers[first_char] = [
        item for item in resolvers if item[0] != "tag:yaml.org,2002:bool"
    ]

SHA_PATTERN = re.compile(r"^[0-9a-fA-F]{40}$")
SECRET_LITERAL_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
UNTRUSTED_EXPRESSIONS = (
    "github.event.issue.title",
    "github.event.issue.body",
    "github.event.pull_request.title",
    "github.event.pull_request.body",
    "github.event.comment.body",
    "github.event.review.body",
    "github.head_ref",
    "github.ref_name",
    "github.event.head_commit.message",
)


def issue(bucket: list[dict[str, str]], path: str, message: str) -> None:
    bucket.append({"path": path, "message": message})


def as_event_set(value: Any) -> set[str]:
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return {str(item) for item in value}
    if isinstance(value, dict):
        return {str(key) for key in value}
    return set()


def walk_strings(value: Any, path: str = "$"):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from walk_strings(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk_strings(item, f"{path}[{index}]")


def validate(data: Any) -> dict[str, list[dict[str, str]]]:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    if not isinstance(data, dict):
        issue(errors, "$", "Workflow must be a YAML mapping.")
        return {"errors": errors, "warnings": warnings}

    if "on" not in data:
        issue(errors, "$.on", "Workflow trigger is missing.")
    events = as_event_set(data.get("on"))
    if not events:
        issue(errors, "$.on", "Workflow trigger must be a string, array, or mapping.")

    jobs = data.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        issue(errors, "$.jobs", "Workflow must define at least one job.")
        return {"errors": errors, "warnings": warnings}

    top_permissions = data.get("permissions")
    if top_permissions is None:
        issue(warnings, "$.permissions", "Declare explicit least-privilege permissions.")
    elif isinstance(top_permissions, str) and top_permissions in {"write-all", "read-all"}:
        if top_permissions == "write-all":
            issue(errors, "$.permissions", "Do not use write-all permissions.")
        else:
            issue(warnings, "$.permissions", "read-all may be broader than required.")
    elif not isinstance(top_permissions, (dict, str)):
        issue(errors, "$.permissions", "Permissions must be a mapping or supported scalar.")

    has_pull_request_target = "pull_request_target" in events
    has_merge_group = "merge_group" in events

    for job_id, job in jobs.items():
        path = f"$.jobs.{job_id}"
        if not isinstance(job, dict):
            issue(errors, path, "Job must be a mapping.")
            continue

        has_uses = "uses" in job
        has_runs_on = "runs-on" in job
        if has_uses == has_runs_on:
            issue(errors, path, "Job must define exactly one of 'runs-on' or reusable workflow 'uses'.")

        if "permissions" in job and job["permissions"] == "write-all":
            issue(errors, f"{path}.permissions", "Do not use write-all permissions.")

        if has_runs_on and "timeout-minutes" not in job:
            issue(warnings, f"{path}.timeout-minutes", "Set a timeout for production workflows.")

        if has_uses:
            ref = str(job.get("uses", ""))
            if not ref.startswith("./") and "@" in ref:
                revision = ref.rsplit("@", 1)[1]
                if not SHA_PATTERN.fullmatch(revision):
                    issue(warnings, f"{path}.uses", "External reusable workflow is not pinned to a full commit SHA.")
            continue

        steps = job.get("steps")
        if not isinstance(steps, list) or not steps:
            issue(errors, f"{path}.steps", "Runner job must define a non-empty steps array.")
            continue

        for index, step in enumerate(steps):
            step_path = f"{path}.steps[{index}]"
            if not isinstance(step, dict):
                issue(errors, step_path, "Step must be a mapping.")
                continue

            if "uses" in step:
                action_ref = str(step["uses"])
                if action_ref.startswith(("./", "docker://")):
                    pass
                elif "@" not in action_ref:
                    issue(errors, f"{step_path}.uses", "Action reference must include @ref.")
                else:
                    revision = action_ref.rsplit("@", 1)[1]
                    if not SHA_PATTERN.fullmatch(revision):
                        issue(warnings, f"{step_path}.uses", "Action is not pinned to a full commit SHA.")

                if has_pull_request_target and action_ref.startswith("actions/checkout"):
                    with_block = step.get("with", {})
                    ref_value = str(with_block.get("ref", "")) if isinstance(with_block, dict) else ""
                    if any(token in ref_value for token in ("pull_request.head", "github.head_ref", "head.sha", "head.ref")):
                        issue(errors, f"{step_path}.with.ref", "Privileged pull_request_target workflow checks out untrusted pull request code.")

            if "run" in step:
                run_value = str(step["run"])
                for expr in UNTRUSTED_EXPRESSIONS:
                    if "${{ " + expr in run_value or "${{" + expr in run_value:
                        issue(errors, f"{step_path}.run", f"Untrusted context '{expr}' is interpolated directly into a shell script.")
                if "curl" in run_value and "${{ secrets." in run_value:
                    issue(warnings, f"{step_path}.run", "Secret is interpolated into a shell command; prefer environment variables and avoid command-line exposure.")

            if "continue-on-error" in step and step.get("continue-on-error") is True:
                issue(warnings, f"{step_path}.continue-on-error", "Ensure ignored failures are reported and do not bypass required checks.")

    if has_merge_group:
        # Presence is good; no warning required.
        pass

    for path, text in walk_strings(data):
        for pattern in SECRET_LITERAL_PATTERNS:
            if pattern.search(text):
                issue(errors, path, "Possible literal credential or private key detected.")

    if has_pull_request_target:
        issue(warnings, "$.on.pull_request_target", "Review the privileged trust boundary; avoid executing pull request code or exposing secrets.")

    return {"errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    args = parser.parse_args()

    try:
        data = yaml.load(args.workflow.read_text(encoding="utf-8"), Loader=WorkflowLoader)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.workflow}", file=sys.stderr)
        return 2
    except yaml.YAMLError as exc:
        print(f"ERROR: invalid YAML: {exc}", file=sys.stderr)
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
