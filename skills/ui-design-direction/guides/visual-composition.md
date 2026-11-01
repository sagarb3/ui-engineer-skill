# Visual Composition

Use this guide when a screen's hierarchy, typography, spacing, surfaces, or visual identity needs deliberate design. Begin with the whole composition, then inspect component details.

## Diagnose Relationships Before Styling

Identify the first thing a viewer notices, the next thing they need, and the action the screen supports. Diagnose a concrete relationship: competing headings, controls detached from their results, repeated emphasis, or insufficient separation between groups.

Try changing order, proportion, alignment, or grouping before adding decoration. A stronger shadow does not fix an unclear reading order. Intentional asymmetry can work when alignment within regions and reading order remain clear; do not center every element merely for symmetry.

Use a quick reduced-size view to inspect visual weight, then return to actual size to judge readability. An abstracted or text-obscured view can reveal composition but cannot prove that labels or content are usable.

## Control Density and Space

Assign inter-region spacing to the parent layout and internal spacing to the component. Avoid several nested containers each adding padding to the same distance. Related controls should remain close enough to be understood as a group, while sections have a clear separation.

Use density appropriate to the job. A frequently used work queue benefits from visible information and compact controls; a reading surface needs comfortable line length; an expressive landing page may use large contrasts in scale. Spacious does not automatically mean better, and compact does not mean cramped.

Use a separator only when it clarifies a relationship. Check repeated borders around already separated content, nested framed panels, and a divider placed against another divider. Retain deliberate graphic rules when they are part of the selected direction rather than removing them mechanically.

## Typography as a System of Roles

Define a few roles using the project's actual typography: display, page heading, section heading, body, label, supporting text, and data. Not every page needs all roles. Establish hierarchy through size, weight, position, and spacing, with enough contrast between roles to be visible.

Inspect the real font rather than assuming the requested family loaded. Verify its available weights, fallback behavior, glyphs, line breaks, and browser rendering. Avoid synthetic weight or an accidental fallback that changes the layout.

For English text, inspect long words, names, URLs, contractions, and natural line breaks. Do not insert arbitrary breaks that make one screenshot attractive but fail with real copy. Use comfortable line length and line height for prose; dense numeric comparison needs a different treatment. Use tabular numerals where changing or aligned values benefit from stable widths.

Do not shrink important copy or lower contrast until it disappears. Truncation should reflect an actual content-priority decision and provide access to the complete value where needed. Avoid ellipsizing the only identifier that distinguishes records.

## Color, Surfaces, and Emphasis

Start from established brand and semantic tokens. When the brief authorizes a new palette, identify why it fits the audience, content, and setting. Define foreground and background relationships, selected states, focus, status, disabled treatment, and overlays together.

Do not treat a material metaphor as a required palette. A concept based on precision need not become black and neon; a natural theme need not become beige. A largely neutral interface can let actual product imagery carry color when that serves the direction.

Test color in rendered combinations, including text over imagery and moving backgrounds. Preserve meaning with text, shape, or position rather than color alone. A subtle surface difference should remain distinguishable under supported themes and ordinary display conditions.

## Controls, Icons, and Content

Use existing control grammar: label position, sizes, focus, selection, disabled state, and error treatment. Keep interactive and decorative objects visually distinguishable. Do not make every card appear clickable if only one inner button works.

Use a coherent icon family and optical size. Different icon viewboxes can make identical CSS dimensions look uneven. Give functional icon-only controls accessible names. Do not substitute emoji for a missing production icon or use a generic icon as a product's entire central illustration without an intentional reason.

Use realistic example content with internally consistent relationships. Totals should agree with rows, selected details should match their source object, dates should follow a plausible order, and empty states should not contradict a nonzero badge. Label demonstration data where the product requires it; do not fabricate customer evidence or business claims.

Replace vague copy with task-specific language. Keep instructions close to their action. Avoid repeating the same explanation in the title, subtitle, card, and tooltip. Remove redundancy while retaining the context needed to decide and recover.

## Quality Review

Inspect the main viewport, a relevant alternate width, and the state most likely to break the composition. Read the actual text at normal zoom. Check alignment, accumulated spacing, control dimensions, visible main action, density, contrast, and image crop.

Verify hierarchy without depending on animation or perfect placeholder lengths. Preserve distinctive choices that support the brief; do not polish every product into the same neutral template.

## Verification

- A clear visual hierarchy serves the task and selected direction.
- Text is readable in the real font at actual size, including fallback and long content.
- Space, surfaces, colors, and controls express consistent relationships.
- Icons and imagery have an appropriate role; demonstration content is coherent.
- Observed improvements are supported by rendered evidence, not source inspection alone.
