# Measurement and Diagnosis

Read before choosing a performance change or reporting improvement.

## Define the Slow Path

Name the user action, observed symptom, representative data, device conditions, build mode, and accepted goal. Clarify an unspecified target rather than inventing a score. "Many renders" is not itself proof of a user-visible delay.

Reproduce the problem before editing. Compare cold loading with cold loading and warm interaction with warm interaction. Keep cache, network, data size, and runtime conditions comparable. Repeated observations help distinguish consistent cost from startup noise.

## Identify the Dominant Cost

Use browser evidence to distinguish scripting, layout, paint, asset loading, and network. Use React profiling to inspect component work, not every cost in the browser. A slow request will not become faster because a callback was memoized.

Check state propagation, synchronous computations, request waterfalls, DOM size, asset dimensions, and repeated layout measurements according to the trace. Follow the evidence rather than optimizing the code that looks longest.

Development checks and tooling overhead can change the observed workload. Compare appropriate production conditions when possible. Programmatic React profiling requires a suitable profiling-enabled build; do not describe an ordinary production build as though that instrumentation were active.

## Make a Discriminating Change

Change the responsible cause narrowly enough that the next measurement can explain the result. Avoid combining a new state library, new table engine, and new asset pipeline in one optimization unless the accepted architecture change actually requires them.

Preserve correctness and the existing product contract. Reducing freshness, removing validation, hiding content, or allowing stale closures is not a valid performance improvement unless an explicit requirement changes the contract.

## Report Evidence Honestly

Repeat the original workload under comparable conditions. Report relevant observed values, variability where meaningful, and important tradeoffs. Label estimates and unverified hypotheses. Do not invent frame rates or percent improvements.

A synthetic benchmark supports its own workload, not every device or user. A lab improvement does not automatically establish field improvement. Do not add telemetry or an external service without a task-related requirement and authorization.

## Verification

- The slow action is reproduced under known conditions.
- The suspected cost is supported by appropriate evidence.
- The change addresses that cost while preserving the accepted behavior.
- Before-and-after comparisons are comparable.
- Unavailable measurement and remaining uncertainty are explicit.
