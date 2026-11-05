# Scenario Design

Read when choosing test cases, queries, assertions, and regression coverage.

## Define Behavior Before Assertions

Identify the trigger, initial state, accepted outcome, and failure that would distinguish correct behavior from the bug. Name the behavior in ordinary product terms. Avoid test names that only repeat an internal method name.

Build a case matrix from independently meaningful rules. An edit form might need rejection retaining the draft, successful retry, and invalid input blocking save. Do not add arbitrary permutations or invent validation rules solely to increase test count.

For boundaries, choose values that distinguish the actual rule: empty input, a documented maximum, or a matching versus nonmatching record. Expected output should come from the contract, not the same algorithm used in production.

## Exercise the Public Interface

Render the real subject with the established helper and providers. Locate controls by role and accessible name, labels, or meaningful text. Scope repeated content with an appropriate region rather than fragile DOM position.

Use test IDs only when a semantic query cannot express the contract. A missing accessible name is a potential product defect, not a reason to query implementation classes. Do not add ARIA that changes real semantics merely to make a test convenient.

Create user-event per test and await interactions. Assert visible output, accessible state, navigation, or a documented public callback. Exact callback arguments are appropriate when they are the consumer contract; internal setter calls and render counts usually are not.

## Keep the Important Integration Real

Render actual UI primitives, including MUI controls when present. Preserve real validation and the relevant providers. Mock external services or collaborators at the existing project boundary rather than replacing every child component.

Portal content may appear outside the local render container. Query the document or a meaningful region instead of concluding that the dialog is absent. Do not mock the portal away merely to simplify a selector.

## Prove a Regression When Practical

Confirm the new case fails for the old behavior and passes with the fix when the environment permits. Use an isolated copy if reproducing the old state would otherwise disturb user work. Do not reset a shared checkout to create the failing phase.

A passing test alone does not prove it would catch the defect. State whether the failing phase was observed. Avoid broad snapshots that could pass while the affected interaction remains broken.

## Verification

- Cases correspond to accepted rules and meaningful failures.
- Queries and interactions represent the public user interface.
- Important validation and component integration remain real.
- Expected outputs are independent of the implementation algorithm.
- Regression claims match the phases actually observed.
