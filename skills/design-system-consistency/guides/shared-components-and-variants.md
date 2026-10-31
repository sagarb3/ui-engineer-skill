# Shared Components and Variants

Read when extending a primitive, choosing a variant, or deciding whether a visual requirement belongs locally or globally.

## Reuse Before Extending

Inspect existing components and their supported variants. Reuse a fitting variant, compose current primitives, or apply a narrow local layout before introducing a new shared concept. Do not create another button or input implementation for a color or spacing difference.

Verify the installed library API. Similar slots or props in another library do not prove availability. Use documented customization points rather than deep selectors into unstable internal markup.

## Distinguish Layout From Component Grammar

A screen-specific two-column arrangement belongs with the screen. A shared field's error appearance and label relationship belong with the canonical field or theme. Do not change a global component default to align one local form.

Add a shared variant only when real consumers need the same behavior or treatment. Define its name, supported states, semantic role, and relationship to current variants. Avoid several booleans that create undocumented combinations.

## Preserve Interaction

Styling wrappers must preserve IDs, labels, descriptions, events, disabled behavior, native attributes, and refs needed for focus. Do not mix competing primitive systems inside one interaction surface without a concrete compatible design.

Keep visual state synchronized with actual state. An apparently disabled or pending control must not remain freely activatable accidentally. A selected appearance must correspond to the exposed selected state.

## Check Shared Impact

Locate representative consumers before changing a default. Include long labels, compact density, icon-only controls, modal forms, errors, and relevant themes. Run existing examples or visual checks where available.

If the change breaks existing consumers, ask whether a new variant or an authorized migration is appropriate. Do not silently update unrelated callers or add indefinite compatibility machinery for imagined uses.

## Verification

- Existing variants and composition points were inspected.
- Shared behavior changes have actual consumers and an explicit contract.
- Local layout requirements stay local.
- Semantic and focus behavior survive styling changes.
- Representative consumers and supported states were checked.
