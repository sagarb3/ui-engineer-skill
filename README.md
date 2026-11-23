# React UI Agent Skills

English-only Agent Skills for practical React UI engineering and everyday Git work. Built for GitHub Copilot CLI first, with portable `SKILL.md` instructions for Cursor, Codex, Claude Code, OpenCode, and other compatible tools.

The ten skills include working procedures, decision tables, concrete examples, failure handling, red flags, and verification criteria. They include 39 supporting guides, ten local reference indexes, skill UI metadata, and 50 evaluation cases. Each skill is complete in its own folder and requires no companion skill, bundled upstream material, or runtime dependency. Repository evaluation tooling uses Python and Git separately from skill installation.

## Working Style

Make the smallest complete change. Reuse what the project already has. Keep React state ownership clear, component APIs explicit, tests focused on user behavior, and interfaces accessible. Follow the project's existing naming, formatting, typing, and architecture instead of imposing a new style.

Run straightforward, authorized Git commands directly. Stop and ask when requirements are ambiguous, incomplete, or have multiple interpretations. Always ask before force pushes, hard resets, or deleting branches/files, and before other destructive operations or history rewriting. Existing approval for the exact action and target remains valid.

## Output Isolation

**Generated code must contain no AI attribution.** Downstream code, comments, commit messages, and documentation must never mention or link back to this skills repository, a parent agent, or the tool that wrote them. Do not add generated-by comments, promotional links, or attribution trailers. Preserve existing legal notices and unrelated attribution.

All newly written content must be in English. These skills describe working rules; they do not technically enforce output compliance. Review the resulting diff. Tool names and paths below are installation metadata, not text to insert into product code or documentation. Keep installed skill instructions separate from application artifacts.

## Installation

Start from a local checkout or downloaded copy of this repository. The commands below are for a POSIX shell on macOS, Linux, or WSL. Run them from the collection's root, where `skills/` exists. They install instruction files only; no runtime packages are required.

### 1. GitHub Copilot CLI

For personal use across local projects:

```sh
mkdir -p "$HOME/.copilot/skills"
cp -Ri skills/. "$HOME/.copilot/skills/"
```

`-i` prompts before replacing an existing file. Review collisions rather than overwriting local customization. Start a new Copilot CLI session, or run `/skills reload` in an existing session. Ask: `Use harness for this session. Use react-component-practices to update the form.`

For team use, copy individual skill folders into the target project's `.github/skills/`, preserving paths such as `.github/skills/harness/SKILL.md`. Install only the skills the team needs. Avoid duplicate copies of the same skill across discovery locations. See [Copilot CLI skill installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

### 2. Cursor

Use the same copy command with `.cursor/skills/` in the target project, or `~/.cursor/skills/` for personal use. Start a new session and request the skill by name. See [Cursor skill directories](https://cursor.com/docs/skills).

### 3. Codex

Use `.agents/skills/` in the target project, or `~/.agents/skills/` for personal use. Start a new session and invoke `$harness` or `$react-component-practices`. See [Codex local skill discovery](https://learn.chatgpt.com/docs/build-skills).

### 4. Claude Code

Use `.claude/skills/` in the target project, or `~/.claude/skills/` for personal use. Start a new session and invoke `/harness` or `/react-component-practices`. See [Claude Code skills](https://code.claude.com/docs/en/skills).

### 5. OpenCode

Use `.opencode/skills/` in the target project, or `~/.config/opencode/skills/` for personal use. Start a new session and request the skill by name. See [OpenCode skills](https://opencode.ai/docs/skills/).

For example, to install personally for Cursor from this collection's root:

```sh
skill_destination="$HOME/.cursor/skills"
mkdir -p "$skill_destination"
cp -Ri skills/. "$skill_destination/"
```

Replace the destination with the documented directory for your tool. For project installs, use an absolute destination in the target application repository, not a relative directory in this collection. Other compatible agents can use the same skill folders in their documented discovery directory. Check discovery and activation in the installed tool; this collection does not claim runtime testing across every client.

## Make Harness the Baseline

Skills are normally loaded when selected or relevant. A skill named `harness` does not automatically run for every task. Request it at session start, or merge the following standalone rules into the target project's existing baseline instructions:

```text
Prefer the smallest complete change and existing project conventions.
Stop and ask when requirements are ambiguous, incomplete, or have multiple interpretations.
Execute straightforward, authorized Git commands directly.
Ask before force pushes, hard resets, deleting branches/files, destructive actions, or history rewriting.
Write new content in English. Add no AI attribution, workflow provenance, authoring-tool names, or source links to generated artifacts. Preserve existing legal notices.
Keep validation, error handling, security, and accessibility intact.
Use concise trim behavior only when requested; report checks truthfully.
```

For Copilot CLI, use [`.github/copilot-instructions.md`](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions); for Codex and OpenCode, use the existing `AGENTS.md`; for Claude Code, use `CLAUDE.md`. For Cursor, merge these rules into a [project rule](https://cursor.com/docs/rules) such as `.cursor/rules/working-style.mdc` with `alwaysApply: true` in its YAML frontmatter. Review and preserve existing instructions; create the appropriate file if absent. The block is deliberately standalone so the baseline does not link product work back to this collection. It does not grant permission for additional Git or external actions.

## Skills

| Skill | Purpose |
| --- | --- |
| [harness](skills/harness/SKILL.md) | Baseline workflow, clarification, small changes, and isolation |
| [git-tooling](skills/git-tooling/SKILL.md) | Direct routine Git operations with explicit destructive-action boundaries |
| [trim-mode](skills/trim-mode/SKILL.md) | Minimal complete implementation and short action-first replies |
| [ui-design-direction](skills/ui-design-direction/SKILL.md) | Visual hierarchy, responsive layout, and rendered verification |
| [react-component-practices](skills/react-component-practices/SKILL.md) | Pure rendering, state ownership, hooks, and effects |
| [vitest-react-testing](skills/vitest-react-testing/SKILL.md) | Behavior-focused Vitest and React Testing Library tests |
| [react-accessibility](skills/react-accessibility/SKILL.md) | Semantics, keyboard use, focus, forms, and manual verification |
| [design-system-consistency](skills/design-system-consistency/SKILL.md) | Existing tokens, components, themes, and interaction patterns |
| [react-ui-performance](skills/react-ui-performance/SKILL.md) | Measured bottlenecks and comparable before-and-after checks |
| [component-api-design](skills/component-api-design/SKILL.md) | Small prop contracts, composition, ownership, and compatibility |

Request a skill by name in plain language when your client has no explicit invocation syntax. Skills remain self-contained; none requires another installed skill. Their verification criteria describe evidence to gather, not checks that have already run.

## Skill Packaging

Each skill folder contains the same core packaging:

```text
skill-name/
|-- SKILL.md
|-- references.json
|-- guides/
|   `-- task-specific-guides.md
`-- agents/
    `-- openai.yaml
```

`SKILL.md` routes tasks to relevant guides. `references.json` maps local guide paths, titles, and reading triggers; it is a documented collection convention, not a universal agent configuration. Each of the nine non-design skills has three supporting guides; the UI design skill has twelve. Copy the whole skill folder to preserve these files.

`agents/openai.yaml` supplies skill UI metadata. It does not create a specialist agent or start a subagent. See [skills versus specialist agents](docs/agents.md) for profile creation, native client formats, permissions, and automatic delegation boundaries.

## Use the Detailed Guidance

Start with the selected skill's process, then apply the detailed sections relevant to the task. A local correction does not require executing every workflow in the file. Thorough guidance should improve decisions, not turn a one-command Git request into a planning exercise.

| Task | Guidance to apply |
| --- | --- |
| Implement a feature without changing architecture | Harness task contract, responsible layer, implementation discipline, and completion evidence |
| Commit, switch branches, pull, or push | Git operation table, concrete recipes, conflict recovery, and approval boundaries |
| Reduce scope and reply length on request | Trim decision ladder, complete-change rules, worked choice, and response examples |
| Establish or refine a screen | Design direction, information hierarchy, visual choices, responsive behavior, and state model |
| Change React behavior | State ownership, rendering rules, effects, asynchronous races, identity, forms, and framework boundaries |
| Add behavior-focused tests | Query selection, interaction example, asynchronous states, mock boundaries, and test limitations |
| Repair accessibility | Interaction contract, labeled-field example, keyboard and focus, dynamic feedback, and visual checks |
| Align UI with existing conventions | Canonical patterns, reuse order, tokens, library integration, themes, and shared-change impact |
| Resolve a slow interaction | Reproducible baseline, bottleneck evidence, targeted optimizations, and comparable measurements |
| Design component props | Real consumers, valid states, controlled ownership, composition, native behavior, and compatibility |

Code examples illustrate a specific contract. Adapt paths, types, tokens, component props, and commands to the target project after checking its installed versions and conventions. Do not paste an example that changes the product's requirements or introduces unnecessary dependencies. A skill's example is not evidence that the target application has passed its checks.

Detailed instructions do not activate trim mode automatically. Ask for depth when an explanation is needed, and request trim mode when a shorter working style is useful. Both modes retain correctness, validation, error handling, security, and accessibility.

## UI Design Guides

The UI design skill includes twelve original English guides inside its own folder. Its [workflow table](skills/ui-design-direction/SKILL.md#select-the-workflow) distinguishes small corrections, new screens, comparisons, screenshot reconstruction, read-only reviews, and design-rule work. Its [guide index](skills/ui-design-direction/SKILL.md#detailed-guides) tells the agent what to read for the current task.

| Area | Detailed guides |
| --- | --- |
| Direction and visual execution | [Briefs, distinctive concepts, first-screen structure, and comparisons](skills/ui-design-direction/guides/design-brief-and-exploration.md); [typography, spacing, color, controls, and realistic content](skills/ui-design-direction/guides/visual-composition.md) |
| Reconstruction and imagery | [Viewport measurement, screenshot fidelity, and responsive behavior](skills/ui-design-direction/guides/responsive-reconstruction.md); [image-led concepts and implementation](skills/ui-design-direction/guides/image-led-design.md) |
| Media and interactive objects | [Images, textures, asset sets, video, and 3D](skills/ui-design-direction/guides/media-and-assets.md); [games, tactile controls, canvas, timers, and safe state transitions](skills/ui-design-direction/guides/interactive-experiences.md) |
| Movement and narrative | [Feedback, interruption, route transitions, and reduced motion](skills/ui-design-direction/guides/motion-and-transitions.md); [scroll-linked stories, reveals, parallax, and pinned scenes](skills/ui-design-direction/guides/scroll-storytelling.md) |
| Separate quality checks | [Visual review and readiness findings](skills/ui-design-direction/guides/visual-review.md); [task completion, discoverability, and recovery walkthroughs](skills/ui-design-direction/guides/usability-walkthrough.md) |
| Evidence and delivery | [Browser operation, screenshots, recordings, and evidence limits](skills/ui-design-direction/guides/browser-evidence.md); [temporary artifacts, existing design rules, assets, and final delivery](skills/ui-design-direction/guides/task-artifacts-and-design-rules.md) |

Install or copy the entire `ui-design-direction` folder, including `guides/`; the installation commands above already do this. The guides use the host's available capabilities and the target project's existing tools. They do not bundle a browser runner, media service, image generator, or comparison-page utility. Independent concept work or review is conditional on explicit authorization and actual availability; otherwise the work is identified as self-assessed.

## Activate Trim Mode

Say `trim`, `be minimal`, `ponytail`, `lazy senior`, `be lazy`, or `ADHD mode` as a working-style request. For example: `Use trim-mode and fix the dialog's focus restoration.` Explicitly selecting `trim-mode` avoids confusion with another installed skill that shares a trigger.

Trim mode checks necessity, existing code, standard-library/platform support, installed dependencies, and a readable single expression before adding minimal code. It keeps replies short, numbered, and action-first, ending with one concrete next step. It never cuts correctness, validation, error handling, security, or accessibility. Say `turn off trim mode` to return to normal output.

## Verification

Each skill includes task-specific verification criteria. Run the target project's relevant checks and required gates; report blockers and checks that were not run. UI tests in a simulated DOM do not replace real-browser layout, keyboard, or assistive-technology checks.

Before sharing changes, review the diff for English-only additions, scope, secrets, accidental provenance, and attribution fingerprints. Keep the installed instructions out of application bundles and generated product documentation.

## Evaluations

The [evaluation suite](evals/README.md) contains five cases for each skill, with local fixtures, explicit review criteria, and support for baseline versus with-skill preparation. Cases cover normal work, ambiguity, scope, safeguards, activation, and multi-turn mode behavior.

```sh
python3 scripts/evaluate.py validate
python3 scripts/evaluate.py list
python3 -m unittest discover -s tests -v
```

The tool checks collection structure, prepares isolated local repositories, and summarizes evidence-backed reviews. It does not call models or run client sessions automatically. An unrun case stays incomplete; structural validation and passing tool tests do not count as passing skill evaluations. See the evaluation README for preparation, environment isolation, fixture limits, reviewer evidence, scoring, and paired comparison.
