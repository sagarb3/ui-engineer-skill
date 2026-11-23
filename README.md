<p align="center">
  <img src="assets/readme-hero.svg" alt="UI Engineer Skills: consistent UI, reviewable delivery. Shared engineering standards for React teams and their coding tools." width="100%">
</p>

<h1 align="center">UI Engineer Skills</h1>

<p align="center">
  <strong>Give every UI change a shared engineering standard.</strong><br>
  Practical, versioned workflows for React design, implementation, accessibility, testing, and Git.<br>
  Built for GitHub Copilot CLI, with portable skills for Cursor, Codex, Claude Code, and OpenCode.
</p>

<p align="center">
  <a href="https://sagarb3.github.io/ui-engineer-skill/">Website</a> &nbsp; / &nbsp;
  <a href="#quick-start">Get started</a> &nbsp; / &nbsp;
  <a href="#the-skill-library">Explore the skills</a> &nbsp; / &nbsp;
  <a href="#skill-examples">Try the examples</a> &nbsp; / &nbsp;
  <a href="#evaluate-before-you-roll-out">Review the evaluation model</a> &nbsp; / &nbsp;
  <a href="docs/enterprise-adoption.md">Plan a team rollout</a>
</p>

<p align="center">
  <strong>10 focused skills</strong> &nbsp; / &nbsp;
  <strong>39 supporting guides</strong> &nbsp; / &nbsp;
  <strong>50 evaluation cases</strong> &nbsp; / &nbsp;
  <strong>5 client setup paths</strong>
</p>

**[View the website](https://sagarb3.github.io/ui-engineer-skill/)** · [Standalone HTML file](README.html)

## Shared standards. Applied where the work happens.

Teams already have components, review expectations, accessibility requirements, and delivery controls. This collection helps coding tools work within those conventions, from the first design decision to the final Git operation.

Each skill provides a practical process, decision rules, failure cases, and verification criteria. Detailed guides load according to the task. Everything lives in ordinary, reviewable repository files.

<table>
  <tr>
    <td width="33%" valign="top">
      <strong>Consistency across contributors</strong><br><br>
      Reuse existing tokens, components, state ownership, and project conventions. Make important decisions explicit before implementation.
    </td>
    <td width="33%" valign="top">
      <strong>Changes reviewers can assess</strong><br><br>
      Prefer small, complete changes with clear scope, preserved behavior, and practical Git workflows.
    </td>
    <td width="33%" valign="top">
      <strong>Evidence behind the handoff</strong><br><br>
      Match verification to the claim. Separate passing tests, browser observations, performance measurements, and unverified assumptions.
    </td>
  </tr>
</table>

## Quick start

Install through the GitHub Copilot CLI plugin marketplace:

```sh
copilot plugin marketplace add sagarb3/ui-engineer-skill
copilot plugin install ui-engineer@ui-engineer-skills
```

Start a new session and request a skill by name. This installs the ten core skills with their supporting resources. No application dependencies are added.

Try a focused request in your application repository:

```text
Use harness and react-accessibility to review the checkout form.
Identify keyboard, focus, and labeling barriers. Do not edit files.
```

For team distribution, copy approved skill folders into the application's `.github/skills/` directory. Pin a reviewed revision and preserve existing project instructions. A discovered skill does not automatically become the baseline for every task.

**[Full installation and activation guide](docs/installation.md)**

<details>
<summary><strong>Use Cursor, Codex, Claude Code, or OpenCode</strong></summary>

| Client | Project skills | Personal skills |
| --- | --- | --- |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` |

Copy complete skill folders, including guides and metadata, then verify discovery in the installed client. See the [installation guide](docs/installation.md#other-supported-clients) for invocation details and official documentation. Live behavior must be verified against the host and version your team uses.

</details>

## Copilot CLI marketplace

Choose the packages your team needs. The core React library stays independent of the optional repository and workflow tools.

| Plugin | Included | Install |
| --- | --- | --- |
| **UI Engineer** | Ten React UI and practical Git skills, 39 guides, and worked examples | `copilot plugin install ui-engineer@ui-engineer-skills` |
| [GitHub Repository](plugins/github-repository/README.md) | Repository engineering skill, reference material, templates, schemas, and Python validators | `copilot plugin install github-repository@ui-engineer-skills` |
| [Agentic Workflows](plugins/agentic-workflows/README.md) | Workflow routing skill and an explicitly selected Copilot agent | `copilot plugin install agentic-workflows@ui-engineer-skills` |

With all three installed, the collection supplies **12 skills and one native Copilot agent**. Each optional package includes two practical use cases and five review scenarios. Browse and update through the CLI:

```sh
copilot plugin marketplace browse ui-engineer-skills
copilot plugin marketplace update ui-engineer-skills
copilot plugin update ui-engineer
```

Update installed add-ons by their own names. See [plugin maintenance](docs/plugin-maintenance.md) for versioning, validation, upstream updates, and rollback. This is a repository-hosted marketplace; it does not claim GitHub endorsement or inclusion in the built-in catalog.

### Optional package examples

**Repository engineering:** install `github-repository`, then ask:

```text
Use github-skills to review this repository's contribution and release
workflow. Inspect existing files first. Propose a minimal blueprint and
validate it with the bundled helper. Do not publish settings or releases.
```

The [repository package examples](plugins/github-repository/README.md#use-cases) include a repository blueprint and CI review. The helpers require Python 3.10+; YAML-related helpers additionally need PyYAML, as documented in the package.

**Workflow engineering:** install `agentic-workflows`, start a new session, and use `/agent` to select `agentic-workflows`:

```text
Design a manually triggered CI health report using agentic-workflows.
Review existing workflows and propose the local source. Ask about any
missing destination or permissions before implementing. Do not trigger
a hosted run or configure secrets.
```

The [workflow package examples](plugins/agentic-workflows/README.md#use-cases) cover creation and debugging. The agent is explicitly selected (`infer: false`). Remote guidance, gh-aw tooling, authentication, and engine configuration are separate prerequisites; installation does not configure or run them.

The optional packages adapt MIT-licensed material from [he8um/github-skills](https://github.com/he8um/github-skills) and [githubnext/agentics](https://github.com/githubnext/agentics). Exact upstream revisions, local changes, and preserved licenses are recorded in [third-party notices](THIRD_PARTY_NOTICES.md) and the [source lock](third-party/sources.json).

## The skill library

| Skill | What it brings to the workflow |
| --- | --- |
| [Harness](skills/harness/SKILL.md) | A baseline for scope, clarification, ownership, verification, and delivery |
| [UI design direction](skills/ui-design-direction/SKILL.md) | Product-specific concepts, composition, responsive reconstruction, media, motion, and review |
| [React component practices](skills/react-component-practices/SKILL.md) | Clear state ownership, pure rendering, correct effects, identity, and async lifecycle |
| [Component API design](skills/component-api-design/SKILL.md) | Understandable props, valid states, composition, and consumer compatibility |
| [Design system consistency](skills/design-system-consistency/SKILL.md) | Existing tokens, components, variants, themes, and visual-regression discipline |
| [React accessibility](skills/react-accessibility/SKILL.md) | Semantic controls, form feedback, keyboard interaction, focus, and honest audits |
| [Vitest + React Testing Library](skills/vitest-react-testing/SKILL.md) | Behavior-focused scenarios, meaningful assertions, deterministic async work, and mock boundaries |
| [React UI performance](skills/react-ui-performance/SKILL.md) | Reproducible diagnosis, targeted changes, and comparable before-and-after evidence |
| [Git tooling](skills/git-tooling/SKILL.md) | Direct routine commands, protected user work, and explicit history-changing boundaries |
| [Trim mode](skills/trim-mode/SKILL.md) | Smaller complete implementations and concise replies when explicitly requested |

Each skill is self-contained. Its `SKILL.md` routes relevant work to local guides, and `references.json` makes those guides discoverable to tooling. Copy the whole folder; no companion skill is required.

The UI design skill includes twelve specialist guides, from [concept exploration](skills/ui-design-direction/guides/design-brief-and-exploration.md) and [scroll storytelling](skills/ui-design-direction/guides/scroll-storytelling.md) to [visual review](skills/ui-design-direction/guides/visual-review.md) and [usability walkthroughs](skills/ui-design-direction/guides/usability-walkthrough.md). Each other skill has three focused guides.

## Skill examples

Choose a scenario and copy its prompt into a session with the named skill installed. Replace illustrative paths and component names with your application. Every core skill includes two worked scenarios, linked below, with inputs, expected deliverables, and verification. The examples describe intended behavior, not evaluation results or checks already executed.

<details>
<summary><strong>Harness: preserve a draft after a failed save</strong></summary>

**Use case:** A local bug fix must preserve existing architecture and unrelated work.

```text
Use harness. Fix the profile editor so a rejected save keeps the entered
display name, shows the existing inline error, and allows retry. Preserve
successful saves and public props. Reuse the current request layer,
add a focused regression test, and report checks actually run. Do not push.
```

**Expect:** A scoped correction, retained input, regression evidence, and honest verification limits. [Full examples](skills/harness/examples.md).

</details>

<details>
<summary><strong>Git tooling: commit a fix without including unrelated work</strong></summary>

**Use case:** A reviewed component and test are ready, but another draft is still in progress.

```text
Use git-tooling. Commit only the named search component and regression
test with "Fix search clear behavior". Inspect pre-existing staged work,
preserve unrelated changes, and ask if the index cannot be separated
unambiguously. Report the commit and remaining state. Do not push.
```

**Expect:** Only the authorized files in the commit, with other work preserved. [Full examples](skills/git-tooling/examples.md).

</details>

<details>
<summary><strong>Trim mode: add an accessible search clear action</strong></summary>

**Use case:** A small interaction needs a complete fix without another dependency or state layer.

```text
Use trim-mode. Add a clear action to ProductSearch using the existing
button primitive. Clearing should restore all results and keep focus
in the input. Preserve accessible naming, verify the behavior, and
keep the implementation and response small.
```

**Expect:** Existing primitives, correct focus and results, retained safeguards, and a concise handoff. [Full examples](skills/trim-mode/examples.md).

</details>

<details>
<summary><strong>UI design direction: make inventory exceptions actionable</strong></summary>

**Use case:** A decorative opening pushes the actual work below the first viewport.

```text
Use ui-design-direction to redesign the inventory workspace around
low-stock exceptions and restock actions. Preserve the brand,
navigation, and component library. Define responsive behavior and
loading, empty, failure, and retry states. Implement the agreed scope
and inspect the rendered layout and main path where tools permit.
```

**Expect:** A product-specific hierarchy, usable states, and separate visual and task-completion evidence. [Full examples](skills/ui-design-direction/examples.md).

</details>

<details>
<summary><strong>React component practices: fix stale results and item identity</strong></summary>

**Use case:** Copied result state and index keys break search updates and reordering.

```text
Use react-component-practices to fix ProjectResults. Derive visible
items from the current projects and query without duplicated state,
use stable project IDs, and preserve the existing matching contract,
public props, and empty state. Verify query and ordering changes.
```

**Expect:** One clear state owner, current results, stable identity, and focused checks. [Full examples](skills/react-component-practices/examples.md).

</details>

<details>
<summary><strong>Vitest + React Testing Library: cover rejection and retry</strong></summary>

**Use case:** A save form needs behavior coverage that catches lost drafts.

```text
Use vitest-react-testing to test RenameForm. Edit the project name,
submit, reject the save, and assert the error and retained draft.
Retry successfully and verify the exact callback value. Use real
controls, accessible queries, awaited user-event, and controlled
promises. Keep production code unchanged.
```

**Expect:** Deterministic public-behavior tests, with executed results distinguished from generated files. [Full examples](skills/vitest-react-testing/examples.md).

</details>

<details>
<summary><strong>React accessibility: repair dialog keyboard behavior</strong></summary>

**Use case:** A dialog opens visually but leaves focus behind or loses it on closing.

```text
Use react-accessibility to repair the checkout delivery dialog with
the existing accessible primitive. Verify naming, initial focus,
containment, dismissal, restoration, and long-content visibility.
Preserve checkout behavior. Report browser and assistive-technology
checks that were run and those still unverified.
```

**Expect:** A usable real interaction, accurate semantics, and evidence appropriate to the claim. [Full examples](skills/react-accessibility/examples.md).

</details>

<details>
<summary><strong>Design system consistency: align a one-off settings action</strong></summary>

**Use case:** A screen bypasses the canonical control with a custom palette and spacing.

```text
Use design-system-consistency to align the settings save action with
ActionButton and active semantic tokens. Preserve submission, focus,
disabled, and error behavior. Check supported themes. Keep the change
local and do not alter shared defaults or add another button system.
```

**Expect:** Reuse of current components and tokens without a global visual migration. [Full examples](skills/design-system-consistency/examples.md).

</details>

<details>
<summary><strong>React UI performance: diagnose slow filtering with evidence</strong></summary>

**Use case:** A large inventory feels slow, and the bottleneck has not yet been established.

```text
Use react-ui-performance to investigate slow inventory filtering with
representative data. Record comparable runtime conditions and identify
the dominant cost before editing. Make the narrowest justified change,
preserve matching and selection, and repeat the measurement. Label any
unmeasured hypothesis; do not blanket-memoize the application.
```

**Expect:** A supported diagnosis and honest before-and-after evidence, with correctness preserved. [Full examples](skills/react-ui-performance/examples.md).

</details>

<details>
<summary><strong>Component API design: make field ownership explicit</strong></summary>

**Use case:** A shared field mixes controlled and uncontrolled behavior and loses valid empty strings.

```text
Use component-api-design to review TextField and its consumers. Define
valid controlled and uncontrolled modes, preserve controlled empty
strings, callback arguments, and native attributes. Ask about reset
behavior and compatibility before changing callers. Add only the API
surface needed by current use cases.
```

**Expect:** A clear ownership contract, explicit compatibility impact, and representative consumer checks. [Full examples](skills/component-api-design/examples.md).

</details>

## Agent role examples

These are role-based prompts for ordinary sessions using installed skills. These six UI specialist roles are examples, not bundled native profiles. The optional Agentic Workflows package supplies a separate, explicitly selected native agent. Naming a role does not create an independent execution context or change permissions.

| Role and use case | Copyable starting prompt | Expected handoff |
| --- | --- | --- |
| [UI architect](docs/agent-use-cases.md#ui-architect): plan a workspace before implementation | `Act as a UI architect. Use ui-design-direction and component-api-design to plan the inventory layout, responsive states, and public contracts. Preserve brand and current primitives; do not edit code.` | Concrete design and API decisions, reuse choices, and unresolved questions |
| [React builder](docs/agent-use-cases.md#react-builder): implement an approved slice | `Act as a React builder. Use harness, react-component-practices, and design-system-consistency to implement the approved inventory plan with recovery states. Run relevant checks and keep the diff scoped.` | Complete accepted behavior, changed files, actual checks, and limits |
| [Test engineer](docs/agent-use-cases.md#test-engineer): protect a save interaction | `Act as a test engineer. Use vitest-react-testing to cover pending save, rejection, retained draft, and retry with real controls and controlled promises. Do not change production code.` | Behavior tests, their protected contract, and observed execution results |
| [UI reviewer](docs/agent-use-cases.md#ui-reviewer): assess the rendered result | `Act as a UI reviewer. Use ui-design-direction and react-accessibility to inspect hierarchy, reading, keyboard behavior, focus, and recovery without editing. Separate evidence from assumptions.` | Ranked findings with location, impact, evidence, correction, and coverage limits |
| [Performance auditor](docs/agent-use-cases.md#performance-auditor): find the slow path | `Act as a performance auditor. Use react-ui-performance to reproduce the filter delay, distinguish browser and request costs, and recommend a measured correction. Keep the investigation read-only.` | Supported bottleneck, baseline, recommendation, tradeoffs, and validation plan |
| [Git operator](docs/agent-use-cases.md#git-operator): commit approved files safely | `Act as a Git operator. Use git-tooling to commit only the named fix and test with the agreed message, preserving unrelated staged and unstaged work. Do not push or rewrite history.` | Intended commit, preserved user work, and accurate repository state |

See [complete agent use cases](docs/agent-use-cases.md) for required inputs, detailed prompts, review boundaries, and a team handoff example. Use only the roles the task needs; a small fix does not need a team of agents.

## An operating model teams can review

| Principle | Expected behavior |
| --- | --- |
| Scope discipline | Make the smallest complete change. Preserve existing architecture and unrelated work. |
| Clear decisions | Investigate repository facts directly. Ask before implementing unresolved requirements. |
| Practical Git | Run straightforward authorized commands directly. Obtain exact approval for destructive actions and history rewriting. |
| Existing controls | Keep repository permissions, hooks, signing, review, and branch protection authoritative. |
| Accessible delivery | Preserve validation, error handling, security, and accessibility in every mode. |
| Honest evidence | Report what actually ran, what passed, and what remains unverified. |

**Output isolation is part of the standard.** Generated code must contain no AI attribution, authoring-tool references, or links back to this collection. Keep workflow metadata out of product code, comments, commits, and documentation. Preserve required legal notices and legitimate ownership records.

All content is in English. These are working instructions; enforcement and data handling remain the responsibility of the selected host, provider, repository controls, and organizational policies.

**[Read the operating model](docs/operating-model.md)**

## Evaluate before you roll out

Fifty cases cover normal work, ambiguity, scope, safeguards, activation, and multi-turn behavior. Local fixtures and explicit review criteria make the expected standard inspectable before adoption.

The evaluation tool prepares separate baseline and with-skill workspaces. Reviewers record observed evidence; new cases begin as `unverified`, and incomplete evidence cannot produce a passing result.

```sh
python3 scripts/evaluate.py validate
python3 scripts/evaluate.py list
python3 -m unittest discover -s tests -v
```

Evaluation tooling requires Python 3.9+ and Git; skill installation does not. The tool does not launch model sessions or make paid calls. Structural validation and tooling tests are separate from behavioral skill evaluation. Live-model benchmark results are not currently published.

**[Explore the evaluation suite](evals/README.md)**

## Bring it into your team

1. **Select a pilot.** Choose a repository, client, and representative tasks. Start with the skills that match the work.
2. **Review and distribute.** Pin a revision, preserve existing instructions, and use your normal change-control process.
3. **Evaluate and expand.** Compare actual outputs and evidence before adopting more skills or introducing specialist agents.

The collection fits into an existing development workflow. It does not add a hosted runtime or application dependency. Organizational permissions, data-handling requirements, and distribution terms still need your team's review.

**[Team adoption guide](docs/enterprise-adoption.md)**

<details>
<summary><strong>Skills, agent metadata, and specialist agents</strong></summary>

`agents/openai.yaml` provides skill UI metadata. It does not create or launch a specialist agent. The optional Agentic Workflows plugin supplies one native Copilot profile. The six UI role examples remain ordinary prompts; automatic delegation is not configured.

See [the agent guide](docs/agents.md) for role design, host-specific formats, permission boundaries, and evaluation considerations.

</details>

<details>
<summary><strong>Activate the optional trim mode</strong></summary>

Request `trim`, `be minimal`, `ponytail`, `lazy senior`, `be lazy`, or `ADHD mode` as a working style. Explicitly selecting `trim-mode` avoids confusion with another installed skill using the same trigger.

Trim mode checks necessity, reuse, platform support, and existing dependencies before adding minimal code. It keeps responses action-first and short, while preserving accepted requirements, validation, error handling, security, accessibility, and requested explanation depth.

Say `turn off trim mode` to return to normal output. [Activation details](docs/installation.md#activate-trim-mode).

</details>

## About the maintainer

Built by [Sagar Bhattacharya](https://github.com/sagarb3). This project presents an approach to frontend engineering centered on clear component contracts, accessible interactions, practical tooling, and reviewable evidence.

I’m interested in frontend engineering opportunities where thoughtful UI architecture and practical delivery matter. [Explore the HTML presentation](README.html#about-sagar) for the delivery approach and project evidence, or [visit my GitHub profile](https://github.com/sagarb3) to connect.

## Project origins

Read the [original project brief](docs/initial-prompt.md) and [reference notes](docs/reference-notes.md) for the collection's origins. The original ten skills and evaluation tooling were written for this repository. The two optional packages contain reviewed, adapted upstream material with preserved MIT notices; see [third-party notices](THIRD_PARTY_NOTICES.md).

The proposed backdated development timeline is an illustrative reconstruction, not a record of work performed on those dates. See the [history reconstruction record](docs/history-reconstruction.md) for the actual published commits, assigned timeline, and verification scope.

---

<p align="center">
  <strong>Design deliberately. Build consistently. Verify with evidence.</strong><br>
  <a href="docs/installation.md">Installation</a> &nbsp; / &nbsp;
  <a href="docs/operating-model.md">Operating model</a> &nbsp; / &nbsp;
  <a href="evals/README.md">Evaluations</a> &nbsp; / &nbsp;
  <a href="docs/enterprise-adoption.md">Team adoption</a>
</p>
