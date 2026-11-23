# Copilot CLI Plugin Maintenance

This repository is a GitHub-hosted Copilot CLI marketplace with three versioned plugins. A public repository and a marketplace catalog do not imply inclusion in GitHub's built-in marketplace, official endorsement, or a verified Marketplace App listing.

## Stable Identifiers

| Plugin | Source | Included components |
| --- | --- | --- |
| `ui-engineer` | Repository root | Ten original skills, guides, examples, indexes, and metadata |
| `github-repository` | `plugins/github-repository` | Adapted GitHub repository-engineering skill, references, templates, schemas, and helpers |
| `agentic-workflows` | `plugins/agentic-workflows` | Adapted workflow routing skill and explicitly selected Copilot agent |

The marketplace identifier is `ui-engineer-skills`. Keep these identifiers stable: users install `plugin@marketplace`, and renaming changes their installation identity.

All plugin manifests use Agent Plugins 1.0. Skills are immediate children of each plugin's `skills/` directory. Copilot-specific profiles are under `com.github.copilot/agents/`. Do not add legacy configurable component fields to a manifest that declares the canonical schema.

## Install and Update

```sh
copilot plugin marketplace add sagarb3/ui-engineer-skill
copilot plugin marketplace browse ui-engineer-skills
copilot plugin install ui-engineer@ui-engineer-skills
```

Install optional packages separately:

```sh
copilot plugin install github-repository@ui-engineer-skills
copilot plugin install agentic-workflows@ui-engineer-skills
```

Refresh the catalog before checking for package changes:

```sh
copilot plugin marketplace update ui-engineer-skills
copilot plugin update ui-engineer
copilot plugin list
```

Update each installed add-on by its own plugin name. Restart the session to use changed context as required by the installed client. Do not enable global auto-update or override managed policy on the user's behalf.

The core plugin can also be installed directly with `copilot plugin install sagarb3/ui-engineer-skill`. Avoid duplicate manual and plugin copies of the same skills; decide which installation to retain before removing anything.

## Version a Change

1. Inspect the affected skill, agent, guides, examples, and evaluations. Keep accepted behavior and output isolation intact.
2. Update the plugin's semantic version and the matching catalog entry together. Use a patch for a compatible correction, a minor version for additive capability, and a major version for a breaking contract or distribution change.
3. Refresh relevant cases and source-lock records when their inputs change. Run the model-free checks below, then perform the appropriate native-client and behavior checks.
4. Review and commit through the repository's normal Git process. Publish a tag or release only when that publication is authorized.

An instruction edit can change behavior even if its file extension is Markdown. Evaluate the affected contract, not just JSON syntax. No live-model pass rate is implied by structural checks.

The initial manifests declare `0.1.0`. A version field alone does not create a Git tag or GitHub Release. Advertise a tag-based pin only after that tag is actually published.

## Validate Before Publishing

```sh
python3 scripts/evaluate.py validate
python3 scripts/check_plugins.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The first command covers the original ten skills and 50 core cases. The second checks manifest/catalog agreement, fixed component locations, local source boundaries, add-on review cases, and pinned imported-file integrity. Unit tests cover the preparation, review, and packaging helpers. None of these commands calls a model or starts a workflow.

For a native installation check, use an isolated Copilot configuration and a temporary checkout rather than changing a user's normal profile. Register the local marketplace, install the selected packages, inspect plugin and skill discovery, and verify explicit agent selection. Record the actual client version. Validate live workflow or model behavior separately when the required tools, account, environment, and authorization exist.

Local registration, all three installs, and twelve-skill discovery were verified with Copilot CLI 1.0.114 using a temporary profile. The native agent file is checked structurally; live agent dispatch, model behavior, and hosted runs were not exercised.

The validation workflow in `.github/workflows/validate.yml` runs the model-free commands on changes and pull requests. It does not install the add-ons' optional helper dependencies, call a model, provision an engine, or execute gh-aw workflows.

## Update Third-party Material

Read [the notices](../THIRD_PARTY_NOTICES.md) and [source lock](../third-party/sources.json). Select an immutable upstream commit, inspect the diff and license, and import only the intended package files. Preserve copyright notices and the documented local adaptations.

For each imported file, record the upstream path and Git blob, installed SHA-256, and adaptation status. An unchanged file must still match its original Git blob. Changes to an adapted file must receive a reviewed lock update; do not refresh hashes blindly merely to make checks pass.

Keep upstream runtime dependencies explicit. In particular, workflow prompt access and the gh-aw runtime are not supplied by importing the Agentics dispatcher. The GitHub repository helper's Python and PyYAML requirements are separate from basic skill installation.

No install hook or automatic upstream synchronization is provided. Update content through a reviewed repository change so future enhancements remain inspectable and reversible.

## Roll Back

Retain a reviewed earlier revision or published version before updating. Use the client's supported version/source mechanism or revert a content change through normal Git review. Do not force push, delete a version, or modify managed settings to recover silently.

Plugin disable and uninstall are user-controlled operations. They do not undo source files or hosted settings that an agent changed during an authorized task; those changes require their own rollback plan.
