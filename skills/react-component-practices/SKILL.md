---
name: react-component-practices
description: Implement or repair React components with clear state ownership, pure rendering, correct effects, stable identity, and existing project conventions.
---

# React Component Practices

## When to Use

Use when implementing or changing React component behavior, hooks, state, or rendering. Follow the installed React version and framework boundaries.

## Process

1. Read the component, callers, nearby tests, and installed versions. Identify the source of truth and requested behavior. Ask before proceeding if requirements or ownership are unclear.
2. Keep rendering pure. Derive values during render when possible; put user-triggered work in event handlers. Use effects for synchronization with external systems, with complete dependencies and cleanup. Cancel or ignore stale asynchronous results.
3. Keep state local until multiple consumers need it. Avoid duplicate derived state and prop-to-state synchronization. Update state immutably; use functional updates when the next value depends on the previous one. Call hooks unconditionally at component or custom-hook top level.
4. Use stable data keys for changing lists. Extract a component or hook when it gives a real ownership or reuse boundary. Preserve semantic HTML, loading and error states, and the project's TypeScript and formatting conventions.
5. Verify observable behavior, including repeated interaction, prop changes, unmounting, and relevant failure paths. Run focused tests, type checks, and lint checks using existing project commands.

Generated code must contain no AI attribution. Keep newly written content in English. Do not include skills-repository links, parent-agent references, authoring-tool names, or provenance text in downstream code, comments, commits, or documentation. Preserve existing legal notices.

## Assign State to Its Owner

Before adding state, classify the value:

| Value | Usual owner | Avoid |
| --- | --- | --- |
| Open disclosure, draft field, temporary selection | The nearest component that needs it | A global store for a local interaction |
| Shared sibling state | Their nearest useful common owner | Two independent copies kept in sync |
| Shareable filters or pagination | Existing router or URL-state mechanism | A URL and local state disagreeing |
| Remote records and request status | Existing data-fetching layer or framework loader | Copying cached data into another cache |
| A value computable from current inputs | Render-time calculation | State plus an effect to update it |
| Mutable integration handle that does not render | A ref with explicit lifecycle | Ref writes that secretly control visible output |

These are ownership choices, not a mandate to introduce every layer. Reuse the architecture already present. If the product needs a different persistence or sharing contract, clarify it first.

For example, given a confirmed case-sensitive filter contract, derive visible records directly:

```tsx
type Project = { id: string; name: string };

function ProjectResults({ projects, query }: {
  projects: Project[];
  query: string;
}) {
  const visibleProjects = projects.filter((project) =>
    project.name.includes(query),
  );

  if (visibleProjects.length === 0) {
    return <p>No matching projects.</p>;
  }

  return (
    <ul>
      {visibleProjects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  );
}
```

Do not add `useEffect` and a second list state to implement that derivation. If filtering is measurably expensive, consider optimization after profiling. If the installed project has a different search contract, preserve it.

## Rendering and Update Rules

Rendering must not mutate props, alter shared objects, start requests, write storage, or subscribe to events. Keep state updates tied to a defined event or synchronization lifecycle. Use a functional update when the new state depends on the previous value:

```tsx
setSelectedIds((currentIds) =>
  currentIds.includes(id)
    ? currentIds.filter((selectedId) => selectedId !== id)
    : [...currentIds, id],
);
```

Do not mutate the previous array and then return it. Avoid separate booleans that permit impossible request states when an explicit status or existing request abstraction already models the transition.

Keep hook calls at supported top-level positions; do not put ordinary hooks inside conditions, loops, or event handlers. Do not suppress hook dependency warnings to force a desired schedule. Development checks may repeat setup and cleanup; make those operations safe rather than adding a flag that hides a missing cleanup.

## Effect and Asynchronous Work Review

For every effect, identify the external system, the values that define its connection, and the cleanup that reverses setup. Event listeners, subscriptions, timers, observers, and imperative widgets need a bounded lifetime. Avoid effects that merely notify a parent about a value that could be passed in the originating event.

Use the project's loader or query mechanism before writing raw fetching effects. When direct asynchronous work is appropriate, handle pending and rejected states, prevent obsolete requests from replacing newer results, and release resources on cleanup. An abort signal can cancel compatible work; other work may need an active flag or request identifier. Do not swallow actual failures as though they were cancellations.

Check these sequences when they are relevant: request A starts, request B starts, B finishes first, A finishes last; the component unmounts while pending; the user retries after an error. The latest valid result should remain authoritative. Decide whether old content stays visible while refreshing according to the accepted product behavior.

## Identity, Composition, and Boundaries

Keys express identity across renders. Use record IDs for lists that reorder, filter, or accept insertion. Do not generate keys during rendering or use array indices where item identity can change. Define component functions at a stable module level when their identity must survive parent updates.

Extract components around coherent visual or interaction responsibility. Extract hooks for reusable stateful behavior or a useful lifecycle boundary, not to hide a few lines of straightforward state. Preserve the project's file conventions and avoid a fixed component-size rule.

Respect framework server/client boundaries. Do not move browser-only APIs into server rendering, send nonserializable values across a boundary, or add a broad client directive to solve one small interactive region. During hydration, avoid nondeterministic initial output from current time, random values, or browser storage without the framework's supported pattern.

## Forms and Failure Behavior

Use controlled fields consistently when the parent owns their values; use defaults only for initial uncontrolled values. Preserve labels, descriptions, and native form behavior. Choose button types explicitly when a control is inside a form.

Do not inject untrusted HTML. Client-side validation improves feedback but does not replace server validation or authorization. Use an existing error boundary for rendering failures where appropriate; handle event-handler and request errors in the relevant action path because a render boundary does not catch every kind of failure.

Verify prop updates, repeated interaction, reset behavior, failures, and identity preservation where they are part of the change. A component that works on first mount but becomes stale after its inputs change is incomplete.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Async and Framework Boundaries](guides/async-and-framework-boundaries.md) | Read for requests, races, unmounting, hydration, and server/client integration. |
| [Composition and Identity](guides/composition-and-identity.md) | Read when extracting components, moving state, changing lists, introducing hooks, or adapting public props. |
| [State and Effects](guides/state-and-effects.md) | Read when deciding whether a value needs state, where it belongs, or whether synchronization requires an effect. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Anti-patterns / Red Flags

- Effects that calculate render data, suppressed dependency warnings, and state updates during render.
- Unstable keys, state mutation, stale closures, and asynchronous updates racing newer requests.
- Global state for local interactions, premature memoization, or framework changes outside the request.
- Raw HTML injection with untrusted content or inaccessible clickable containers.

## Verification Criteria

- State has one clear owner; rendering and hooks follow React's rules.
- Effects clean up and asynchronous work cannot overwrite newer results.
- User-visible behavior and relevant error paths pass focused checks without new warnings.
- The diff matches local conventions and contains no attribution fingerprints.
