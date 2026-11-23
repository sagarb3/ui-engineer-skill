# Compatibility and Consumer Tests

Read before changing defaults, renaming props, moving exports, altering callback shapes, or adding a migration adapter.

## Locate Actual Consumers

Inspect direct imports, re-exports, examples, tests, adapters, and relevant JavaScript call sites. A successful TypeScript check does not prove all runtime consumers remain compatible.

Determine whether the requested work changes implementation or public behavior. An internal rendering repair should not rename props. A new capability should not force existing callers to configure it unless that change is accepted.

## Identify the Breaking Surface

Changes to defaults, callback timing, event arguments, focus, reset behavior, native attribute forwarding, and accessible semantics can break consumers even when the signature compiles.

Make the impact concrete and ask when acceptable compatibility is unspecified. Do not silently change all callers or publish a new package version merely because the code now builds.

## Migrate Narrowly

For an approved change, update necessary call sites, exports, tests, and examples together. Add a temporary adapter only when real consumers need a transition, with an explicit retirement condition. Avoid indefinite compatibility machinery for imagined users.

Preserve unrelated callers and examples. Do not create a parallel component system just to avoid touching a few legitimate consumers.

## Test the Public Contract

Select representative usage, an important edge state, supported ownership modes, callback arguments, native attributes, focus, and changed disabled or pending behavior. Test meaningful invalid combinations at the type level when the project already supports that workflow.

Do not replace real consumers with a test that only reasserts the implementation's own helper calls. A prop rename test should demonstrate a valid consumer; an ownership test should show the parent accepting or rejecting a requested change.

For reset behavior, test the relevant transition rather than first mount alone. For export changes, verify the actual public import path.

## Verification

- The affected consumers and breaking surfaces are known.
- Compatibility changes were authorized before implementation.
- Necessary code, types, exports, examples, and tests move together.
- Runtime and type evidence address their different claims.
- Temporary adapters have a real consumer and retirement condition.
