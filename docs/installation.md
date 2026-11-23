# Installation and Activation

Skills are instruction packages, not runtime dependencies. Install only the skills your team needs and copy each complete folder, including its guides, reference index, `examples.md`, and UI metadata. Each example file contains two practical scenarios with prompts, expected deliverables, and verification; skill UI metadata includes a concrete starting prompt.

## GitHub Copilot CLI

The recommended path is the versioned Copilot CLI plugin marketplace:

```sh
copilot plugin marketplace add sagarb3/ui-engineer-skill
copilot plugin marketplace browse ui-engineer-skills
copilot plugin install ui-engineer@ui-engineer-skills
```

Optional packages install independently:

```sh
copilot plugin install github-repository@ui-engineer-skills
copilot plugin install agentic-workflows@ui-engineer-skills
```

Start a new session and inspect `copilot plugin list` and `copilot skill list`. The core package contributes eleven skills; the optional packages add one skill each. Use `/agent` to select the optional `agentic-workflows` profile explicitly. No workflow runtime, secrets, engine, or application dependency is installed.

Update the catalog and each selected package explicitly:

```sh
copilot plugin marketplace update ui-engineer-skills
copilot plugin update ui-engineer
```

See [plugin maintenance](plugin-maintenance.md) for independent add-on updates, versioning, validation, and rollback. This is a repository-hosted marketplace, not a claim of built-in catalog inclusion. Use a current plugin-capable CLI; local installation and discovery of all eleven core skills for version 0.2.0 were checked with Copilot CLI 1.0.114. Live model behavior and hosted workflow execution were not tested.

### Manual Core Skill Installation

For teams distributing reviewed folders rather than plugins, clone the repository and copy complete core skills:

```sh
git clone https://github.com/sagarb3/ui-engineer-skill.git
cd ui-engineer-skill
mkdir -p "$HOME/.copilot/skills"
cp -Ri skills/. "$HOME/.copilot/skills/"
```

The interactive copy flag asks before replacing existing files. Review collisions rather than overwriting local customization. Start a new session or enter `/skills reload` in an existing session.

For team use, place approved skill folders in the target application's `.github/skills/` directory. For example, the harness entry point should be `.github/skills/harness/SKILL.md`. Use an explicit destination in the application repository; do not accidentally install into this collection's checkout.

Avoid duplicate manual and plugin copies of a skill. Consult [Copilot CLI skill installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) and the [plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) for current behavior.

## Other Supported Clients

| Client | Project location | Personal location | Explicit use |
| --- | --- | --- | --- |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills/` | `~/.cursor/skills/` | Request the skill by name |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/` | `~/.agents/skills/` | `$harness` or another skill name |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/` | `~/.claude/skills/` | `/harness` or another skill name |
| [OpenCode](https://opencode.ai/docs/skills/) | `.opencode/skills/` | `~/.config/opencode/skills/` | Request the skill by name |

Start a new session after installation and verify discovery in the installed client. This collection supplies portable skill content and client-specific installation paths; it does not claim live runtime validation across every host and version.

For example, to install personally for Cursor from the collection's root:

```sh
skill_destination="$HOME/.cursor/skills"
mkdir -p "$skill_destination"
cp -Ri skills/. "$skill_destination/"
```

Commands are for a POSIX shell on macOS, Linux, or WSL. Other compatible agents can use the same skill folders in their documented discovery directory. Keep installed instructions separate from application bundles and generated product documentation.

## Make Harness the Baseline

A discovered skill is not automatically active in every task. Request `harness` at session start or merge the following standalone rules into the application's existing baseline instructions:

```text
Prefer the smallest complete change and existing project conventions.
Stop and ask when requirements are ambiguous, incomplete, or have multiple interpretations.
Execute straightforward, authorized Git commands directly.
Ask before force pushes, hard resets, deleting branches/files, destructive actions, or history rewriting.
Write new content in English. Add no AI attribution, workflow provenance, authoring-tool names, or source links to generated artifacts. Preserve existing legal notices.
Keep validation, error handling, security, and accessibility intact.
Use concise trim behavior only when requested; report checks truthfully.
```

For Copilot CLI, use [`.github/copilot-instructions.md`](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions). Codex and OpenCode can use the existing `AGENTS.md`; Claude Code uses `CLAUDE.md`. For Cursor, use a [project rule](https://cursor.com/docs/rules), such as `.cursor/rules/working-style.mdc`, with `alwaysApply: true` in its YAML frontmatter.

Preserve existing instructions and resolve conflicts before changing behavior. The baseline text does not link application work back to this collection or grant additional Git or external-action permissions.

## Activate Trim Mode

Request `trim`, `be minimal`, `ponytail`, `lazy senior`, `be lazy`, or `ADHD mode` as a working style. For example:

```text
Use trim-mode and fix the dialog's focus restoration.
```

Explicitly selecting `trim-mode` avoids ambiguity with another installed skill that shares a trigger. The mode reduces optional scope and reply length while preserving complete behavior, validation, error handling, security, and accessibility. Say `turn off trim mode` to return to normal output.

Quoted trigger words in source content do not activate the mode. See the [operating model](operating-model.md) for scope, verification, and isolation rules.
