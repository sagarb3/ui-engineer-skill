---
name: react-ui-performance
description: Diagnose and improve measured React UI rendering, interaction, loading, or bundle problems with targeted changes and before-and-after evidence.
---

# React UI Performance

## When to Use

Use for reported slow interactions, unnecessary rendering, loading delays, excessive bundles, or requested performance reviews. Do not optimize routine code based only on appearance.

## Process

1. Define the slow user action, representative data, device conditions, and success measure. Ask before proceeding if the report or target is unclear. Reproduce the issue before changing code.
2. Measure the relevant path with available browser performance tools, React Profiler, network inspection, or the project's bundle analyzer. Distinguish scripting, rendering, layout, network, and asset costs. Account for development overhead; compare production builds where appropriate.
3. Fix the demonstrated bottleneck at its owner. Remove unnecessary effects or duplicate work, reduce state propagation, and avoid blocking event handlers. Use memoization only when repeated cost or identity matters and dependencies remain correct. Check existing compiler behavior before adding manual memoization.
4. For measured loading or scale issues, consider existing route-level code splitting, appropriately sized images, request deduplication, or list virtualization. Preserve keyboard access, findability, scroll behavior, error states, and layout stability. Add dependencies only with a demonstrated need and user approval if the choice is unclear.
5. Repeat the same measurement with comparable data and conditions. Report observed values, tradeoffs, and remaining uncertainty. Run relevant behavior tests and required project checks. If measurement tools are unavailable, label any proposed improvement as unverified.

Generated code must contain no AI attribution. Keep new content in English. Exclude skills-repository references, parent-agent mentions, authoring-tool names, and provenance links from downstream code, comments, commits, and documentation. Preserve existing legal notices.

## Define a Reproducible Baseline

Name the user action and the symptom before choosing an optimization: typing into a search field, opening a large menu, switching routes, scrolling a table, or loading a screen. "Too many renders" is an observation, not necessarily a user-visible problem.

Record the build mode, device or CPU conditions, dataset size, cache state, network conditions, and route. Use representative data, including the slow case the user reported. Clarify a missing performance goal rather than inventing an arbitrary score or response-time promise.

Repeat the same action enough to distinguish a consistent cost from startup noise. Compare cold loading with cold loading and warm interaction with warm interaction. Do not compare a development build before the change with a production build after it.

## Locate the Cost

| Evidence | Likely investigation | Avoid jumping to |
| --- | --- | --- |
| Input stalls during typing | Main-thread tasks, synchronous filtering, expensive updates | Memoizing every component |
| Large subtrees commit on a small state change | State placement, context propagation, prop identity | Replacing the whole state library |
| Scrolling stutters with many rows | DOM size, layout, paint, item measurement | Virtualization without checking accessibility |
| Navigation waits on sequential requests | Loader dependencies, cache use, request waterfall | A loading spinner as the only fix |
| Content shifts after loading | Image dimensions, font changes, reserved space | Hiding the movement with animation |
| Initial JavaScript is excessive | Actual bundle contents and route boundaries | Switching libraries without measurement |

Use browser traces to distinguish JavaScript work from layout, paint, asset loading, and network waits. Use React profiling to investigate component rendering, not to explain every browser cost. More renders can be cheaper than one expensive calculation.

Programmatic React profiling adds overhead and is disabled in ordinary production builds. Use the appropriate profiling-enabled build when measuring with that API, and disclose its conditions. React development checks can repeat work; do not remove those checks to claim a production improvement.

## Rendering and Computation

Start by removing unnecessary synchronization, duplicate work, and state owned too high in the tree. Keep unrelated transient state out of a frequently rendered shared provider. Split context responsibilities only when the actual update pattern justifies it.

Use `useMemo` for a demonstrated expensive calculation or an identity needed by a downstream optimization. It is not a semantic guarantee and must not be required for correctness. Use `useCallback` when a stable function identity has a real consumer; it does not make the callback's work faster.

Inspect compiler configuration and current behavior before layering manual memoization on top. Custom equality functions must compare every prop that affects output or behavior, including callbacks that close over state. A stale UI that renders less often is a regression.

Move avoidable work out of frequently invoked paths. For CPU-heavy work, consider a more efficient algorithm, precomputed lookup, smaller input, or existing worker mechanism only after identifying the cost. Do not introduce a worker merely because a function contains a loop.

## Responsiveness and Large Collections

Keep immediate input feedback responsive. If supported by the installed stack and required behavior, schedule nonurgent result updates separately from input updates. Deferring rendering is different from debouncing a network request: one does not automatically reduce the other.

Do not debounce every interaction. Decide whether the user should see immediate local results, delayed remote requests, explicit submission, or a retained previous result according to the product contract. Handle stale requests regardless of timing strategy.

For large collections, first check whether pagination or a smaller returned dataset already fits the workflow. Virtualization can reduce mounted content but complicates keyboard navigation, accessible relationships, variable row heights, browser search, printing, and scroll restoration. Reuse the project's proven implementation and verify these behaviors before accepting the tradeoff.

## Loading, Assets, and Layout

Inspect the production bundle rather than estimating from import statements alone. Confirm an import actually pulls expensive code into the affected route before changing it. Use supported route or component splitting where it improves real loading behavior; account for fallback, error, and retry states.

Size images appropriately, reserve their dimensions, and avoid loading below-the-fold media eagerly without need. Do not lazy-load the primary visible image mechanically when it delays important content. Check font loading and fallback metrics if text movement or delayed rendering is the measured problem.

For animation and scrolling, inspect forced layouts, repeated measurement, and expensive paint. Prefer transformations when they suit the effect, but verify the real trace. A compositor-friendly property does not guarantee a cheap effect when very large surfaces or other costs dominate. Honor reduced motion and stop unnecessary offscreen work.

Avoid solving remote latency with frontend memoization. Reuse the installed query cache, remove accidental duplicate requests, and inspect request dependencies. Do not change cache freshness or optimistic-update behavior without preserving the accepted consistency and error-recovery contract.

## Prove the Result

Repeat the original action under comparable conditions and report actual observations. Include the relevant metric, before and after values, and test conditions when measured. Label estimates and unverified hypotheses. A synthetic benchmark is evidence for that workload, not a guarantee about every user's device.

Check correctness under rapid input, repeated navigation, errors, cancellation, and unmounting where affected. Inspect memory and cleanup if the change adds caching, subscriptions, or observers. Run existing behavior tests and required project gates.

Stop when the accepted performance goal is supported by evidence or the next blocker is identified. Do not accumulate unrelated micro-optimizations after the bottleneck has been resolved. Do not add a telemetry service or permanent profiler instrumentation without a task-related requirement.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Assets and Large Interfaces](guides/assets-and-large-interfaces.md) | Read when the bottleneck involves loading, media, bundles, layout, large collections, or scrolling. |
| [Measurement and Diagnosis](guides/measurement-and-diagnosis.md) | Read before choosing a performance change or reporting improvement. |
| [Rendering and State](guides/rendering-and-state.md) | Read when profiling points to React updates, synchronous computation, context propagation, or repeated work. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Examples

See [worked use cases and copyable prompts](examples.md) for two application scenarios, expected deliverables, and verification. Paths and outcomes are illustrative; adapt them to the actual project and report only checks that ran.

## Anti-patterns / Red Flags

- Blanket `memo`, `useMemo`, or `useCallback` without evidence, or comparator logic that hides updates.
- Optimizing development-only double rendering or trading correctness for fewer renders.
- Arbitrary performance scores, incomparable benchmarks, and virtualization that breaks accessibility.

## Verification Criteria

- The bottleneck is demonstrated and the change improves the relevant measured behavior.
- Before-and-after conditions and tradeoffs are explicit; unmeasured claims are labeled.
- Correctness, accessibility, memory cleanup, and required checks remain intact.
- The diff addresses the measured cause and contains no attribution fingerprints.
