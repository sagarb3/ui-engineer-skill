---
name: vitest-react-testing
description: Write or repair behavior-focused React tests with Vitest and React Testing Library, covering user interactions, asynchronous states, and regressions without asserting implementation details.
---

# Vitest and React Testing Library

## When to Use

Use for React component tests in a Vitest and React Testing Library project, or when that stack is explicitly requested. Do not replace another test runner without approval.

## Process

1. Read the component contract, existing tests, setup, and installed APIs. Reuse project render helpers, providers, and DOM matchers. Ask before proceeding if expected behavior or the requested test scope is unclear.
2. Render through the public interface. Prefer `screen.getByRole` with an accessible name, or label queries for form controls. Use text when it is the actual contract and test IDs only when a semantic query cannot express it.
3. Create a `userEvent.setup()` instance per test and await interactions. Assert visible output, accessible state, navigation, or public callbacks with meaningful arguments. Exercise the real UI library and providers; mock network or external boundaries using existing tools.
4. Cover the requested success and failure paths, plus the regression trigger. Use `findBy` for content that appears asynchronously, `queryBy` for absence, and `waitFor` for retried assertions. Avoid arbitrary sleeps and side effects inside `waitFor`.
5. Restore changed mocks, timers, and global state. If fake timers are needed, configure user-event timer advancement and restore real timers. Run focused tests in non-watch mode, then required project gates. For a regression, confirm the test fails against the broken behavior when practical.

Generated code must contain no AI attribution. Write new content only in English. Keep skills-repository references, parent-agent mentions, authoring-tool names, and provenance text out of downstream code, test names, comments, commits, and documentation. Preserve existing legal notices.

## Establish the Test Contract

Read expected behavior before selecting assertions. Identify the trigger, initial state, observable outcome, and meaningful failure path. Name tests after the behavior: "keeps the draft when saving fails" describes a contract; "calls the handler" usually does not.

Inspect the installed Vitest version, React test environment, setup files, aliases, DOM matchers, cleanup policy, and existing render helper. Do not assume globals are enabled or that browser APIs exist in a simulated DOM. Reuse approved providers without replacing actual product validation or component behavior.

For an ordinary component test, import test functions explicitly if that is the project convention. For a regression, add the smallest case that distinguishes the broken behavior from the intended result. Keep expected outputs independent of the implementation's algorithm.

## Choose Queries by Meaning

| Need | Query | Reason |
| --- | --- | --- |
| A visible control with a name | `getByRole` with `name` | Checks the public accessible interface |
| A labeled form field | `getByLabelText` | Exercises the label association |
| Content expected after asynchronous work | `findByRole` or another `findBy` | Awaits appearance rather than assuming timing |
| Content expected to be absent | `queryByRole` or another `queryBy` | Allows a direct absence assertion |
| One control among repeated groups | `within(group)` | Expresses the intended region |
| A nonsemantic integration marker | A documented test ID | A fallback when a meaningful query is unavailable |

Avoid adding ARIA or test IDs solely to make an implementation-detail assertion convenient. If a role query reveals that a visible button has no accessible name, fix the actual labeling when the task authorizes application changes. Otherwise report the defect instead of mocking it away.

## Worked Interaction Test

The following assumes an existing `RenameForm` with a labeled name field, a Save button, and an `onSave` callback receiving the edited name. Adapt it to the real component contract; the file path is illustrative. DOM matchers must already be loaded by project setup.

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { expect, it, vi } from 'vitest';
import { RenameForm } from './RenameForm';

it('saves the edited project name', async () => {
  const user = userEvent.setup();
  const onSave = vi.fn();
  render(<RenameForm initialName="Draft" onSave={onSave} />);

  const nameField = screen.getByRole('textbox', { name: /project name/i });
  await user.clear(nameField);
  await user.type(nameField, 'Release plan');
  await user.click(screen.getByRole('button', { name: /^save$/i }));

  expect(onSave).toHaveBeenCalledTimes(1);
  expect(onSave).toHaveBeenCalledWith('Release plan');
});
```

The exact callback arguments are the public contract here, so checking them is appropriate. Checking internal setter calls, render counts, or which hook the form uses would couple the test to implementation.

## Cover States That Can Fail Differently

Choose cases from requirements rather than a mechanical test count. For a save form, distinct behaviors may include invalid input blocking submission, pending state preventing duplicate work, successful completion, and a rejected save retaining the draft for retry. Do not add unsupported business rules just to fill a matrix.

For asynchronous content, await the outcome visible to the user. Use `waitFor` for an assertion that must be retried, not to repeatedly click or mutate state. Use a controlled promise when the pending interval itself matters. Use timers only for a real timer-driven contract, such as debouncing; do not sleep to let the implementation "settle."

When a request race is relevant, control completion order and verify that an older response cannot overwrite a newer one. Test unmount cleanup when it guards observable behavior or external resources, without asserting private hook machinery.

## Mock Real Boundaries

Prefer the project's existing network mocking approach for requests. Keep the subject, its validation, and important UI primitives real. For MUI or another installed component library, render its actual controls with required providers. Remember that dialogs and menus may render through portals outside the local container; query the document or an appropriate accessible region.

Use deterministic data, time, and request results. Do not make live network calls or depend on the host timezone for a formatting contract. Keep expected values explicit and representative.

Vitest module mocks may be hoisted. Do not reference later initialized variables from a hoisted factory; use the installed version's supported pattern. Clear call history when history is the only shared state; restore spies when original implementations must return. Resetting a mock can also remove its implementation, so choose cleanup deliberately rather than calling every reset API.

If fake timers are required, pair user-event with the appropriate timer-advancement option, advance the intended interval, flush relevant pending work, and restore real timers. Do not disable user-event delays as a blanket workaround for timer hangs.

## Validation and Test Limits

Run the existing focused command in non-watch mode. For example, use the project's package-manager equivalent of `vitest run path/to/file.test.tsx`, without downloading a runner implicitly. Run required type and lint gates, since transpilation alone does not prove type correctness.

For a regression, prove the new assertion fails against the old behavior when practical in an isolated copy; do not reset a shared worktree or delete user changes to manufacture the red phase. Then confirm it passes with the fix. If only the passing state was observed, report that accurately.

Use a real browser for layout, clipping, pointer geometry, native platform integration, and assistive-technology behavior. Simulated focus assertions can support a test but cannot establish complete keyboard or screen-reader usability. Coverage percentages alone do not prove the acceptance criteria are tested.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Async and Mocks](guides/async-and-mocks.md) | Read when testing pending states, timers, requests, retry, cancellation, or stale results. |
| [Project Setup and Execution](guides/project-setup-and-execution.md) | Read before adding or running tests in an unfamiliar React project, or when a test fails before reaching its assertions. |
| [Scenario Design](guides/scenario-design.md) | Read when choosing test cases, queries, assertions, and regression coverage. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Examples

See [worked use cases and copyable prompts](examples.md) for two application scenarios, expected deliverables, and verification. Paths and outcomes are illustrative; adapt them to the actual project and report only checks that ran.

## Anti-patterns / Red Flags

- Testing hook call counts, internal state, CSS class names, or large snapshots instead of behavior.
- Mocking every child or UI control so the test cannot catch integration failures.
- Missing awaits, shared mutable fixtures, `.only`, and assertions that pass before work finishes.
- Treating a simulated DOM as proof of layout, focus geometry, or real-browser accessibility.

## Verification Criteria

- Tests fail for the relevant behavioral regression and pass for correct behavior.
- Queries and interactions reflect how users find and operate controls.
- Tests are isolated and await observable asynchronous outcomes.
- Real-browser-only checks are identified honestly; downstream output has no attribution fingerprints.
