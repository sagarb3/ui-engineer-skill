# Everyday Frontend Delivery

## Component and State Ownership

Inspect current consumers, primitives, tokens, framework conventions, data loaders, and test seams before designing a new abstraction. Keep transient interaction state local; derive values from props/state rather than duplicating them. Separate controlled and uncontrolled contracts, preserve valid empty values, use stable domain identities, and cancel or ignore obsolete async results.

Use composition for actual reuse, not every imagined variant. Do not introduce a second button/dialog system or state container for one feature. Preserve server/client boundaries in Next.js and existing reactive conventions in Vue/Svelte rather than transplanting React-specific hooks.

## Behavior-Focused Testing

Use Vitest and the repository's testing library for public behavior, accessible roles/names, real interactions, and deterministic async boundaries. Await user-event and UI updates; mock the external boundary rather than internal implementation. Cover accepted errors, retained inputs, retries, pending/disabled states, and ownership transitions. Avoid broad snapshots, arbitrary sleeps, implementation mirrors, and weakened expectations to conceal a bug.

Use Storybook for representative components, states, themes, and interaction examples. Use Playwright for browser integration and critical journeys, not every helper function. Keep fixtures isolated, make server readiness explicit, retain useful traces for failures, and use a documented small retry policy without hiding flakes.

## Accessibility and Design-System Hygiene

Prefer semantic HTML and existing accessible controls. Verify keyboard order, visible focus, dialog focus/dismissal/restoration, labels and error associations, contrast, motion preferences, zoom, responsive layouts, and meaningful announcements. Loading/error/empty/success states are part of the component contract.

Use semantic tokens, documented variants, themes, and existing breakpoints. Check light/dark or other supported themes. Inspect the rendered result and primary task when tools permit; source review alone does not establish usability or accessibility compliance.

## Performance and Build Health

Reproduce the slow interaction with representative data and an explicit device/runtime/network context. Distinguish render work, main-thread computation, layout, asset loading, network waterfall, server latency, and build bottlenecks. Optimize the measured path before memoizing or adding infrastructure.

For large UIs, consider pagination/virtualization only when its focus, semantics, and restoration costs are handled. For media, use appropriate dimensions/formats/loading priority. For bundles, inspect actual imports, route boundaries, duplicated dependencies, and client/server split. Preserve freshness, authorization, and recovery when caching requests.

Compare equivalent before/after conditions and state limitations. Bundle bytes are not interaction latency; CI duration is not production performance; generated tests are not passing tests.

## Preview Handoff

Bind the preview URL to the reviewed commit. Confirm public/private access, synthetic data, environment values, SSR/static behavior, expiry, and cleanup ownership. Exercise one primary user path plus error/retry and responsive/keyboard behavior. Do not expose private source maps, credentials, internal APIs, or customer data through a public preview.

Deliver the scoped diff, visual/behavior evidence, executed commands, preview commit/link if actually created, compatibility impact, and remaining manual checks. Preserve required product documentation while keeping authoring attribution out of application artifacts.
