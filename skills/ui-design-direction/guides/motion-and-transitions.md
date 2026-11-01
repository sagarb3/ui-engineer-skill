# Motion and Transitions

Use when an interaction, state change, entrance, or navigation transition needs motion. Motion should communicate what happened, where something went, or what deserves attention. Do not add animation mechanically to every screen.

## Define the Transition Contract

Identify the trigger, object affected, state before and after, visible feedback, duration policy, interruption behavior, and reduced-motion alternative. Reuse the project's current motion language and installed primitives. Clarify ambiguous requests such as "make it smooth" before choosing an interaction model.

Distinguish immediate feedback from work completion. A press state can acknowledge input immediately; success must wait for a real result. Do not postpone a business-state update until a decorative animation ends or display success before a save actually succeeds.

Review three useful moments when they apply: the primary action, an important state change, and initial presentation. The task may need only one. Entrance motion should not replay on every rerender, and ordinary controls need not perform an elaborate sequence.

## Coordinate Related Changes

Tie movement to the affected object. When an item moves into a collection, its result and the collection state should agree. When a row is removed, focus and neighboring layout must settle predictably. Avoid a button, badge, and panel moving independently without a causal relationship.

Use direction consistently. A drawer opens from its anchored edge and closes back toward it. Previous and next navigation should have an understandable relationship. Preserve list position and scroll context when returning from details where that is the accepted behavior.

Choose emphasis from the product. A meaningful completion or transformation can be memorable; an unrelated confetti effect may interrupt work. Keep expressive moments concentrated rather than giving every element equal movement.

## Choose a Technical Approach

| Situation | Approach to consider | Risk to inspect |
| --- | --- | --- |
| Simple press, hover, or disclosure | Existing control behavior or a CSS transition | Focus treatment, interrupted reversal, hidden content |
| Stateful entrance or exit | Existing animation primitives | Unmount timing, cleanup, accessibility tree |
| Object continuity between views | Supported shared-element or view-transition mechanism | Unique identity, old/new snapshots, fallback |
| Gesture or coordinated layout change | Existing mature animation tools | Input latency, layout work, lifecycle ownership |
| Complex material or spatial behavior | Appropriate media or rendering path | Device cost and a useful fallback |

Check supported APIs in the actual target browsers. Feature-detect optional transition capabilities and keep navigation functional without them. Do not add a new framework or animation dependency for a small effect already covered by the stack.

For React integrations, bind setup and cleanup to the proper lifecycle. Remove listeners, observers, timers, and animation handles on cleanup. Avoid leaking work when a route changes or a component remounts.

## Route and Shared-object Transitions

Choose a transition that matches implementation constraints. A simple visual cover can separate unrelated views, an overlap may preserve context between mounted regions, and a shared-object transition can connect list and detail. More continuity also means more lifecycle and layout coordination.

Do not keep two fully interactive copies of a screen mounted accidentally. Prevent duplicate focus targets, repeated side effects, and inconsistent announcements. Ensure loading and failure can interrupt a navigation sequence without leaving an opaque cover or hidden page behind.

For snapshot-based transitions, ensure transition identities are unique when required and actually refer to the same object. Check ghosting, content changes during capture, fast navigation, back navigation, and unsupported environments. A transition is optional presentation, never the only path to the new state.

Preserve focus and scroll according to the route's contract. A screenshot of the final state cannot prove that the transition maintained either.

## Timing, Interruption, and Reduced Motion

Use existing duration and easing tokens. Frequent actions need prompt response and limited travel; a storytelling sequence may be longer if the user controls it and the content justifies it. Do not apply one hard duration limit to every kind of experience.

Test rapid repeated input and reversal. A new action should proceed from the current state or replace the previous sequence predictably, not jump back to an obsolete starting point. Make terminal states deterministic even when motion is skipped.

Honor reduced-motion preferences and provide directly readable content. Disable nonessential movement or replace it with a simpler change; do not remove state feedback. Content must not remain transparent if an observer fails or motion is disabled.

Prefer changes that avoid unnecessary layout and paint where suitable, but measure the actual effect. Large blurred layers, multiple full-screen surfaces, and persistent offscreen animation can be expensive even when the changing property looks inexpensive. Do not add `will-change` everywhere.

## Verify in Motion

Operate the real control forward, backward, and rapidly. Check normal speed, final state, focus, scroll position, errors, background-tab behavior if relevant, and reduced motion. A frame sequence can show continuity but does not prove real-time responsiveness; a static screenshot proves neither.

Verify meaningful invisible results with text or accessible status when needed. Copying, background saving, or queueing work should communicate the actual result without relying on an animation alone. Do not announce success until the operation succeeds.

- Feedback, state, and visible outcome agree.
- Motion has a task-related purpose and works without its optional technology.
- Repeated input, interruption, cleanup, focus, and reduced motion are correct.
- Browser evidence supports any timing or performance claim.
