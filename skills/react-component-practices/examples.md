# React Component Practices Examples

These scenarios describe consuming applications. Paths and APIs are illustrative; inspect real callers and installed versions before editing. Expected results are not recorded test outcomes.

## Keep Search Results Current

**Use case:** A result list copies filtered records into state, omits the query from its effect dependencies, and uses array indices as keys. Changing the query or reordering records produces stale or mismatched content.

```text
Use react-component-practices to fix src/ProjectResults.tsx. Results
must follow the current projects and query without duplicated derived
state. Preserve the existing case-sensitive substring rule. Projects
can reorder, so preserve identity by project ID. Keep public props and
empty-state behavior compatible, and verify query and order changes.
```

**Expected deliverable:** A clear source of truth, current derived output, stable item identity, and focused behavior checks. Blanket memoization, a new store, or a changed matching rule are outside the request.

**Review:** Change the query without replacing the project array, reorder matching projects, and supply no matches. Verify the visible results and any per-item state remain attached to the correct IDs.

## Prevent Stale Request Completion

**Use case:** A customer detail component requests data when selection changes. A slow old request can overwrite a faster new selection.

```text
Use react-component-practices to fix src/CustomerDetails.tsx. The latest
selected customer must remain authoritative when requests finish out of
order. Reuse the current loader or query mechanism. Preserve error and
retry behavior, handle unmounting, and cover A-starts, B-starts,
B-finishes, A-finishes. Do not migrate the request library.
```

**Expected deliverable:** A narrow correction using compatible cancellation or stale-result protection. A cancellation must not hide actual request failures, and cleanup must release owned resources.

**Review:** Control completion order, reject a current request, retry, and navigate away while work is pending. Report executed checks and any missing browser or toolchain evidence separately.

## Useful Combinations

Use `harness` to retain scope and `vitest-react-testing` for deterministic interaction tests. A performance change is a separate concern unless measurement shows the current behavior is also slow.
