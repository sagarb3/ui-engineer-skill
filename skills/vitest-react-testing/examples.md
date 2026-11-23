# Vitest and React Testing Library Examples

These prompts describe an application with the named test stack already installed. Replace paths and callback details with the real contract. Expected checks are not execution results.

## Preserve a Draft Through Rejection and Retry

**Use case:** A rename form accepts a promise-returning `onSave(name)` callback. A failed request should keep the edited name and allow retry.

```text
Use vitest-react-testing to test src/RenameForm.tsx. Enter a new project
name, submit, reject the save, and verify the inline error and retained
draft. Retry successfully and verify the exact callback value. Use the
existing render helper, real controls, accessible queries, and awaited
user-event interactions. Control promises rather than using sleeps.
Keep production code unchanged and report the focused command's result.
```

**Expected deliverable:** Tests through the form's public interface covering rejection, retained input, and retry. The subject and its validation should remain real; external request behavior may be controlled at the existing boundary.

**Review:** The tests should fail if rejection clears the draft or retry uses the old value. Check that asynchronous assertions wait for the relevant result and that no shared mock state leaks between tests.

## Verify a Real Debounce Contract

**Use case:** The product explicitly requires remote search after a documented debounce interval, and the current implementation has repeated-request regressions.

```text
Use vitest-react-testing to cover the existing debounce contract in
src/CustomerSearch.tsx. Reuse the documented interval and request mock.
Verify no premature request, one request for the settled query, and
cleanup when unmounted. Configure user-event with supported timer
advancement, restore real timers, and keep stale-result behavior real.
Do not change the interval or install another test runner.
```

**Expected deliverable:** Deterministic tests of the accepted timing behavior, not a wall-clock sleep or a test that mocks the debounce itself away.

**Review:** Inspect timer cleanup, awaited interactions, request arguments, and test isolation. A missing test environment should be reported as a prerequisite, not solved by silently downloading tools or claiming success.

## Scope Boundary

If a tests-only task reveals an application bug, report it rather than silently fixing production code. Simulated DOM coverage does not establish real layout, clipping, or screen-reader behavior.
