# React UI Performance Examples

These are hypothetical performance investigations. Workload sizes and goals must come from the actual task. The examples contain no measured improvement claim.

## Diagnose a Slow Inventory Filter

**Use case:** Typing becomes sluggish with a representative large inventory. The cause could be synchronous computation, state propagation, DOM size, or request behavior.

```text
Use react-ui-performance to investigate slow typing in the inventory
filter with the reported large dataset. Record the action, build mode,
data size, device conditions, and cache state. Identify the dominant
cost before editing. Make the narrowest justified change, preserve
matching and selection behavior, and repeat the same measurement.
Do not blanket-memoize components or change the data-freshness policy.
```

**Expected deliverable:** A reproducible baseline, evidence about the bottleneck, a targeted correction, and a comparable result. If measurement is unavailable, a hypothesis and its validation plan should be labeled accordingly.

**Review:** Inspect rapid input, clearing, selection, stale requests, and relevant error paths. A smaller render count is not enough if the interface becomes stale or data is mutated.

**Illustrative evidence fields:**

```text
Action and workload: state the reproduced interaction and data.
Environment: state build, device, cache, and network conditions.
Before and after: report only observed comparable values.
Correctness: name the checks actually run.
Limitations: identify unmeasured behavior and tradeoffs.
```

## Evaluate Virtualization Before Adding It

**Use case:** A data table mounts many rows, but keyboard navigation, browser search, printing, and scroll restoration matter to its users.

```text
Use react-ui-performance to assess the large order table. Compare the
existing pagination and data-loading approach with the installed
virtualization option. First establish whether mounted DOM cost is the
bottleneck. Preserve record identity, keyboard access, focus, and the
required search, printing, and restoration behavior. Recommend the
smallest suitable approach before introducing another table library.
```

**Expected deliverable:** A workload-based decision and explicit tradeoffs. A new dependency or fewer mounted nodes alone does not establish a better experience.

**Review:** Verify accepted navigation and accessibility behavior with representative data. Do not infer mobile frame rates or field performance from one desktop observation.
