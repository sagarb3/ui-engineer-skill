# Assets and Large Interfaces

Read when the bottleneck involves loading, media, bundles, layout, large collections, or scrolling.

## Inspect What Is Actually Loaded

Use the production bundle or network evidence rather than estimating from import statements alone. Confirm that an import brings expensive code into the affected route before changing libraries or exports.

Use supported route or component splitting when it improves the real loading path. Preserve fallbacks, error recovery, and retry. Splitting everything can create its own request and coordination cost.

## Media and Layout Stability

Size images for their display role, reserve dimensions, and choose suitable responsive sources. Do not lazy-load the primary visible image mechanically when that delays essential content. Check font loading and fallback metrics if text movement is the observed problem.

Inspect forced layout, repeated measurement, expensive paint, and offscreen work when scrolling or animation stutters. Prefer suitable transformations, but verify the actual trace rather than assuming any transform is cheap. Large blurred surfaces and persistent layers can still be expensive.

Respect reduced motion and cleanup. Do not leave timers, observers, rendering loops, or preloaded assets active after the owning route is gone.

## Large Collections

Determine whether pagination, reduced returned data, or an existing collection primitive already fits the product. Virtualization can reduce mounted nodes but changes browser search, printing, scroll restoration, variable row measurement, and accessibility behavior.

Reuse the established implementation when possible. Preserve item identity, keyboard navigation, meaningful count and position information, and focus when items mount or unmount. Do not accept fewer DOM nodes as proof that the task remains usable.

Check representative and worst accepted data, not only a small demo. Avoid loading the entire remote dataset solely to filter it in the browser when the existing contract is server-side.

## Requests and Caches

Inspect accidental duplicate requests, sequential dependencies, and invalidation before adding another cache. Preserve the accepted freshness and consistency contract. Do not hide latency by indefinitely displaying stale records without an agreed product policy.

For optimistic actions, preserve rejection and rollback behavior. A smoother interface that loses user input or misreports persistence is not a successful optimization.

## Verification

- Bundle, network, media, or collection evidence identifies the relevant cost.
- Loading and layout changes preserve essential content and recovery.
- Large-data strategies retain keyboard, focus, identity, and accepted navigation behavior.
- Resources and caches have bounded lifetime.
- Measurements use comparable data and conditions.
