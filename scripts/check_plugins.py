#!/usr/bin/env python3
"""Check local Copilot plugin packaging and reviewed third-party snapshots."""

import ast
import hashlib
import json
from pathlib import Path
import re

if __package__:
    from .evaluate import ROOT, local_path, read_json, require
else:
    from evaluate import ROOT, local_path, read_json, require


SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MANIFEST_FIELDS = {"$schema", "name", "version", "description", "author", "homepage",
                   "repository", "license", "keywords", "extensions"}
NAME = re.compile(r"(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?\Z")
VERSION = re.compile(r"\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?\Z")


def check_manifest(path):
    manifest = read_json(path)
    require(isinstance(manifest, dict), "Manifest must be an object")
    require(set(manifest) <= MANIFEST_FIELDS, "Unknown Agent Plugins manifest field")
    require(manifest.get("$schema") == SCHEMA, "Expected Agent Plugins 1.0 schema")
    name = manifest.get("name", "")
    require(isinstance(name, str) and 1 <= len(name) <= 64 and NAME.fullmatch(name),
            "Invalid plugin name")
    require(isinstance(manifest.get("version"), str) and VERSION.fullmatch(manifest["version"]),
            "Expected a semantic plugin version")
    require(isinstance(manifest.get("description"), str) and manifest["description"],
            "Missing plugin description")
    if "author" in manifest:
        require(isinstance(manifest["author"], dict)
                and set(manifest["author"]) <= {"name", "email", "url"}
                and all(isinstance(value, str) for value in manifest["author"].values()),
                "Invalid author metadata")
    require(all(isinstance(value, str) for value in manifest.get("keywords", [])),
            "Invalid plugin keywords")
    return manifest


def check_sources(root):
    lock = read_json(root / "third-party/sources.json")
    require(lock.get("schema_version") == 1, "Unknown source-lock format")
    imported = set()
    for component in lock.get("components", []):
        require(re.fullmatch(r"[a-f0-9]{40}", component.get("revision", "")),
                "Upstream source must use an exact commit")
        require(component.get("license") == "MIT" and component.get("modifications"),
                "Missing source license or adaptation record")
        for item in component.get("files", []):
            require(item["path"] not in imported, "Duplicate imported file")
            imported.add(item["path"])
            path = local_path(root, item["path"])
            require(path.is_file(), "Imported file is missing: " + item["path"])
            body = path.read_bytes()
            require(hashlib.sha256(body).hexdigest() == item.get("installed_sha256"),
                    "Imported file changed without source-lock review: " + item["path"])
            require(re.fullmatch(r"[a-f0-9]{40}", item.get("upstream_blob_sha1", "")),
                    "Missing upstream Git blob")
            if not item.get("adapted"):
                blob = hashlib.sha1(b"blob " + str(len(body)).encode() + b"\0" + body).hexdigest()
                require(blob == item["upstream_blob_sha1"], "Unmodified import differs from upstream")
            if path.name == "LICENSE":
                require(b"MIT License" in body and b"Copyright (c)" in body,
                        "Missing preserved license notice")
    require(bool(imported), "No reviewed imports found")
    return len(imported)


def validate(root=ROOT):
    catalog = read_json(root / ".github/plugin/marketplace.json")
    require(NAME.fullmatch(catalog.get("name", "")) and len(catalog["name"]) <= 64,
            "Invalid marketplace name")
    require(isinstance(catalog.get("owner"), dict) and catalog["owner"].get("name"),
            "Missing marketplace owner")
    require(isinstance(catalog.get("plugins"), list) and catalog["plugins"], "Empty marketplace")
    plugins = set()
    skills = set()
    agents = set()
    addon_cases = 0
    for entry in catalog["plugins"]:
        require(isinstance(entry.get("source"), str), "This catalog uses local relative sources")
        plugin_root = local_path(root, entry["source"])
        manifest = check_manifest(plugin_root / "plugin.json")
        require(entry.get("name") == manifest["name"] and entry.get("version") == manifest["version"],
                "Catalog and plugin identity/version differ")
        require(manifest["name"] not in plugins, "Duplicate plugin name")
        plugins.add(manifest["name"])
        local_skills = []
        for directory in sorted((plugin_root / "skills").glob("*")):
            if not directory.is_dir():
                continue
            require(not directory.is_symlink(), "Skill directory must not be a symlink")
            content = (directory / "SKILL.md").read_text()
            require(re.search(r"^name: " + re.escape(directory.name) + r"$", content, re.M),
                    "Skill name does not match its folder")
            require("Generated code must contain no AI attribution." in content,
                    "Skill is missing output-isolation guidance")
            require(directory.name not in skills, "Duplicate installed skill name")
            skills.add(directory.name)
            local_skills.append(directory.name)
            for script in (directory / "scripts").glob("*.py"):
                ast.parse(script.read_text(), filename=str(script))
        local_agents = []
        for path in (plugin_root / "com.github.copilot/agents").glob("*.agent.md"):
            content = path.read_text()
            require(content.startswith("---\n") and "\n---\n" in content,
                    "Agent is missing frontmatter")
            frontmatter = content.split("---\n", 2)[1]
            require(re.search(r"^description: .+", frontmatter, re.M), "Agent is missing description")
            require(re.search(r"^infer: false$", frontmatter, re.M),
                    "Bundled agents currently require explicit selection")
            require("include-custom-instructions: true" in frontmatter,
                    "Agent must load repository instructions")
            require(path.name not in agents, "Duplicate installed agent name")
            agents.add(path.name)
            local_agents.append(path.name)
        require(local_skills or local_agents, "Plugin contributes no skills or agents")
        cases_path = plugin_root / "evals/cases.json"
        if plugin_root != root.resolve():
            cases = read_json(cases_path)
            require(cases.get("plugin") == manifest["name"] and cases.get("schema_version") == 1,
                    "Add-on evaluation suite does not match plugin")
            identifiers = set()
            for case in cases.get("cases", []):
                require(case.get("id") and case["id"] not in identifiers, "Duplicate add-on case")
                identifiers.add(case["id"])
                require(case.get("prompt") and case.get("expected") and case.get("required_evidence"),
                        "Incomplete add-on case")
            require(bool(identifiers), "Add-on has no evaluation cases")
            addon_cases += len(identifiers)
    return {"plugins": len(plugins), "skills": len(skills), "agents": len(agents),
            "addon_review_cases": addon_cases, "locked_imports": check_sources(root),
            "live_model_evaluations_run": 0}


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), indent=2))
    except (ValueError, OSError, KeyError, TypeError, SyntaxError) as error:
        raise SystemExit(str(error))
