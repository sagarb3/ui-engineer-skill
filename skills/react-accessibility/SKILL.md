---
name: react-accessibility
description: Build or fix accessible React interfaces with semantic controls, keyboard interaction, focus management, form feedback, and checks beyond automated scans.
---

# React Accessibility

## When to Use

Use for interactive UI changes or requested accessibility reviews. Inspect the affected interaction rather than expanding a small fix into a whole-product audit.

## Process

1. Identify the user task, affected controls, existing accessible primitives, and project requirements. Ask before proceeding when expected interaction or accessibility scope is unclear.
2. Prefer native HTML: buttons for actions, links for navigation, associated labels for inputs, and meaningful heading order. Give controls accessible names; use unique IDs for labels and descriptions. Add ARIA only when native semantics are insufficient, keeping state truthful.
3. Support keyboard operation and visible focus. For dialogs, use a proven accessible primitive, set initial focus, contain focus while modal, support appropriate dismissal, and restore focus to the trigger. Keep ordinary controls out of custom tab-order schemes.
4. Associate errors and instructions with their fields. Announce relevant asynchronous status without stealing focus or flooding live regions. Preserve entered values on recoverable errors. Ensure meaning does not rely on color, hover, motion, or pointer input alone.
5. Check applicable WCAG AA requirements, including text contrast, non-text contrast, reflow, zoom, target size, and reduced motion. Run existing automated checks, then manually verify keyboard flow and affected assistive-technology interactions in a browser. Report coverage limits rather than claiming compliance from a scan.

Generated code must contain no AI attribution. Keep new content in English. Exclude skills-repository references, parent-agent mentions, authoring-tool names, and provenance links from downstream code, comments, commits, and documentation. Preserve existing legal notices.

## Start With the Interaction Contract

Identify what a user must discover, operate, and understand. Inspect the accessible name, role, state, focus movement, error feedback, and recovery path for that task. A button with a label can still be unusable if opening its dialog loses focus or the result is never announced.

Use the existing accessible primitives and their supported composition APIs. Do not replace a proven menu, combobox, or dialog with generic elements and partial keyboard handlers. Keep native semantics where they already fit. A navigation link needs a real destination; an action needs a button with an appropriate type.

Clarify custom interaction requirements before choosing a widget pattern. A select, an editable combobox, a menu, and a list of navigation links have different keyboard contracts even if they look similar.

## Names, Descriptions, and Forms

Visible labels should describe the control's purpose and remain available after text is entered. Associate labels programmatically, and ensure repeated components produce unique IDs. Do not use placeholder text as the only label or add an `aria-label` that unexpectedly replaces the visible wording.

Use descriptions for instructions and errors without packing every piece of surrounding copy into the control's name. Mark invalid state when validation has actually failed according to the product's timing rules. A field should not announce an error before the user has had a reasonable opportunity to enter it unless the existing workflow requires immediate validation.

Example field relationship, assuming a project using React's `useId`:

```tsx
import { useId } from 'react';

function ReferenceField({ error }: { error?: string }) {
  const fieldId = useId();
  const hintId = `${fieldId}-hint`;
  const errorId = `${fieldId}-error`;

  return (
    <div>
      <label htmlFor={fieldId}>Reference</label>
      <input
        id={fieldId}
        name="reference"
        aria-invalid={error ? true : undefined}
        aria-describedby={error ? `${hintId} ${errorId}` : hintId}
      />
      <p id={hintId}>Use the reference shown on your invoice.</p>
      {error && <p id={errorId}>{error}</p>}
    </div>
  );
}
```

This establishes field associations; it does not define validation timing or complete announcement behavior. For a failed multi-field submission, the accepted workflow may also need a summary linked to invalid fields and deliberate focus placement. Keep values available for correction. Do not block paste, password managers, or standard browser editing shortcuts.

## Keyboard and Focus Review

Walk the affected task using only the keyboard. Check that the focus order follows the reading and interaction order, each operation is available, focus is visible, and exiting a region is possible. Avoid positive `tabIndex`; use normal document order for ordinary controls.

For composite widgets, use the chosen primitive's keyboard model. Arrow-key navigation and roving focus apply to particular patterns, not every row of buttons. Do not make noninteractive text focusable merely because it is visually important.

For modal dialogs, verify a meaningful accessible name, an appropriate initial focus target, containment while modal, inactive background content, expected Escape behavior, and a reachable close control where appropriate. Restore focus to the trigger or a logical successor if the trigger no longer exists. Large explanatory content may need initial focus on a heading rather than an input; do not always focus the first interactive element mechanically.

After deleting an item, changing a route, or replacing a loading region, verify focus does not disappear into the document body or land on an unrelated control. A visual success message does not repair lost focus.

## Dynamic Feedback

Use a restrained status announcement for meaningful background updates. Reserve urgent announcements for information that needs immediate attention; do not put every changing count or keystroke into an assertive live region. Keep announcement text specific to the result rather than repeating the whole screen.

For loading and pending actions, preserve understandable labels and indicate busy state on the relevant region when useful. `aria-disabled` communicates state but does not itself block activation; implement the behavior consistently when native disabled semantics are not appropriate.

Tooltips cannot carry essential instructions available only on hover. Provide keyboard access and an accessible description where needed. If information is required to complete a form, keep it available in the normal flow rather than hiding it exclusively in a tooltip.

## Visual and Motion Checks

For applicable WCAG AA checks, ordinary text generally needs a contrast ratio of at least 4.5:1, with 3:1 for qualifying large text. Relevant non-text indicators also need sufficient contrast; evaluate their actual state and background rather than just a palette swatch. Disabled and decorative content have different requirements, so assess the specific criterion.

Check text enlargement to 200% and reflow at a narrow viewport equivalent to 320 CSS pixels where applicable. Preserve controls, meaning, and reading order. Two-dimensional content such as some data tables has exceptions; that does not justify horizontal scrolling for the entire page.

Evaluate pointer target size and spacing under the applicable standard. WCAG 2.2 AA's target-size criterion uses 24 by 24 CSS pixels with defined exceptions; a larger comfortable target is often a better product choice. Do not mistake a recommended size for a universal conformance rule.

Honor reduced-motion preferences for nonessential motion. Avoid flashing, motion-dependent meaning, and fixed layers that obscure focused controls. Check status through text or shape as well as color. Give meaningful images appropriate alternatives and hide redundant decorative icons from assistive technology.

## Evidence and Scope

Run existing automated checks, then verify the changed task manually in a real browser. For assistive-technology checks, record the browser, assistive technology, flow, and observed result when available. If that environment is unavailable, state the limit and do not label the screen fully compliant.

Prioritize defects that block task completion, hide errors, trap focus, or prevent control discovery. Report the affected control, user impact, concrete fix, and verification method. Keep a local accessibility repair local unless a broader audit was requested.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Audit and Browser Proof](guides/audit-and-browser-proof.md) | Read when verifying accessibility or reporting findings. Use the applicable standard and project requirements; a quick audit is not a blanket conformance certification. |
| [Focus and Composite Widgets](guides/focus-and-composites.md) | Read for dialogs, menus, tabs, comboboxes, disclosure groups, and focus after changing content. |
| [Semantic Controls and Forms](guides/semantic-controls-and-forms.md) | Read for labels, field feedback, native semantics, accessible names, and validation behavior. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Anti-patterns / Red Flags

- Click handlers on generic containers, positive `tabIndex`, hidden focus outlines, and placeholder-only labels.
- ARIA contradicting native semantics, duplicate IDs, and focus lost after a UI update.
- Disabled zoom, inaccessible error feedback, or assuming an automated pass proves accessibility.

## Verification Criteria

- The affected task is usable by keyboard with predictable, visible focus.
- Controls expose correct names, roles, values, and states; errors are discoverable.
- Relevant visual, automated, and manual checks are recorded with their limits.
- Changes preserve established interaction patterns and contain no attribution fingerprints.
