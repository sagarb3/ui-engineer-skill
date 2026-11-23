# Responsive Reconstruction

Use for screenshot recreation, approved mockup implementation, or layouts whose behavior changes across widths, input methods, and viewport heights.

## Establish the Reference Contract

Clarify whether the task calls for exact screenshot fidelity, a responsive interpretation, or borrowing selected visual relationships. These are different acceptance criteria. A fidelity task should not silently become a redesign; a concept image should not force broken geometry into the final product.

Record the reference's visible range, known CSS viewport, image dimensions, browser zoom if known, and device scale where relevant. A screenshot's physical pixels are not necessarily CSS pixels. For example, a 780-pixel-wide capture at a confirmed scale of two may represent a 390-CSS-pixel viewport. Do not infer scale from image width alone.

If necessary measurements are unknown, ask before treating an assumption as a strict target. Separate a full document capture from a single viewport. A tall image of a desktop page does not imply a mobile layout.

## Measure From Large Relationships to Details

Start with content width, navigation size, column proportions, alignment axes, dominant object, heading scale, and main action placement. Then inspect spacing rhythm, controls, image crops, borders, and shadows. Do not tune small details while the overall proportions remain wrong.

Use real layout primitives and intrinsic sizing. Do not reconstruct an entire UI through absolute coordinates or place transparent controls over a screenshot. The final interface needs semantic text, reachable controls, real data states, and responsive flow.

For a generated concept image, repair impossible details: distorted labels, inconsistent spacing, unreadable small text, and physically impossible controls. Preserve the agreed composition rather than reproducing artifacts. For an exact supplied screenshot, retain requested geometry and flag conflicts with usability or existing constraints instead of silently changing it.

If pixel comparison is part of the acceptance criteria, match viewport, fonts, content, scale, and state first. Mask only legitimately nondeterministic regions under the project's policy. Do not mask the changed control to make a visual test pass. When exact pixel matching is not required, compare composition and readable behavior without inventing a numerical fidelity score.

## Plan Responsive Changes Explicitly

| Region | Decide | Check |
| --- | --- | --- |
| Navigation | Persistent rail, compact header, or disclosed navigation | Current location and every required destination remain reachable |
| Main content | Columns, stacking order, or a retained scroll region | Reading order and task context remain intact |
| Details | Inline, drawer, new route, or expandable section | Selection context and back behavior remain understandable |
| Actions | Inline toolbar, wrapped group, or fixed action area | Labels fit and focused controls remain visible |
| Dense data | Prioritized columns, local horizontal scroll, or alternate representation | Essential values and relationships are preserved |
| Media or canvas | Crop, fit, reframe, or resize | Important subject, hit targets, and coordinates remain correct |

Breakpoints should follow content and existing project conventions. A desktop screen reduced with `transform: scale()` is not a responsive implementation. Do not hide required controls just to remove overflow.

Check minimum sizing in flex and grid children, long unbroken values, intrinsic image sizes, wrapping labels, and accumulated fixed widths. Fix the source of unwanted overflow rather than applying page-wide clipping that conceals it.

## Viewport Height, Overlays, and Input

Check fixed and sticky elements against actual available space, browser chrome, safe areas, and virtual keyboards where applicable. Opening an input must not hide its error, close control, or main action without a way to reach them.

Test modal and drawer scrolling separately from background scrolling. Avoid two competing scroll traps or an overlay whose close control scrolls out of reach. Verify focus containment and restoration using the established primitive.

For touch or canvas interaction, confirm the pointer coordinates account for rendered size and device scale. Use pointer capture and touch-action behavior appropriately to the intended gesture. Do not disable all scrolling or zooming globally to make one gesture work. Provide keyboard alternatives where the task requires them.

## Evidence Without an Exhaustive Matrix

Use the project's required viewport coverage. Otherwise choose the main viewport, an alternate width that changes layout, and one high-risk content or interaction state. Add more cases only when a specific risk warrants them.

For layout changes, inspect the affected region and adjacent content at actual reading size. For input changes, complete the relevant action. For a long page, inspect section transitions and the end, not just the opening. For a screenshot recreation, compare the same viewport and state before declaring fidelity.

Fix an observed defect in the viewport where it occurred, then check the shared rule's other consumers. More screenshots do not compensate for a known unresolved problem. Stop expanding evidence once the accepted range and identified risks are covered.

## Verification

- Fidelity, scale, and responsive expectations are explicit.
- Reference pixels are not confused with viewport dimensions or document height.
- Major proportions and typography are correct before decorative detail.
- Supported layouts, input methods, overlays, and high-risk content remain usable.
- No full-page image, coordinate overlay, or clipping workaround substitutes for real UI.
