# Interactive Experiences

Use for games, drawing surfaces, timed experiences, tactile controls, simulated objects, and flows where manipulating the object is central to the product. Do not treat them as ordinary buttons with decorative effects.

## Model the Objects and Rules

Identify the objects the user recognizes, how input changes them, the allowed states, visible feedback, persistence needs, and the assets required for each state. A list of pages and controls is insufficient to define a game or simulation.

For a drawing surface, relevant states may include idle, drawing, cancelled stroke, undoable result, and saved result. For a reward flow, they may include eligibility, request pending, committed result, presentation, and failure recovery. Use the actual domain; ask about missing rules before implementing them.

Separate authoritative state from its presentation. Decide which system determines outcomes, which transitions consume a resource, and which actions must be idempotent. The end of an animation is not a reliable transaction boundary.

## Make the Interaction Understandable

Show the usable affordance, expected action, current state, and observable result. A control can feel physical without imitating every feature of a physical device. Labels, focus, and keyboard alternatives still matter.

For drag, rotation, pressure-like input, or gestures, define start, active, cancellation, completion, and out-of-bounds behavior. Clarify whether motion snaps, clamps, wraps, or returns. Do not infer game rules from the shape of a knob or wheel.

Provide appropriate feedback close to the object being manipulated. A slower reveal may be part of the experience when the user requested it, but ordinary control response should remain immediate. Keep essential outcomes available when motion, sound, or haptics are disabled or unavailable.

## Handle Input and Rendering Correctly

Use the project's input and rendering mechanisms. Map input coordinates into the actual rendered coordinate system, accounting for scaling, scrolling, and device pixel ratio. Test resize and orientation changes rather than assuming the canvas matches its CSS box.

Use pointer capture where the gesture needs continuity outside the initial target. Handle cancellation, loss of capture, and leaving the page. Limit touch-action restrictions to the surface that needs them; preserve page scrolling and zoom elsewhere.

Use an appropriate elapsed-time model rather than counting frames as time. Frame pacing varies by device and background state. Pause or reconcile timed behavior when the document loses visibility according to the product's rules. Release animation frames, listeners, observers, audio nodes, and rendering resources when the owner is removed.

Use real-time 3D only when perspective, physical interaction, or view-dependent material behavior matters. Otherwise a coherent image or sprite set may serve the same experience with less cost. Do not add a physics engine or rendering stack without a current, feasible requirement.

## Keep Transactions and Recovery Safe

For an experience that spends credits, assigns rewards, records progress, or saves a result, define exactly when the durable action occurs. Prevent duplicate settlement across repeated input, retries, refreshes, and interrupted presentations. Enforce eligibility and resource changes in the authoritative system, not only in the interface.

An illustrative transition sequence is:

```text
ready -> request pending -> committed result -> result presentation -> settled
                         -> recoverable failure -> ready or retry
```

The domain decides whether a retry is safe and how an unknown result is reconciled. Do not automatically start a second transaction when the first response was lost. Read back the known result or use an existing idempotent operation as required by the backend contract.

For a local game or canvas, preserve the requested progress and reset behavior. Do not add persistent storage merely because it might be useful later. If persistence is required, handle missing, old, or invalid stored data and define recovery instead of assuming parse success.

## Plan the Asset Set

Create a state-aware asset inventory before producing visuals. Keep camera angle, baseline, proportions, lighting, and rendering style coherent across objects and states. Characters, props, material maps, and animation frames may need separate production methods.

Check sprite alignment, frame order, looping seams, alpha edges, and the actual interaction size. An attractive still image cannot prove that an animation or hit target works. Keep meaningful symbols and state indicators recognizable at small sizes.

If sound is used, respect browser activation requirements and offer the product's mute controls. Provide visible feedback for important audio events. Do not claim haptic or sound quality from a browser session that cannot test it.

## Verification

Test the primary action, rapid repeated input, cancellation, boundary values, resize, loss of visibility, refresh, and recovery when relevant. Check touch and keyboard paths supported by the product. Verify a canvas is actually rendered before capturing evidence.

For stateful transactions, verify a committed result survives interrupted presentation and is not charged or settled twice. For timers and simulations, test elapsed-time correctness rather than only apparent animation smoothness.

- The rules, objects, state transitions, and authoritative owner are explicit.
- Input is responsive and coordinates remain accurate under supported layouts.
- Presentation cannot corrupt durable state or duplicate an operation.
- Accessibility, reduced motion, cleanup, and unavailable media have suitable behavior.
- Claims about feel, sound, haptics, or performance match what was actually tested.
