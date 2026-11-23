# UI Engineer Skill

A personal frontend delivery skill for component work, secure GitHub Actions, and bounded gh-aw maintenance. Copy the entire `ui-engineer` directory; no other skill in this collection is required.

## Contents

```text
ui-engineer/
|-- agents/
|   `-- openai.yaml
|-- guides/
|   |-- agentic-workflows.md
|   |-- automation-recipes.md
|   |-- deterministic-ci.md
|   |-- frontend-delivery.md
|   |-- repository-practices.md
|   `-- sources.md
|-- templates/
|   |-- dynamic-review/
|   |   |-- extension.mjs.template
|   |   `-- workflow.mjs.template
|   |-- ci-doctor.md.template
|   |-- docs-sync.md.template
|   |-- dynamic-review.md.template
|   |-- preview-deploy.yml.template
|   `-- ui-ci.yml.template
|-- README.md
|-- SKILL.md
|-- examples.md
|-- references.json
`-- sources.json
```

## Install

From the collection root, install into your application repository:

```sh
mkdir -p /path/to/application/.github/skills
cp -Ri skills/ui-engineer /path/to/application/.github/skills/
```

For personal Copilot CLI use:

```sh
mkdir -p "$HOME/.copilot/skills"
cp -Ri skills/ui-engineer "$HOME/.copilot/skills/"
```

The copy prompts before overwriting existing files. For Codex, use `.agents/skills/`; for Claude Code, use `.claude/skills/`; for another compatible host use its documented directory. Start a new session and request `ui-engineer` (Codex: `$ui-engineer`; Claude Code: `/ui-engineer`). No compiler, plugin, credentials, or workflow runs are installed by copying a skill.

The collection's `ui-engineer` Copilot plugin includes this skill together with the existing UI library. Plugin and skill identifiers are separate. Avoid installing duplicate copies through both routes.

## Use

```text
Use ui-engineer to audit our React workspace CI. Inspect packages/ui,
apps/web, shared dependencies, root scripts, and required checks.
Propose a minimal correction for fork safety, Storybook/Playwright,
and pending path-filtered checks. Keep hosted settings as proposals.
```

```text
Use ui-engineer to design CI Doctor for the UI CI workflow. Use gh-aw
with Copilot, read-only investigation, deduplicated bounded reports,
and no automatic patches or reruns. Ask about unresolved billing and
output policy; compile locally if prerequisites exist. Do not dispatch.
```

See [examples.md](examples.md) for detailed inputs, outcomes, and verification.

## Template Contracts

Templates are starting points, not active workflows. Adapt and validate them before copying into `.github/workflows/`.

| Template | Required adaptation |
| --- | --- |
| `templates/ui-ci.yml.template` | pnpm pinned in root `packageManager`; runtime in `.nvmrc`; root scripts `lint`, `typecheck`, `test:unit`, `build`, `build-storybook`, `test:storybook`, `test:e2e`; Playwright web-server configuration and report paths |
| `templates/preview-deploy.yml.template` | Trusted-ref preview provider command, OIDC trust, `preview` environment, and approved deployment script |
| `templates/ci-doctor.md.template` | Exact producer workflow name, reporting policy, supported gh-aw version, and Copilot authentication |
| `templates/docs-sync.md.template` | Actual docs roots, check commands if needed, authentication, and optional approved schedule |
| `templates/dynamic-review.md.template` | Explicit experimental opt-in, compatible runtime/account, and extension files below |
| `templates/dynamic-review/*.mjs.template` | Copy as `extension.mjs` and `workflow.mjs` under `.github/extensions/ui-review/`; verify compatible SDK export and execution support |

For npm use `npm ci`; for Yarn use the repository's frozen/immutable mode. Vue/Svelte packages use their existing check/build/test scripts; Next.js SSR builds and preview hosting need their real server/environment contract. Do not change tools to fit the sample.

The CI skeleton intentionally runs on every PR so its gate remains reportable. Its optional path-filter example is in the deterministic CI guide. Narrow expensive jobs through a validated affected-work calculation when the repository needs it.

## Source and Verification Boundaries

The guides synthesize the three required source projects; they are not wholesale copies of upstream workflows. [Source notes](guides/sources.md) and [sources.json](sources.json) record reviewed revisions and file paths. Inspect current official syntax against your installed tool version before adopting experimental fields.

Bundled templates do not configure GitHub settings, enable a provider, supply secrets, trigger paid inference, or prove hosted behavior. Generated code must contain no AI attribution. Preserve legitimate legal notices and required compiler metadata.
