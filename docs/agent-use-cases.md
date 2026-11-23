# Agent Role Use Cases

These six roles describe useful ways to organize work with the installed skills. Native specialist agent profiles and automatic delegation are not implemented in this repository. The role prompts below can be used in an ordinary session; they do not require a nonexistent custom-agent command.

Install the named skills first, replace illustrative paths with real application paths, and supply the accepted requirements. Expected handoffs are acceptance criteria rather than recorded outputs. A role prompt does not change host permissions or create an independent reviewer.

## UI Architect

**Use case:** A team needs a coherent plan for an inventory workspace before implementation begins.

**Provide:** The main user task, current route, brand rules, component library, representative data, supported viewports, and constraints that must remain intact.

```text
Act as a UI architect for this task. Use ui-design-direction and
component-api-design to plan the inventory workspace. Prioritize
low-stock exceptions and the restock action. Preserve the current
brand, navigation, and component library. Define the main layout,
responsive changes, important states, and necessary component contracts.
Ask about unresolved workflow choices. Deliver the design and API
handoff only; do not edit application code.
```

**Expected handoff:** A concrete hierarchy, state and responsive plan, current-component reuse decisions, public contracts that actually need change, and unresolved decisions. The plan should identify the main action and result without adding speculative features.

**Review boundary:** A proposed design is not a rendered implementation or a tested user flow. The architect should not claim either occurred.

## React Builder

**Use case:** The design and behavior are accepted, and the team needs a focused implementation in the existing application.

**Provide:** The approved design and state contract, target files, current components, accepted API changes, and project checks.

```text
Act as a React builder. Use harness, react-component-practices, and
design-system-consistency to implement the approved inventory plan.
Reuse current primitives and the existing data layer. Keep state
ownership clear and preserve record identity. Include the agreed
loading, empty, failure, and retry behavior. Keep the diff scoped,
run relevant installed checks, and report any unmet acceptance item.
Do not add dependencies or push changes without authorization.
```

**Expected handoff:** The complete accepted slice, affected files, behavior changed, checks actually executed, and remaining limits. A default-state screenshot alone is not complete delivery.

**Review boundary:** The builder may self-check, but cannot label that self-check as an independent review.

## Test Engineer

**Use case:** A save interaction needs regression coverage for pending work, rejected requests, retained input, and retry.

**Provide:** Actual component code, accepted callback and validation contracts, installed test setup, and approved render helpers.

```text
Act as a test engineer. Use vitest-react-testing to cover the rename
form's pending, rejected-save, retained-draft, and successful-retry
behavior. Keep the subject and controls real, use accessible queries,
await user interactions, and control promise completion. Reuse project
providers and mocks. Do not change production code. Report a discovered
product defect and distinguish generated tests from executed results.
```

**Expected handoff:** Focused behavior tests, the relevant contract they protect, commands and outcomes, and any blocker. A mock that supplies the desired validation result is not sufficient coverage.

**Review boundary:** No runner installation, invented passing result, or assertion weakening to hide a product bug.

## UI Reviewer

**Use case:** A completed screen needs visual and accessibility findings before a team accepts it.

**Provide:** The current page or captures, viewport and data state, relevant design constraints, and the permitted read-only interaction scope.

```text
Act as a UI reviewer. Use ui-design-direction and react-accessibility
to review the current inventory screen without editing files. Assess
hierarchy, actual-size readability, action discoverability, responsive
layout, keyboard use, focus, and failure feedback. Separate visual
findings from task-completion observations. Rank concrete issues with
location, evidence, impact, and a correction. Label missing evidence
and do not claim independent review if you participated in the build.
```

**Expected handoff:** Actionable evidence-based findings and explicit coverage limits. When a separate reviewer is authorized and actually used, the report can identify that independence.

**Review boundary:** A screenshot cannot prove keyboard, motion, or persistence behavior. No editing or live consequential action is authorized by the review alone.

## Performance Auditor

**Use case:** A representative large inventory causes slow typing, but the owner needs a diagnosis before approving an optimization.

**Provide:** The slow path, reproduction data, runtime conditions, available measurement tools, and the accepted performance target.

```text
Act as a performance auditor. Use react-ui-performance to diagnose the
reported inventory-filter delay. Reproduce the action, record build,
data, device, cache, and network conditions, then distinguish rendering,
computation, layout, and request costs. Recommend the narrowest measured
fix and its correctness checks. Keep this investigation read-only.
Label unmeasured hypotheses; do not invent gains or add telemetry.
```

**Expected handoff:** A supported bottleneck, comparable baseline evidence, a specific recommendation, tradeoffs, and a measurement plan for an authorized change.

**Review boundary:** Fewer renders or a synthetic trace alone does not establish a measured user improvement.

## Git Operator

**Use case:** A reviewed fix is ready to commit, while the checkout also contains unrelated work.

**Provide:** Exact target paths, the desired message, relevant check results, and whether a push is authorized.

```text
Act as a Git operator. Use git-tooling to commit only the named search
component and regression test with "Fix search clear behavior".
Inspect pre-existing staged content, preserve unrelated changes, and
stop if separating the work requires a user decision. Report the
resulting commit and remaining worktree state. Do not push, amend,
rebase, reset, delete, or force push as part of this request.
```

**Expected handoff:** An actual commit containing the intended change, unchanged unrelated work, and a truthful result. A conflict in the index should prompt a concrete question rather than a silent staging decision.

**Review boundary:** A code-review approval is not automatically permission to rewrite or publish history.

## Example Team Handoff

For an approved inventory feature, the architect supplies the contract, the builder implements it, the test engineer verifies behavior, the reviewer checks the rendered result, and the Git operator handles the authorized commit. Use a performance investigation only when there is a relevant measured concern.

Do not launch every role for a small task. Share the task, accepted constraints, relevant files, observed checks, and remaining limits. Avoid concurrent writers on the same files. Later automatic delegation would need native host configuration and separate routing and permission validation; these examples do not implement it.
