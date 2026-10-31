---
name: design-system-consistency
description: Align React UI changes with existing tokens, components, variants, themes, and interaction patterns without introducing a parallel design system.
---

# Design System Consistency

## When to Use

Use when adding UI to an established product or correcting visual and interaction drift. Creating a new design system requires an explicit request.

## Process

1. Inspect nearby screens, component exports, theme configuration, tokens, and existing examples. Identify the canonical implementation. Ask before proceeding if competing systems exist or the required treatment is unclear.
2. Reuse existing components, semantic color roles, spacing, typography, radii, and motion values. Check the installed library's actual API before using a prop or theme hook. Do not add a replacement library for a local gap.
3. Use an existing variant when it fits. Add a narrowly scoped variant only for a current requirement. Ask before changing shared token meaning or global component defaults; inspect their consumers first.
4. Preserve accessibility semantics, focus states, interaction behavior, and supported themes. Keep exceptions local and explain a necessary exception in ordinary project terms without provenance text.
5. Compare the changed screen with adjacent screens and relevant component examples. Verify supported themes, responsive sizes, and interactive states. Run existing visual checks when available; report if only code inspection was possible.

Generated code must contain no AI attribution. Write new content only in English. Keep skills-repository links, parent-agent references, authoring-tool names, and provenance text out of downstream code, comments, commits, and documentation. Preserve existing legal notices.

## Find the Canonical Pattern

Inspect actual usage as well as documentation. A token file may exist without being the active theme, and an old example may use a deprecated component. Check exports, current screens, theme providers, component examples, and relevant tests before choosing the source of truth.

When two systems coexist, identify which owns the affected surface. A migration in progress is not permission to move an unrelated page to the newer system. Ask when the target system or migration boundary is unclear. Do not merge conflicting design documents or delete legacy styles as part of an ordinary UI task.

Build a small mental inventory: canonical control, current variants, token roles, styling entry point, supported themes, and consumers affected by a shared change. Do not create a new inventory document unless the task requests one or the repository already maintains it.

## Reuse in the Right Order

1. Use a current component and supported variant that already fit the behavior.
2. Compose existing primitives for a local screen-level arrangement.
3. Add a local style using existing semantic tokens when the requirement is genuinely specific.
4. Extend a shared variant when real consumers need the same treatment.
5. Introduce a new primitive only when the existing system cannot express the required contract.

This order is a decision aid, not permission to invent missing requirements. Ask before a shared change that alters established behavior or token meaning. A new button color alone rarely justifies another button implementation.

## Token Roles and Theme Behavior

| Concern | Prefer | Risk to check |
| --- | --- | --- |
| Surface and content colors | Semantic background, foreground, border, status roles | Raw palette values may fail in another theme |
| Spacing | Existing spacing scale and layout primitives | Near-duplicate values create visible rhythm drift |
| Typography | Existing text roles and component defaults | Local font changes can break wrapping and hierarchy |
| Elevation and layering | Established overlay and z-index roles | A higher local number may break dialogs elsewhere |
| Motion | Existing transition tokens and preferences | New timing can feel inconsistent or ignore reduced motion |
| Sizing and density | Existing control sizes and density modes | A local override may shrink targets or clip content |

Semantic names express purpose, not a particular hue. A token called `--color-danger` should not be redefined locally to mean a neutral border. If no suitable role exists, determine whether the need is a local exception or a new shared concept.

For a project already exposing these illustrative tokens, a local layout can remain direct:

```css
.settings-section {
  display: grid;
  gap: var(--space-4);
  padding: var(--space-6);
  color: var(--color-text);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-panel);
}
```

Use the actual project tokens; do not add this token vocabulary just to copy the example. In a utility-first or CSS-in-JS project, use the established equivalents rather than introducing a new styling layer.

## Library and Styling Integration

Verify the installed library version and supported customization mechanism. Prefer documented slots, theme overrides, variants, or composition points over selectors that depend on internal DOM structure. Never assume an API exists because another library uses the same prop name.

Keep control semantics and interaction ownership intact. A styling wrapper must not drop IDs, descriptions, event handlers, disabled behavior, or refs needed for focus. Do not mix competing primitive systems inside one interaction without a concrete, verified need.

Distinguish screen layout from component design. A page-specific two-column arrangement belongs with the page. A shared input's error appearance belongs with the canonical input or its theme configuration. Avoid making a global override to solve one page's alignment issue.

For supported themes, check actual rendered combinations: content on surfaces, selected and focused controls, status indicators, disabled text, and overlays. A theme toggle changing variables successfully does not prove every state remains legible.

## Shared Changes and Compatibility

Before changing a default, locate representative consumers and identify which intentionally depend on it. Check common and edge uses: long labels, icon-only controls, compact tables, modal forms, and validation errors. Run existing component examples or visual checks where available.

If a required change would break established consumers, ask whether to introduce a new variant or perform an explicit migration. Do not silently change all callers, add permanent compatibility layers for hypothetical consumers, or remove old variants without approval.

Keep exceptions narrow and attributable to product needs in ordinary language. An explanation such as "The chart legend uses the data-series palette" communicates the reason without mentioning a skill or authoring workflow.

## Review the Whole Surface

Compare the changed region with adjacent screens at the same viewport and density. Check control height, label alignment, section spacing, text roles, border treatment, icon size, focus, and validation appearance. Similar colors alone do not establish consistency.

Capture and inspect relevant rendered states when tools permit. Distinguish existing drift from changes introduced by the patch. Do not use a consistency task to redesign unrelated screens. Report shared impact and any visual checks that could not be run.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Design Rules and Visual Regressions](guides/design-rules-and-visual-regressions.md) | Read when documentation conflicts with implementation, visual baselines change, or a UI task affects shared rules. |
| [Shared Components and Variants](guides/shared-components-and-variants.md) | Read when extending a primitive, choosing a variant, or deciding whether a visual requirement belongs locally or globally. |
| [Tokens and Themes](guides/tokens-and-themes.md) | Read when choosing colors, spacing, typography, elevation, density, or theme-aware styles. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Anti-patterns / Red Flags

- Magic values where a fitting token exists, raw palette colors for semantic roles, and duplicated primitives.
- Deep selectors into library internals, blanket `!important`, and global overrides for one screen.
- Shared token changes without checking consumers or undocumented visual exceptions.

## Verification Criteria

- Existing primitives and tokens are reused, with only necessary local exceptions.
- Themes, interaction states, and responsive behavior remain consistent.
- Shared changes have been checked against their affected consumers.
- Visual checks and limitations are reported; downstream output has no attribution fingerprints.
