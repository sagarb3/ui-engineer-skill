# Scroll Storytelling

Use when a page explicitly needs an expressive scroll sequence, product demonstration, or staged visual explanation. Do not impose cinematic scrolling on forms, work queues, documentation, or other surfaces where direct navigation is more useful.

## Decide Whether Scroll Carries the Story

Identify the product-specific object or relationship that changes as the reader progresses. A useful sequence may reveal construction, connect an input to an output, expose a detail, or follow a process. Random floating geometry and repeated fade-ins do not establish a narrative.

Clarify ambiguous requests for scroll movement. A reveal triggered by entering the viewport differs from a sequence whose progress follows scroll position. Choose according to the intended behavior rather than substituting one for the other because it is simpler.

Keep the underlying content readable without animation. The story should not be the only way to discover a claim, reach a link, or understand a result. Do not hijack the browser's ordinary wheel, touch, keyboard, or history behavior without an explicit product requirement.

## Choose the Progress Model

| Model | User expectation | Checks |
| --- | --- | --- |
| One-time reveal | A section appears when reached and stays available | Scrolling back does not hide content or repeat distraction |
| Scroll-linked sequence | Position determines the scene; reversing scroll reverses progress | Pause, reverse, fast jump, and restored position agree |
| Pinned scene | A region stays in place while a bounded story progresses | Entry and release are clear; content is not trapped |
| Layered parallax | Depth comes from restrained relative movement | Text remains stable and motion can be reduced |
| Discrete chapter change | Visible progress changes at a meaningful boundary | Navigation and reading order remain predictable |

Smooth scrolling changes input feel; it does not itself create a story. Do not add a global scrolling library by default. Reuse supported browser mechanisms or installed animation tools, with a readable fallback. Full-screen snap navigation requires a specific use case and testing; it is not a general page-layout solution.

## Write a Storyboard Before Implementation

For each scene, state the reader's question, visible object, change, supporting text, progress interval, and exit state. The object should remain identifiable as it moves between scenes. Do not assign arbitrary large scroll distances merely to make the page feel elaborate.

An example for a physical product might move from an overall view to an internal component, show the relevant mechanism, and return to a usable product view near the call to action. The chosen product determines the details; do not reuse that sequence for an unrelated service.

Vary the role of sections deliberately. Some may remain static for close reading. Others can use a transition to explain a causal relationship. Do not animate every paragraph with the same stagger or give decorative movement equal weight to the actual demonstration.

For a dominant wordmark, decide whether it remains an ordinary heading or transforms into a navigation identity. If it transforms, keep one clear semantic identity and avoid duplicate focusable copies. For an image-led stage, ensure foreground text and action visibility remain stable through its full range.

## Implement With Bounded Complexity

Use the project's established tools. Check browser support before relying on scroll timelines or other optional features. Scope observers, listeners, timelines, and measurements to their owner and release them on unmount or route change.

Avoid repeated synchronous layout reads in a scroll handler. Cache suitable measurements and update them when actual layout changes. Recompute correctly after font loading, image loading, resize, and orientation changes. Do not hardcode a single captured page height as the whole progress model.

Pin only as long as the scene needs. Check stacking, clipping, focus, and neighboring section flow. Nested scrolling regions and sticky headers can change which scroller owns progress; test the actual containing layout.

For video or 3D scenes, verify loading, seeking, reverse motion, device cost, and fallback separately. A blank or delayed scene must not prevent the rest of the page from being read or operated.

## Narrow Screens and Reduced Motion

Choose whether a narrow layout uses a reframed scene, a shorter sequence, or a static explanation. Preserve essential information and primary actions. Do not reduce the whole desktop stage until text becomes unreadable or remove the only explanatory content.

In reduced-motion mode, reveal content directly and replace nonessential movement with stable states. A fallback should communicate the same meaning. Do not make content depend on a scroll event that may never fire after the page opens at an anchor or restored position.

## Verify Nonlinear Navigation

Test from the top, from a middle-page anchor, after refresh at a restored position, while scrolling backward, and after a fast jump to the bottom. Resize during the sequence when supported. Check keyboard traversal, touch, focus visibility, and the normal reading path.

Use recordings or direct operation for timing claims; screenshots show only selected frames. Inspect the final section and release from pinned regions rather than stopping after an attractive opening.

- Every motion sequence serves an identifiable content purpose.
- Triggered and linked progress behave according to the selected model.
- Pinning, reverse movement, restoration, and layout changes remain stable.
- Content and actions remain usable on narrow screens, without motion, or when optional APIs fail.
- No scrolling library, animation, or asset was added without a present requirement.
