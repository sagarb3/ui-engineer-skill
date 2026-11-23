# Media and Assets

Use when a design depends on photography, illustration, diagrams, textures, a family of objects, video, or real-time 3D. Media must contribute to the product rather than compensate for a weak layout.

## Assign a Job to Each Asset

Decide what an asset helps the user recognize, understand, compare, locate, or feel. A useful object thumbnail, product demonstration, or explanatory diagram can be central to a work tool. A decorative landscape may contribute nothing to that same task.

Choose important imagery before finalizing the layout when its crop and shape determine composition. If the structure itself is unclear, fix structure first; more image detail cannot create a missing task hierarchy.

Define the subject, viewing angle, scale, lighting, background, detail level, and clear area needed for adjacent text. Choose the representation for the purpose: a real product photo, an explanatory vector diagram, a natural illustration, a texture, or interactive geometry. Do not use a tiny generic icon as a substitute for a required product image.

## Select a Suitable Source

Inspect existing project assets and user-provided material first. Reuse an appropriate asset instead of making a new one just to exercise a tool. For external assets, verify the actual license, permitted use, and attribution requirements; a search result or preview is not a license.

Use available image tools when the request calls for a new bitmap and those tools fit the task. Use the established vector or code-native system for icons, charts, and precise editable diagrams. Do not add a paid service, upload private material, or incur an unapproved cost merely because a concept would benefit from imagery.

If the necessary source or tool is unavailable, identify the missing asset and provide a concrete brief. Do not conceal the gap with a temporary graphic described as finished. Keep downloaded previews and inspiration images out of production unless their rights and resolution support that use.

## Integrate at the Real Display Size

Judge the asset inside the rendered page. Check subject scale, gaze or movement direction, crop, focal point, contrast behind text, and whether the image supports or competes with the action.

For an image intended to blend into the surface, inspect edge colors against the actual background. For transparency, inspect the alpha channel and edges on the final background; a filename or visible checkerboard is not proof of transparency. Preserve an intentional frame when the composition calls for one rather than treating seamless blending as mandatory.

Use responsive sources or art-directed crops when required. Reserve dimensions to reduce layout movement, choose appropriate resolution for actual display density, and balance visible quality with loading cost. Do not embed large originals as data URLs or lazily load the central above-fold image mechanically.

Test narrow crops and high-density rendering. A background that was clear for desktop text may place the subject behind the same text on a phone. Fix the crop, composition, or layout rather than adding an opaque panel that defeats the agreed concept without review.

## Build Coherent Sets

For objects, characters, collectibles, or repeated illustrations, define a common view angle, baseline, relative scale, lighting direction, palette, edge treatment, and background behavior. Preserve meaningful differences between objects. Applying the same filter to inconsistent source material does not necessarily create a coherent set.

Inventory the required states before production: normal, selected, unavailable, damaged, progressed, or other product-specific states. Define actual sprite dimensions, padding, alignment, and frame order when an atlas is needed. Check frames together for jitter and inconsistent silhouette size.

For scientific or engineering imagery, verify what the material actually depicts. Decorative labels, invented scales, or a preview rendering used as a technical texture can misrepresent the subject. Do not imply scientific accuracy from a realistic appearance.

## Texture and Surface Material

Distinguish a color texture from normal, roughness, displacement, and preview maps. Use the map appropriate to the rendering path. A photographed sphere is not a seamless wall texture.

Check tiling at final scale, seams, repeat frequency, visible artifacts, and contrast with foreground controls. Texture must not reduce readability or become the strongest object on a data surface. Apply monochrome or limited-color treatment only when it fits the approved direction and preserves information.

## Video and Real-time 3D

Use video when time-based footage explains or supports the content. Check poster, loading, loop seam, compression, playback controls, reduced-motion handling, captions for meaningful speech, and fallback. Do not rely on autoplay with sound; browser policy and user settings may prevent it. Essential information must remain available if playback fails.

Scrubbing video through scroll or gestures needs checks for arbitrary seeking, reverse movement, buffering, and memory. Do not decode a long clip into an unbounded set of full-size image frames by default.

Use real-time 3D when inspection, spatial behavior, lighting response, or physical interaction is necessary. If one image communicates the same result, prefer it. Reuse installed rendering tools, keep assets and scenes within measured device limits, and provide a meaningful fallback when the graphics context is unavailable.

Check camera framing, resize, input, canvas resolution, offscreen work, disposal, and context loss. A screenshot with a blank canvas is failed evidence. Do not claim a frame rate, realistic physics, or mobile performance without measurement on the relevant environment.

## Delivery and Verification

Put final assets in the project's normal asset locations. Keep original working files and unused candidates outside the shipped product unless requested. Production code must not depend on a temporary folder or external preview URL.

Preserve required source licenses and legitimate notices. Keep tool logs, prompts, private references, and workflow provenance out of downstream code, commits, and product documentation. Do not remove legally required attribution to satisfy output isolation.

- Every final asset has a clear role, usable rights, and sufficient visual quality.
- Crops, transparency, dimensions, loading, and actual-page integration were checked.
- Sets and animation frames remain coherent across required states.
- Video and 3D have suitable input, motion, performance, cleanup, and failure behavior.
- Missing assets and unverified capabilities are reported honestly.
