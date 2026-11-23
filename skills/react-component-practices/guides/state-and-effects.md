# State and Effects

Read when deciding whether a value needs state, where it belongs, or whether synchronization requires an effect.

## Establish a Single Owner

Classify each value as local interaction state, shared client state, URL state, server state, derived render data, or a mutable integration handle. Use the project's existing owner for that class. A value should not become a second source of truth merely because it is convenient to access locally.

Derived values normally belong in rendering. Filtering records, calculating a total, or selecting a display label from current inputs does not require an effect that writes another state variable. Such duplication introduces a stale intermediate render and another reset rule.

When a draft intentionally differs from saved data, model that distinction explicitly. Identify initialization, editing, save, cancellation, and reset behavior. Do not blindly copy every incoming prop update into a draft and erase unsaved work.

## Update From Current State

Use immutable updates. When the next value depends on the previous value, use the supported functional update form so queued events do not read an obsolete closure. Do not mutate a collection and then return the same reference.

Prefer a coherent status model when several booleans represent one exclusive state. Keep independent flags independent only when their combinations are meaningful. Do not introduce a reducer merely because a component has several fields; use it when transitions need an explicit shared owner.

## Identify the External System

For every effect, name the resource or system being synchronized: a subscription, timer, DOM integration, connection, observer, or supported external state. If no external system exists, consider a render calculation or event handler instead.

Include reactive dependencies according to the installed React rules. Do not suppress the lint warning or hide a value in a ref merely to prevent the effect from running. Restructure ownership when the dependency relationship exposes a real design problem.

Setup and cleanup should form a coherent pair. Remove the same listener, cancel the owned timer, unsubscribe, disconnect the observer, or release the widget. Development remount checks should expose missing cleanup rather than be bypassed with an initialized flag.

## Events Versus Synchronization

Work caused by a user action generally belongs in that event's path. Submitting a form, reporting an intentional selection, or invoking a save should not depend on observing a later state change unless the architecture requires it.

Do not use an effect to send a callback for a value that can be sent directly from the originating event. Conversely, synchronization with an external source may need a lifecycle that is independent of any single click.

## Verification

- Each visible value has a clear source of truth.
- Derived data updates immediately with its inputs.
- Draft resets and prop changes preserve the accepted ownership contract.
- Effects have an external purpose, complete dependencies, and correct cleanup.
- Repeated interaction and remount behavior do not duplicate work.
