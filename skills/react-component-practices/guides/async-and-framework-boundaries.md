# Async and Framework Boundaries

Read for requests, races, unmounting, hydration, and server/client integration.

## Reuse the Existing Data Lifecycle

Inspect the framework loader or query layer before adding a fetching effect. Reuse its cache, error, retry, invalidation, and cancellation conventions. Do not create a second cache in component state or change cache freshness to hide an unrelated stale-data bug.

Clarify whether old content remains visible during refresh, whether an error replaces the whole region, and whether retry preserves user input. These are product behaviors rather than universal React defaults.

## Protect Against Stale Completion

Define which request owns the result. If A starts before B but finishes after it, an obsolete A result must not replace B when B represents the current input. Use the existing query mechanism, compatible cancellation, or an explicit active/request-identity guard.

Cancellation does not make every rejection harmless. Distinguish an expected cancellation from a real failure and preserve the error feedback required by the product. Release owned resources when the component unmounts or its request-defining inputs change.

For mutations, establish duplicate-submission and retry behavior. A disabled button alone may not protect an operation from other callers. If the backend supplies idempotency or authoritative read-back, use that contract rather than guessing that a repeated request is safe.

## Respect Rendering Boundaries

Read installed versions and framework conventions. Do not move browser APIs, mutable global state, or user-specific data into server rendering. Keep server-only secrets and authorization on the server.

Use the narrowest existing client boundary that supports the interaction. Do not mark an entire application as client-rendered merely because one control needs state. Values crossing a framework boundary must satisfy that framework's actual serialization and ownership rules.

## Hydration and Initial State

The initial server and client output must agree under the framework's supported model. Current time, randomness, storage, viewport measurements, or browser-only preferences can make initial output differ. Use the established initialization strategy instead of suppressing hydration warnings indiscriminately.

Do not render sensitive or unauthorized content briefly and then hide it in an effect. Initial authorization belongs at the appropriate boundary, not in a later visual correction.

## Errors and Recovery

Rendering failures, event-handler failures, and rejected asynchronous work have different owners. An error boundary does not catch every event or request rejection. Handle errors where they occur and use the existing boundary for the failures it actually supports.

Verify failure feedback, retained input, retry, cancellation, and navigation away. Check the sequence that exposed the bug rather than only the first successful mount.

## Verification

- Existing loaders and query conventions remain authoritative.
- Stale, cancelled, and unmounted work cannot corrupt the current result.
- Duplicate mutation and retry behavior follow the real backend contract.
- Server/client boundaries and hydration remain correct.
- Failure and recovery are observable and honestly tested.
