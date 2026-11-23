# Design System Consistency Examples

These examples assume an existing product design system. Replace component, token, and route names with the active system. Expected deliverables are review criteria, not observed results.

## Align a Settings Action

**Use case:** A settings screen uses a hand-styled save button with a one-off color and spacing, while nearby forms use the canonical action component.

```text
Use design-system-consistency to align the settings save action with
the existing ActionButton and semantic tokens. Preserve label, native
form submission, disabled state, focus, and error behavior. Check the
supported light and dark themes. Keep the fix local; do not change
shared defaults, add a second button system, or replace the palette.
```

**Expected deliverable:** Reuse of the canonical component or its supported variant without losing native behavior. A shared token or default should not change to repair one local screen.

**Review:** Compare with adjacent forms using the same content density. Check focus, disabled and pending states, form behavior, and actual theme combinations. Token substitution alone is not visual verification.

## Assess a Shared Density Change

**Use case:** The team wants denser data-entry controls, but the current shared default also appears in dialogs and touch-oriented screens.

```text
Use design-system-consistency to assess a compact control variant.
Inspect current variants and representative consumers, including
dialogs, long labels, validation errors, and touch layouts. Recommend
an existing variant or a narrow extension. Do not change global
defaults or update visual baselines before the compatibility and
design decision is resolved.
```

**Expected deliverable:** A concrete impact assessment and an implementation recommendation supported by real consumers. If approved standards conflict, the agent should identify the conflict and ask which governs.

**Review:** Ensure the recommendation preserves readable labels, useful targets, and accessible states. Snapshot differences should be inspected rather than accepted in bulk to make checks green.

## Useful Combination

Pair with `component-api-design` if a new public variant is needed. A local visual correction does not authorize a component API redesign or a design-system migration.
