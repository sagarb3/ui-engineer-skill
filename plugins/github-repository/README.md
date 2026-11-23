# GitHub Repository Engineering Add-on

This optional Copilot CLI plugin bundles an adapted copy of [he8um/github-skills](https://github.com/he8um/github-skills), pinned to the revision recorded in [the source lock](https://github.com/sagarb3/ui-engineer-skill/blob/main/third-party/sources.json). Its MIT license and copyright are preserved in [LICENSE](LICENSE).

## Install

```sh
copilot plugin marketplace add sagarb3/ui-engineer-skill
copilot plugin install github-repository@ui-engineer-skills
```

This installs the `github-skills` instruction package with its references, templates, schemas, helpers, and example blueprint. It does not apply templates, change hosted settings, install Python packages, or run workflows.

## Use Cases

**Read-only repository audit:**

```text
Use github-skills to audit our repository files and Actions workflows.
Separate confirmed local findings from hosted settings you cannot inspect.
Rank concrete issues and suggest a scoped remediation plan. Do not edit
files, change settings, post messages, or publish a release.
```

**Reviewable repository blueprint:**

```text
Use github-skills to plan a public TypeScript library repository. Inspect
existing conventions and ask about undecided license, ownership, and
release requirements. Prepare complete proposed files and a repository
blueprint JSON. Validate what the installed tools support, and keep
hosted setting changes as proposals until they are authorized.
```

Expected outputs are actionable findings or a complete, scoped proposal. Neither example asserts that work has been executed. Generated product artifacts must not contain this collection's attribution or authoring provenance; legitimate legal notices remain.

## Optional Helper Dependencies

Instructions and templates are usable without running a helper. The imported helpers require Python 3.10 or later. Workflow validation and repository-package auditing also require `PyYAML>=6.0,<7.0`. Install prerequisites only when needed and authorized, preferably in an isolated environment.

The scripts are under the loaded skill's `scripts/` directory. Resolve that directory from the installed skill location rather than running an unrelated `scripts/` path in the application. The bundled example blueprint is at `skills/github-skills/examples/sample-repository-blueprint.json` within this plugin.

## Evaluation

The local review cases in [evals/cases.json](evals/cases.json) describe scope, evidence, template, and settings boundaries. They are separate from the original collection's 50 core cases and have not been run against a live model by their existence alone.
