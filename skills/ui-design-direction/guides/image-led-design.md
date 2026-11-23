# Image-led Design

Use when a concept image is requested or when an available image tool is suitable for exploring a composition. This workflow does not require image generation for every screen and does not turn a design image into application code automatically.

## Choose the Deliverable First

Distinguish an image-only concept, an image followed by implementation, and direct UI implementation. Follow the user's selected path. Ask when the deliverable is unclear. Do not stop after generating an image if a functioning screen was requested, and do not edit the application when the request is only for visual exploration.

Check existing assets, permitted reference images, available tools, output formats, and costs. Follow established tool permissions and user preferences. Do not create accounts, purchase credits, install a separate service, or upload private screenshots without authorization. If image generation is unavailable, use a code sketch or describe the missing capability; do not pretend an image was produced.

## Define the Visual Brief

Describe the product's task, important content, principal object, first-screen composition, type hierarchy, color relationships, media treatment, and target device. Name the constraints that matter most. Keep the brief coherent instead of appending contradictory style words.

For a working surface, specify the actual objects and action relationships rather than asking for a generic dashboard. For a brand surface, define what makes the product distinctive and how the image supports the message. Do not add decorative window frames around a workspace unless they are explicitly part of the deliverable.

Use reference images according to their role:

| Reference role | Preserve | Do not infer |
| --- | --- | --- |
| Style evidence | Relationships in type, color, material, and emphasis | Its brand or unrelated business content |
| Fixed product shell | Approved navigation and regions | Permission to redesign the preserved shell |
| Fidelity target | Agreed structure and visible details | Unknown viewport scale or hidden behavior |
| Asset reference | The required subject and relevant visual properties | Rights to redistribute everything in the image |

Inspect a local reference before asking a tool to modify it. Use the host's supported image-reference mechanism. Do not rely on an inaccessible path or claim to preserve an image that the tool never received.

## Keep Geometry Unambiguous

Record CSS viewport, document extent, and output image dimensions separately. A high-resolution portrait image may depict a desktop page's full scroll length. It must not be interpreted as a phone merely because the canvas is taller than it is wide.

For a long page, plan the opening, evidence or explanation, deeper detail, and ending as a continuous hierarchy. Determine which sections have images, diagrams, real product content, or typographic emphasis. Avoid squeezing the whole narrative into a poster-like arrangement with unreadable labels.

When producing section images separately, keep compatible widths, typography, surface colors, and transition boundaries. Do not assemble unrelated images and describe them as one coherent page. Treat generated text as provisional; it cannot define actual product copy or data contracts.

## Inspect and Refine Deliberately

Open the result and inspect composition at the target logical size. Identify the largest problem, what should remain, and the variable to change. Examples include the wrong subject scale, insufficient clear space for text, a missing primary action, or an implausible content density.

Revise for a concrete reason rather than repeatedly requesting random variants. A structural defect needs a structural change; a new texture or stronger glow will not fix it. Stop when the selected concept meets the visual brief or when the next asset or requirement needs a user decision.

Do not assume a detailed image is a better design. Check readability, main action, product-specific content, and the feasibility of its components. A beautiful but impossible-to-operate concept is not an implementation target.

## Convert Into a Real Interface

Measure major ratios, content bounds, text hierarchy, image role, and alignment. Rebuild using the project's components, semantic HTML, normal document flow, actual text, and responsive layout. Use final asset files only for genuine imagery, not for the whole interface.

Replace distorted text, fabricated controls, inconsistent numeric relationships, and compressed long-page spacing with correct product content. Preserve the approved visual relationships while restoring readable layout. For an exact fidelity request, clarify changes that affect the target rather than silently interpreting it as a loose concept.

Do not place a full-page bitmap behind transparent links, embed the prototype in an iframe as the application, or reproduce every element with absolute positioning. Implement the actual interactions, pending and failure states, focus behavior, and framework boundaries.

Compare the rendered interface with the agreed concept at the same known viewport. Then verify alternate layouts and actual task completion. Visual resemblance and functional correctness are separate acceptance conditions.

## Verification

- The selected image or code path matches the requested deliverable and permissions.
- Reference role, viewport, document height, and output resolution are distinguished.
- Revisions address observed problems rather than adding decoration indiscriminately.
- The implemented UI uses semantic content and real interactions rather than a screenshot facade.
- No generation logs, tool names, prompts, or workflow attribution appear in product artifacts.
