# Trim Mode Examples

These are illustrative working-style requests. File paths refer to the consuming application. Examples show expected behavior rather than recorded execution.

## Add a Local Clear Action

**Use case:** An existing search input needs a clear action. The application already has an accessible button primitive and all results derive from the current query.

```text
Use trim-mode. Add a clear action to src/components/ProductSearch.tsx
using the existing button primitive. Clearing the query should restore
all results and keep focus in the search field. Add no dependency or
new state layer. Keep the control named for assistive technology and
verify the affected behavior.
```

**Expected deliverable:** The smallest complete implementation, with a clear accessible name and correct focus. The agent should reuse the existing query owner instead of introducing synchronized result state.

**Review:** Search, clear, and repeat with keyboard input. Check that an empty query returns the agreed full set and that labels and focus remain correct. Verification and error handling are not optional because the prompt requests brevity.

**Illustrative completion format:**

```text
1. State the changed behavior.
2. Name the checks actually run and any material limit.
3. Next: give one concrete review or use step.
```

This template contains no claim that checks passed.

## Keep Depth When an Explanation Is Requested

**Use case:** A reviewer wants a small patch but still needs to understand an asynchronous edge case.

```text
Use trim-mode for the implementation. Fix the stale-response bug in
src/CustomerLookup.tsx without changing its public API. Explain how the
fix behaves when request B finishes before request A, and describe the
cleanup and failure paths in enough detail for review.
```

**Expected deliverable:** A bounded correction and an adequate explanation. Short presentation must not remove the race analysis, failure behavior, cleanup, or necessary checks.

**Review:** Confirm the implementation handles the requested sequence, not just first mount. Turn the mode off with `turn off trim mode` when normal presentation is desired. Quoting those words in documentation alone must not activate or stop it.
