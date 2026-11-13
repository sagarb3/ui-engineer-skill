# Operating Model

The collection defines a shared way to approach React UI work. These are instructions interpreted by the host, supported by task-specific guides and evaluation criteria. They are not an authorization service or a substitute for repository controls.

## Small, Complete Changes

Follow existing naming, formatting, architecture, dependencies, and design conventions. Prefer the smallest change that fully satisfies the accepted outcome, including necessary callers, types, error paths, and tests.

Keep state ownership explicit, component contracts understandable, tests focused on behavior, and interfaces accessible. Measure before optimizing. Avoid speculative abstractions, unrelated cleanup, and unnecessary dependencies.

Inspect repository facts directly. Ask before implementing unclear requirements or selecting among unresolved product interpretations. A question does not prevent independent read-only work, but its dependent choice must remain pending.

## Git and Action Boundaries

Execute straightforward, authorized Git operations directly. Always ask before force pushes, hard resets, or deleting branches/files, and before other destructive operations or history rewriting. Exact prior approval for an action and target remains valid unless the actual consequences differ.

An edit request alone does not authorize pushing, publishing, sending messages, or paid operations. Skills do not expand permissions. Keep hooks, branch protection, identity, signing, and the host's approval mechanisms intact.

## Output Isolation

**Generated code must contain no AI attribution.** Downstream code, comments, commits, and documentation must not mention or link back to this skills repository, a parent agent, or the authoring tool. Do not add generated-by comments, promotional links, or workflow attribution trailers.

Keep newly written content in English. Preserve legitimate legal notices and unrelated ownership records. Keep installed instructions, prompts, tool logs, and review metadata out of product artifacts and application bundles.

Isolation is a behavior rule that requires review; it is not technically enforced by Markdown. Inspect the actual diff, including new files. Data handling remains governed by the selected host, provider, permissions, and organizational policies.

## Progressive Detail

Start with the relevant `SKILL.md` process. Read only the supporting guides triggered by the task. A local correction does not require running every workflow in a skill.

Every skill contains a `references.json` index with local guide titles, paths, and reading triggers. The index is a collection convention, not a universal client configuration. Copy complete skill folders so those paths remain valid.

The UI design skill has twelve guides covering direction, visual composition, reconstruction, media, image-led work, motion, scroll storytelling, interactive experiences, reviews, usability, evidence, and artifacts. Each other skill has three focused guides. None requires another installed skill.

## Verification and Honest Delivery

Use existing project checks and evidence suited to the changed behavior. A type check is not a browser review; a screenshot is not task completion; a successful local commit is not a successful push.

Report checks actually executed, their outcomes, and material limits. Do not invent performance gains, accessibility compliance, independent review, or live-model evaluation results.

The [evaluation suite](../evals/README.md) prepares isolated cases and summarizes reviewer judgments backed by evidence. New cases start unverified. Passing repository-tool tests does not establish that a skill performs reliably across models or clients.

## Optional Trim Behavior

Trim mode activates only on request. It checks necessity, existing code, platform support, installed dependencies, and readable direct code before introducing a custom solution. Replies become short, numbered, and action-first, ending with a concrete next step.

Requested explanation depth and necessary safeguards remain intact. Trim does not authorize cutting validation, error handling, security, accessibility, or accepted requirements.

## Agents and Metadata

`agents/openai.yaml` contains skill UI metadata. It does not create or launch a specialist agent. Native profiles, runtime permissions, and delegation are separate concerns described in [the agent guide](agents.md).
