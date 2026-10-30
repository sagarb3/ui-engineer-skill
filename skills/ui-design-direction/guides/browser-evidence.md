# Browser Evidence

Use to run the target UI, inspect real output, capture useful evidence, and report the limits of available tools. Successful source edits or a build are not proof of visual quality or usability.

## Use the Existing Runtime

Read the project's documented start and check commands, package manager, dependencies, and required environment. Reuse a suitable running development server rather than starting a competing process. Confirm its repository and revision instead of assuming any page on the expected port is the current application.

When a port is occupied, identify the conflict without killing an unrelated process. Use a supported alternate port or ask if the target is unclear. Do not rewrite build configuration or install a second toolchain just to make a screenshot convenient.

For a standalone prototype, use the requested delivery format and an appropriate existing static server when needed. For a React application, run the actual application rather than recreating a disconnected static version for evidence.

Respect environment permissions and consequential-action boundaries. A browser test should not publish, send messages, purchase, delete real data, or mutate unrelated services without authorization.

## Choose Available Tools Honestly

Use the host's available browser, screenshot, and image-inspection tools or the project's installed browser test stack. Do not reference scripts bundled by another project or invent command names that this skill does not provide.

If a tool cannot observe the required state, choose a supported fallback and state the limit. Code inspection, simulated DOM tests, static screenshots, frame sequences, recordings, and direct browser operation provide different kinds of evidence.

Use an isolated browser context where supported. Do not attach to a personal browser profile, bypass browser security, or export cookies to solve an environment problem. Use designated test credentials without exposing them in output.

## Capture the Actual State

Record route, viewport in CSS pixels, relevant zoom or device scale, revision, fixture or data state, and the action that produced the image. Wait for a meaningful readiness condition, such as the required content and fonts, rather than an arbitrary long sleep or an unsuitable global network-idle assumption.

For a stateful view, operate the real controls. Do not add production query parameters, hidden state switches, or fake success screens solely for screenshots. Reuse an existing test fixture mechanism when it represents the contract accurately.

Choose a viewport capture for the visible composition, a region capture for a local defect, or a full-page capture for document flow. Full-page images do not replace actual-size reading or demonstrate sticky and scroll-linked behavior automatically.

Inspect the resulting file. Check for missing fonts, broken assets, transparent entrance content, overlays, stale loading states, blank canvas, wrong route, and unintended sensitive data. A successful screenshot command does not prove the screenshot is valid evidence.

## Select Coverage by Risk

Use required project coverage first. Otherwise choose the primary viewport, a layout-changing alternate width, and one important edge state. For a single fixed-device task, verify the stated range instead of creating an unrelated cross-device matrix.

Examples of useful additional evidence include a long error message in a narrow form, a selected row opening a drawer, a populated data table, or the last scene of a long page. Add a case because it could affect a concrete decision, not because more captures appear more thorough.

Compare candidates and before/after states using consistent viewport, scale, content, fonts, and readiness. Label baseline, current, static, and interactive evidence. If shared styling changed, re-capture states it affects rather than silently reusing stale screenshots.

## Observe Motion and Interaction

Use direct operation for responsiveness, interruption, keyboard behavior, and perceived continuity. A playable recording can support those observations when captured at known conditions. A sequence of still frames can show state progression but cannot prove normal-speed smoothness or input latency.

For motion, operate forward and backward, repeat quickly, interrupt, and test reduced motion. For scroll scenes, inspect restoration and release from pinned content. For canvas or 3D, verify nonblank rendering and real input before capture.

Do not report frame rates or performance gains without actual measurements. Do not infer that native keyboard, haptics, audio, or assistive technology works from a video that did not exercise it.

## Read Back Important Results

When an authorized flow is expected to persist state, verify it through the supported reload or read-back path. A displayed toast, animation, or mocked response cannot independently prove durable completion. Distinguish a frontend demonstration from a backend-integrated test.

If a request result is uncertain, inspect the resulting state before repeating a consequential action. Keep local and external data boundaries explicit.

## Keep Evidence Useful and Contained

Store captures in the approved task or evidence location, separate from final application assets. Use descriptive names that identify viewport and state without including secrets or unnecessary personal data. Reuse unchanged evidence when it still represents the current revision, and label it accordingly.

Leave review or preview servers running only when needed for the requested handoff and allowed by the environment. Report their address and prerequisites. Stop only processes created for this task when cleanup is appropriate; do not terminate unrelated work.

## Verification

- The running page and evidence correspond to the intended application and revision.
- Captures show known viewports, actual content states, and loaded assets.
- Motion, task completion, and persistence claims use evidence suited to those claims.
- Missing tools and environment failures are reported accurately.
- Evidence contains no secrets, unauthorized mutations, or workflow provenance in product files.
