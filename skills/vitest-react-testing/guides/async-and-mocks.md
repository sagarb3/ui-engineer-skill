# Async and Mocks

Read when testing pending states, timers, requests, retry, cancellation, or stale results.

## Await an Observable Condition

Use a `findBy` query for content expected to appear asynchronously. Use `queryBy` for absence and `waitFor` when an assertion needs retrying. Keep side effects out of `waitFor`; repeated clicks or state changes inside it can create the behavior being asserted.

Do not use arbitrary sleeps to let the component settle. A test should synchronize with the actual contract: enabled control, visible status, callback, or resulting data.

## Control Completion Order

Use a controlled promise when the pending interval matters. Assert the pending behavior before settling it, then verify success or failure. For race conditions, start requests in the relevant order and complete them in the opposite order to expose stale replacement.

Do not treat every late response as an error or every rejection as cancellation. Match the implementation's external contract. Verify that rejected saves preserve the draft and that retry behaves as requested, rather than only checking a callback was invoked.

## Mock at the Boundary

Reuse the project's request mocking or typed service seam. Avoid live network calls and uncontrolled host time. Do not replace the subject's validation, state ownership, or component primitives with mocks that guarantee the expected result.

Module mock factories may be hoisted. Follow the installed Vitest version's supported pattern and do not access later initialized variables from a hoisted factory. Preserve actual types instead of suppressing errors or casting every mock to an unrestricted type.

Choose cleanup intentionally. Clearing call history preserves implementation; resetting can remove configured behavior; restoring spies returns original implementations. Do not call every cleanup API indiscriminately and hide the lifecycle you depend on.

## Timers and Global State

Use fake timers only for a real timing contract. Configure user-event's timer advancement appropriately, advance the relevant interval, settle pending work, and restore real timers. Disabling delays as a general workaround can bypass the behavior under test.

Restore changed globals, system time, environment, request handlers, and spies according to project setup. Keep data isolated between cases. Avoid test ordering dependencies or a shared mutable fixture that preserves state accidentally.

## Verification

- Async assertions wait on the intended observable result.
- Pending, rejection, retry, and race cases control the relevant timing.
- Mocks preserve important product logic and actual collaborator types.
- Timers and global state return to the project's expected baseline.
- Tests pass independently rather than only in a particular suite order.
