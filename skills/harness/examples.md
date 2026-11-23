# Harness Examples

These are illustrative application scenarios, not results from this repository. Replace paths with real application files before use. Expected results describe acceptance criteria, not checks already executed.

## Preserve a Draft After a Failed Save

**Use case:** An established profile editor clears entered values when a request is rejected. The team wants a local correction using existing architecture.

**Provide:** The editor, its save callback or service, neighboring tests, and the accepted retry behavior.

```text
Use harness. In src/ProfileEditor.tsx, a rejected save clears the entered
display name. Keep the draft after failure, show the existing inline error,
and allow retry. Preserve the successful-save behavior and public props.
Reuse the current request layer. Add a focused regression test and run the
relevant installed checks. Do not push or change unrelated files.
```

**Expected deliverable:** A correction at the state owner, a regression covering rejection and retry, and a report of checks actually run. The change should not introduce another store, request abstraction, or form library.

**Review:** Enter a new value, reject the first save, verify the value remains, then retry successfully. Confirm other consumers and successful submission still follow the existing contract. If the environment cannot execute a check, the delivery should name that limit.

## Clarify Persistence Before Adding Storage

**Use case:** A product request says filters should be remembered without specifying whether that means within the route, across refreshes, or across devices.

```text
Use harness. The request is to make the order table remember its filters,
but persistence scope and reset behavior have not been decided. Inspect
the existing table and router, identify what the repository already
answers, and ask the remaining product question before implementing.
```

**Expected response shape:** A focused question distinguishing the unresolved persistence choices, supported by relevant repository facts. The response should not ask the user to locate an obvious router configuration or quietly choose local storage.

**Review:** No dependent persistence behavior should be implemented while the requirement is unresolved. Independent read-only investigation can continue. A short question is a successful outcome for this scenario.

## Useful Combinations

Pair with `react-component-practices` for state ownership or `vitest-react-testing` for the regression. Harness remains the scope and delivery baseline; combining skills does not grant extra permission to publish, push, or rewrite history.
