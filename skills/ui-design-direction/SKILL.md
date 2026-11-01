---
name: ui-design-direction
description: Design or review React interfaces, including visual direction, concept comparisons, screenshot reconstruction, imagery, motion, scroll stories, interactive experiences, and browser-based verification.
---

# UI Design Direction

## When to Use

Use for a new screen, visual redesign, unclear visual hierarchy, visual comparison, screenshot reconstruction, or a requested UI review. Use the relevant specialist guide for media, motion, scroll storytelling, and interactive experiences. Preserve established design direction for routine component fixes.

## Process

1. Inspect the existing UI, tokens, target devices, content, and primary user action. Ask before proceeding if the audience, desired outcome, or visual requirements are unclear. Compare multiple directions only when requested.
2. Define one direction using concrete choices: content hierarchy, layout, type scale, spacing rhythm, color roles, and interaction emphasis. Follow existing brand rules and components. Ask for a choice if the brief permits multiple interpretations.
3. Build the smallest representative screen with realistic content. Include applicable loading, empty, error, success, disabled, hover, and focus states. Let content determine responsive breakpoints rather than targeting one screenshot size.
4. Inspect the rendered result at narrow and wide viewports. Check long text, zoom, overflow, contrast, keyboard use, and reduced motion. Refine based on screenshots and observed behavior; state if browser inspection is unavailable.

Generated code must contain no AI attribution. Write new content only in English. Keep skills-repository references, parent-agent mentions, authoring-tool names, and provenance links out of downstream code, comments, commits, and documentation. Preserve existing legal notices.

## Select the Workflow

| Request | Work to perform | Boundary |
| --- | --- | --- |
| Named local visual correction | Inspect the component and adjacent content, make the correction, check the affected viewport | Do not reopen settled design direction |
| New screen or substantial redesign | Establish a concrete brief, resolve unclear decisions, implement the main path and states, inspect rendered output | Do not stop at an attractive default state |
| Compare directions | Present meaningfully different feasible concepts using the same facts and constraints | Build comparison views only when requested; do not implement every candidate as a finished product |
| Reproduce a screenshot or approved prototype | Establish viewport and fidelity requirements, measure the major relationships, rebuild with project components | Do not invent a new style or ship the screenshot as the interface |
| Review existing UI | Gather evidence, diagnose, rank findings, and stop | Read-only unless fixes are requested |
| Establish project design rules | Reconcile current evidence with existing rules and obtain decisions on conflicts | Do not silently replace approved standards |

## Detailed Guides

Read the guides triggered by the actual task before making decisions in those areas. These are supporting instructions within this skill, not additional skills or required tool installations. Paths are relative to this file.

| Task or question | Guide |
| --- | --- |
| Product facts, distinctive concepts, direction cards, first-screen structure, or side-by-side alternatives | [Design brief and exploration](guides/design-brief-and-exploration.md) |
| Visual hierarchy, typography, spacing, color, iconography, realistic data, and readable surfaces | [Visual composition](guides/visual-composition.md) |
| Screenshot fidelity, viewport measurement, responsive restructuring, keyboard and overlay risks | [Responsive reconstruction](guides/responsive-reconstruction.md) |
| Photography, illustrations, textures, sprite sets, video, or real-time 3D | [Media and assets](guides/media-and-assets.md) |
| Image-led concepts, image generation when available, long-page mockups, and conversion into real UI | [Image-led design](guides/image-led-design.md) |
| Feedback, entrance, interruption, shared-element continuity, route transitions, and reduced motion | [Motion and transitions](guides/motion-and-transitions.md) |
| Scroll-triggered reveals, scroll-linked scenes, pinning, parallax, and cinematic page narratives | [Scroll storytelling](guides/scroll-storytelling.md) |
| Games, tactile controls, drawing, timed experiences, reward flows, and canvas interaction | [Interactive experiences](guides/interactive-experiences.md) |
| New-design critique, existing-product polish, review gates, findings, and re-check limits | [Visual review](guides/visual-review.md) |
| Discoverability, first-use comprehension, a real task from entry to outcome, and recovery | [Usability walkthrough](guides/usability-walkthrough.md) |
| Running the page, screenshots, recordings, truthful evidence, and tool fallbacks | [Browser evidence](guides/browser-evidence.md) |
| Temporary files, comparison artifacts, existing design documents, and clean delivery | [Task artifacts and design rules](guides/task-artifacts-and-design-rules.md) |

For a new screen, begin with the brief and browser-evidence guides, then load only the specialist topics the screen uses. For a screenshot recreation, start with responsive reconstruction. For a review, choose visual review, usability walkthrough, or both according to the request. Existing project conventions and explicit user constraints take precedence over examples in these guides.

The [reference index](references.json) maps these guides for tooling. It is not a required client configuration or a request to load every guide.

## Define the Screen's Job

Separate the requested deliverable from the visual problem. A design recommendation, a prototype, an implemented screen, and a read-only critique have different stopping points. Do not change application code during a review or produce a static mockup when a working interaction was requested.

Inspect a representative existing screen and any current brand or design rules. Identify the audience, main task, frequency of use, content density, and primary action. Ask about unresolved requirements instead of treating a generic word such as "modern" as a complete brief.

For an existing product, distinguish adding a feature from redesigning the product. A new billing field should inherit the settings page's language. A requested settings redesign may change hierarchy and spacing, but does not automatically authorize changing brand identity or business flow.

Write a short direction in concrete terms. For example: "A compact inventory workspace where stock exceptions are prominent, filters remain close to results, and one primary action adds an item." This guides decisions more effectively than a list of visual adjectives.

## Build the Information Hierarchy

Choose what users need first, what supports the decision, and what can remain secondary. A dashboard should prioritize actionable data over a decorative welcome banner. A content page may need a strong reading rhythm. A conversion page may need evidence and a clear call to action. Do not force every screen into the same hero and card grid.

Use headings, grouping, alignment, and whitespace before adding borders and shadows. Related controls should look related. Distinguish primary, secondary, and destructive actions using established patterns. Keep labels specific: "Save address" tells users more than "Continue" when the next effect is saving an address.

For tables, prioritize columns and preserve relationships. Decide which columns can wrap, which need stable alignment, and whether narrow layouts should scroll or change representation. Do not hide essential data to make a screenshot look cleaner.

## Make Visual Choices Deliberately

| Concern | Decide | Check |
| --- | --- | --- |
| Typography | Hierarchy, body size, line length, emphasis | Long headings, readable dense text, font fallback |
| Spacing | Existing scale and grouping rhythm | Related items cluster; sections remain distinct |
| Color | Surface, content, action, status roles | Contrast and meaning without color alone |
| Shape and depth | Existing radii, borders, elevation | Depth communicates layering rather than decoration |
| Icons and imagery | Functional purpose and consistent family | Icons have names; useful images have appropriate alternatives |
| Motion | Which transition helps orientation or feedback | Reduced motion, interruption, and responsiveness |

Use real or realistic English content early. Test long names, zero values, large counts, empty metadata, and a multiline error. A layout that works only with short placeholders is not ready.

Do not impose a universal color palette, font, animation library, or CSS framework. Use the project's available assets and tokens. Avoid decorative additions that create no hierarchy, context, or useful feedback.

## Specify Responsive Behavior

Define what changes as available space changes: navigation position, column count, control wrapping, sticky regions, and content priority. Set breakpoints where the content needs them, within established project conventions.

Prefer flexible tracks and intrinsic sizing over fixed dimensions. In a grid or flex layout, verify children can shrink, long strings can wrap, and controls do not push the page beyond the viewport. Keep a deliberate scroll region for data that genuinely requires two-dimensional navigation.

Fixed headers, footers, and bottom actions must not cover content, focused controls, or virtual-keyboard interactions. Check available viewport height and safe areas when relevant. Do not treat one desktop screenshot and a scaled-down copy as responsive design.

## Design the State Model

For each important region, consider the states its data and actions actually support:

- Loading: preserve enough structure to avoid a misleading empty result and unnecessary layout movement.
- Empty: distinguish no data from no matching results; offer the relevant recovery action.
- Error: explain what failed near the affected region and retain recoverable input.
- Pending action: communicate progress and prevent accidental duplicate work where required.
- Success: confirm the result without unnecessary interruption or focus changes.

Do not add a skeleton, toast, or modal mechanically. Choose feedback appropriate to duration and consequence. A local field error should not require dismissing a global alert to understand it.

## Compare and Refine

When the user asks for alternative directions, compare meaningfully different hierarchy, density, navigation, or layout decisions using the same content and viewport. Merely changing accent colors does not create a useful alternative. Ask for selection before implementing a direction when the requirements leave that choice open.

For an agreed direction, build a representative slice and inspect it in the real browser. Compare screenshots at consistent sizes; then operate the page. Visual alignment cannot prove that a menu is usable by keyboard or that submission recovers from failure.

Record concrete defects: "At narrow width, the filter row pushes the results outside the viewport" is actionable. Fix the source of the layout problem rather than adding viewport-specific offsets to hide it. Re-check the affected region and adjacent content after changes.

## Delivery Evidence

State the implemented hierarchy and responsive behavior, the screens and states actually checked, and any missing browser verification. Do not claim visual or accessibility approval from code inspection alone. Stop after the requested design outcome; do not add an unrequested design-system migration.

## Anti-patterns / Red Flags

- Arbitrary gradients, decorative clutter, excessive motion, and low-contrast secondary text.
- Redesigning an established product without a request or introducing a second token system.
- Lorem ipsum hiding layout problems, fixed heights clipping content, and color-only meaning.

## Verification Criteria

- The primary action and information hierarchy are clear with realistic content.
- Layout works at relevant viewport sizes, with long text and zoom.
- Interactive states, focus visibility, contrast, and motion preferences are verified.
- The result follows the agreed direction and contains no attribution fingerprints.
- The applicable specialist guides were followed; omitted checks and unavailable capabilities are identified.
- Visual appearance and task completion were evaluated separately, with no claim of independent review unless it occurred.
