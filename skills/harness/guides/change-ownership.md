# Change Ownership

Read when deciding where a change belongs, how much code to touch, or whether an abstraction is justified.

## Trace the Actual Path

Follow the entry point through the component, callback, state owner, external boundary, and visible result. Inspect callers and nearby tests before changing a public function or prop. Use the smallest search that can reveal the responsible layer, expanding only when evidence crosses that boundary.

One incorrect caller normally needs a caller correction. Several callers with the same defect may indicate a shared owner. Repeated workaround code is evidence to inspect the owner; it is not automatic permission to merge unrelated behaviors.

## Choose a Complete Seam

Keep validation at trust boundaries and domain rules where the project already owns them. Do not move authorization into a disabled button or make a display component responsible for durable persistence simply to reduce file count.

A complete change may require a component, callback type, consumer, fixture, and test. File count is not the measure of simplicity. Prefer a clear existing seam over a one-file patch that duplicates logic or makes an invariant optional.

## Reuse With Evidence

Inspect the actual API and current version of a helper or installed library. Similar names do not prove equivalent behavior. Check empty values, ordering, cancellation, error semantics, and accessibility before substitution.

Use native capabilities when they fit project conventions. Do not replace the established accessible field with a raw input solely because the raw element is shorter. Conversely, do not add a wrapper around a direct platform expression without a current need.

An abstraction should have a concrete owner and actual consumers. Give it domain-specific inputs and outputs rather than a generic options object that anticipates unrelated future cases. Keep ordinary control flow visible.

## Preserve the Surrounding Contract

Avoid renaming, moving, or reformatting unrelated code. Preserve public defaults unless the change explicitly addresses them. Keep state identity and user input stable when restructuring components.

Comments should explain constraints the code cannot express. Do not narrate simple operations or label code with the tool or workflow that authored it. Preserve existing legal notices.

## Example Decision

If a clear button changes the text but leaves results stale, inspect whether the results are derived from the text or copied into separate state. Correcting duplicate ownership may be smaller and more reliable than adding a second clear handler. Verify the actual matching contract before changing search semantics.

## Verification

- The change reaches the layer that owns the invariant.
- All necessary callers and types are updated together.
- Reused APIs were checked for behavioral compatibility.
- No speculative abstraction or unrelated cleanup accompanies the fix.
- Existing validation, error behavior, accessibility, and user work remain intact.
