# Composition and Identity

Read when extracting components, moving state, changing lists, introducing hooks, or adapting public props.

## Preserve Identity Deliberately

Keys tell React which item persists across renders. Use stable record identity for lists that insert, remove, sort, or filter. Index keys can attach local state to the wrong item when order changes. Random keys recreate items and discard their state.

Component identity can also change when a component function is recreated inside another render. Define stable component boundaries at module level when preserving state matters. Do not change keys as a generic refresh mechanism; a key-based reset must represent an intentional ownership reset.

Before moving state, identify whether users expect selection, focus, or drafts to survive changes in parent rendering, route, or record. Clarify an unspecified reset policy rather than choosing the easiest remount behavior.

## Extract a Coherent Responsibility

A component can own a visual region, interaction, lifecycle, or repeated domain unit. It need not be split because it exceeds a fixed line count. An extraction should simplify ownership or real reuse, not scatter a straightforward interaction across wrappers.

Keep domain meaning in the interface. Prefer an explicit item ID and callback over passing internal state setters through many layers. Use composition where content arrangement varies, but do not introduce a generic component factory for one concrete screen.

## Custom Hooks

Extract a hook for reusable stateful behavior or a useful external-system lifecycle. Name its contract and cleanup responsibilities. Do not use a hook merely to hide a direct calculation or relocate every line out of the component.

Hooks should preserve React's supported call rules and project conventions. Do not call ordinary hooks conditionally, in callbacks, or in loops. Reuse existing hooks when their actual lifecycle and behavior match the task.

## Semantics and Native Behavior

Composition must preserve labels, IDs, descriptions, button types, form association, event behavior, and refs needed for focus. A style wrapper that drops those attributes can break an otherwise correct primitive.

Keep navigation and action semantics distinct. Do not replace a button with a clickable generic container during extraction. Avoid injecting untrusted HTML or moving authorization into display-only logic.

## Verify Consumers

Read the direct callers and relevant re-exports before changing a prop. Update necessary types and tests together. A type check does not establish runtime state preservation, JavaScript-consumer compatibility, or correct focus.

Use a reordered-list case to test identity when relevant, and repeated prop changes to test an extraction's ownership contract. Preserve behavior outside the requested change and avoid incidental folder reorganization.

## Verification

- Identity follows real objects rather than position or randomness.
- State and focus reset only when the accepted contract requires it.
- Extractions create a meaningful ownership or reuse boundary.
- Native semantics and consumer contracts remain intact.
