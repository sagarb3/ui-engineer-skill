# Visual Review

Use for a requested visual critique or the visual acceptance pass of an implemented screen. Judge the actual rendered result against the product's task and constraints. Separate this from a usability walkthrough and from a source-code review.

## Choose the Review Mode

| Work | Review standard | Output |
| --- | --- | --- |
| New screen or broad redesign | Confirmed brief, product fit, hierarchy, visual execution, required states | Readiness judgment and actionable findings |
| Existing-product polish or feature addition | Current brand, tokens, components, and adjacent screens | Specific deviations and local improvements |
| Exact recreation | Agreed reference, viewport, content, and fidelity contract | Observed differences and functional constraints |
| Direction comparison | The same facts and target surface across candidates | Comparative tradeoffs, not a manufactured winner |
| Named small correction | The changed region and its neighbors | Focused verification without a full redesign critique |

Do not penalize an established work tool for using familiar navigation or table patterns. Do not introduce a different font or palette during a consistency review because it matches personal taste. A recreation is judged by its requested target, not originality.

If the user asked for review only, do not edit files, create a replacement design, or enter an implementation loop. Report and stop.

## Prepare Evidence

Use the current revision, known viewport, actual content state, and representative screenshots. Include the relevant brief and fixed constraints. For existing-product work, provide current tokens or comparable screens. For motion, use direct operation, a playable recording, or an accurately described frame sequence.

Inspect evidence before reviewing it. A loading placeholder, missing font, blank canvas, stale screenshot, or wrong route can invalidate the conclusion. Label reused evidence and ensure it still applies to the current revision.

If independent review is authorized and available, give a reviewer the evidence and constraints without supplying the desired verdict or previous rationale. If review is performed by the implementer, identify it as self-review. Do not claim independent review without an actual separate reviewer.

## Review in Order of Impact

Start with overall hierarchy and reading at normal size. Can a viewer identify the main object, current context, and principal action? Then inspect composition, type, spacing, color, imagery, controls, and applicable states.

Look for task-blocking visual defects before polishing detail:

- Essential text is unreadable, clipped, or lost over imagery.
- The main action is hidden, obscured, or visually indistinguishable from decoration.
- The central image is missing, visibly unfinished, or incompatible with the agreed direction.
- Core information relationships are wrong, such as totals disagreeing with visible records.
- Supported responsive layouts or overlays prevent access to necessary content.

A strong decorative treatment does not offset those defects. Keep a readiness blocker separate from a stylistic preference.

For a new direction, check whether the composition expresses this product's content or could be reused unchanged for an unrelated product. This is a diagnostic, not a demand for novelty in every business control. Distinctiveness must not undermine conventions users rely on.

Inspect the middle and end of a long page. Check whether section rhythm, imagery, and emphasis continue the selected concept instead of reverting to repeated generic blocks. Verify that the ending gives an appropriate next action or conclusion to the content.

## Use Specific Findings

Each finding should state location, observed defect, user or design impact, evidence, and a concrete correction. Separate observed facts from hypotheses.

```text
Location: Narrow-screen inventory toolbar.
Observation: The primary action wraps below the scrollable table and is obscured by the fixed footer.
Impact: Users cannot reach it at the reviewed viewport without changing layout or zoom.
Evidence: Current narrow-screen capture and direct keyboard operation.
Correction: Let the toolbar wrap in normal flow and reserve space for the fixed action area.
```

Do not report vague instructions such as "add polish" or "make it premium." Do not add arbitrary findings to satisfy a quota. If an apparent defect might be caused by test data or the capture tool, mark it for reproduction before changing the product.

## Scores Are Optional

Use a numerical score only when requested or required by the existing review process. Define the rubric first. An optional ten-point rubric can assign up to two points each for task hierarchy, layout and typography, visual coherence, media and detail, and state/responsive execution.

Scores are reviewer judgments, not measured user outcomes or accessibility conformance. Report blockers explicitly regardless of total. For an existing-product consistency review, concrete findings are usually more useful than an aesthetic score.

## Fix, Re-check, and Stop

When fixes are authorized, address the highest-impact confirmed defects first. Re-check the changed state and any shared rules it affects. Do not replace the direction to solve a local alignment problem. Do not polish away a distinctive choice merely because the neutral alternative is familiar.

Use one bounded review pass followed by targeted verification unless new material defects justify more. Stop when the accepted criteria are met or a remaining decision needs the user. Additional screenshots or reviewer rounds must answer a specific unresolved question.

## Verification

- The selected review mode matches the requested work.
- Findings are supported by current evidence and distinguish fact from inference.
- Readiness blockers are explicit; scores do not hide them.
- Existing constraints and scope are preserved.
- Review independence, motion coverage, and other limits are reported truthfully.
