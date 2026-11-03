# Rendering and State

Read when profiling points to React updates, synchronous computation, context propagation, or repeated work.

## Remove Unnecessary Work First

Inspect duplicated derived state and effects that calculate render data. Keep transient local state near its owner so unrelated regions do not update with every keystroke. Do not move everything into global state as a performance strategy.

Inspect context consumers and actual update frequency before splitting providers or replacing the state library. A smaller ownership correction may address the measured problem without an application-wide migration.

## Memoization Has a Consumer

Use memoization for a demonstrated expensive calculation or an identity needed by a downstream optimization. `useCallback` does not make the callback's work cheaper. `useMemo` is not a correctness guarantee or a required cache for business semantics.

Check compiler configuration and existing optimization before adding manual layers. Custom comparisons must account for every prop that affects output or behavior, including callbacks that close over state. A stale UI that renders less often is a regression.

Do not add blanket memoization to all components or stabilize every object mechanically. Measure whether the change removes relevant work and whether its complexity is justified.

## Keep Input Responsive

Separate immediate input feedback from nonurgent rendering where the supported stack and product behavior allow it. Deferring a rendered result is different from debouncing a network request; one does not automatically reduce the other.

Choose timing from the accepted interaction. Local filtering may need immediate feedback; remote search may use the project's existing request policy. Preserve cancellation, stale-result protection, and understandable pending behavior regardless of scheduling.

## Improve the Actual Calculation

When computation is the bottleneck, consider less repeated work, a suitable data structure, a smaller input, or an existing worker seam. Do not add a worker merely because a function contains a loop. Account for serialization, startup, cancellation, and cleanup if a worker is necessary.

Keep caches bounded and tied to the correct data identity. An ever-growing cache or memo key based on unstable objects can create a new performance problem while appearing to reduce renders.

## Verification

- The optimized updates were identified by measurement.
- Ownership and derivation remain correct.
- Memoization has a demonstrated cost or identity consumer.
- Rapid input, prop changes, errors, and cancellation still behave correctly.
- Added caches or subscriptions have bounded lifetime and memory behavior.
