# Tokens and Themes

Read when choosing colors, spacing, typography, elevation, density, or theme-aware styles.

## Find the Active System

Inspect the actual theme provider, token exports, styling entry point, current examples, and nearby screens. An old token file may no longer govern the route being edited. When two systems coexist, identify which owns the surface before adding styles.

Ask when conflicting design rules or migration boundaries are unresolved. Do not migrate an unrelated page to a newer system merely because it appears preferable.

## Use Meaningful Roles

Prefer semantic roles for content, surfaces, actions, borders, focus, and status. A raw palette color can be appropriate for data-series identity, but should not silently replace a semantic error or selected-state role.

Reuse the existing spacing and text scales. A value close to an established token may indicate accidental drift, but do not replace a necessary local dimension mechanically. Explain an actual exception in product terms.

Keep ownership clear: page layout owns space between regions; a component owns its internal spacing. Avoid accumulated padding across several wrappers or local overrides that compensate for a wrong shared default.

## Theme and State Combinations

Check text on the actual surface, selected and disabled controls, focus, status indicators, overlays, and images under supported themes. Changing variables successfully is not proof that all combinations remain readable.

Do not redefine a semantic role to mean something different in one component. If a new role is required, determine whether it is a local exception or a shared concept. Ask before altering established shared meaning.

Use existing elevation and z-index roles. A very large local z-index may fix one panel while breaking dialogs and notifications elsewhere. Inspect the actual stacking context rather than escalating numbers.

## Verification

- The selected tokens belong to the active system.
- Semantic roles retain their established meaning.
- Spacing and typography preserve consistent relationships.
- Supported theme and interaction-state combinations remain readable.
- Shared token changes have an explicit scope and checked consumers.
