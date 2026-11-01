# Audit and Browser Proof

Read when verifying accessibility or reporting findings. Use the applicable standard and project requirements; a quick audit is not a blanket conformance certification.

## Define the Scope

Identify the route, task, controls, supported input methods, relevant devices, and changed states. Keep a local repair local unless the user requested a product-wide audit. Inspect existing primitives and accepted requirements before prescribing a replacement.

Prioritize inability to discover or operate controls, trapped or lost focus, inaccessible errors, unreadable essential text, and missing recovery. Do not rank a personal visual preference above a task-blocking defect.

## Automated Checks

Run the installed accessibility checks and inspect their evidence. An automated pass cannot establish correct focus sequencing, useful alternative text, sensible announcements, or task comprehension. A violation should be reproduced in the real affected state rather than treated as an abstract score.

Do not add a new scanning service, upload private pages, or publish evidence without authorization. If tools are unavailable, record the gap and perform the supported manual checks.

## Visual Conditions

Check rendered contrast on actual backgrounds, not palette values in isolation. Ordinary text generally requires 4.5:1 under WCAG AA; qualifying large text uses 3:1. Apply the relevant exceptions and non-text requirements correctly.

Check enlarged text, narrow reflow, long messages, focus visibility, and fixed-layer obstruction. Distinguish a legitimate two-dimensional data region from accidental whole-page horizontal scrolling. Respect reduced motion and avoid meaning that depends only on color, sound, hover, or movement.

Evaluate pointer target size and spacing under the applicable criterion. Do not confuse a recommended comfortable target with the standard's exact threshold and exceptions.

## Manual Task Proof

Complete the relevant path using keyboard and, when available, the intended assistive technology. Observe names, roles, values, state changes, announcements, and recovery. A simulated DOM assertion can support a finding but cannot replace real-browser operation.

Record the environment and what actually happened. If a screen reader or real mobile keyboard is unavailable, mark that behavior unverified. Do not infer it from a screenshot.

## Report Findings

State the affected location, observed barrier, user impact, supporting evidence, concrete correction, and re-check method. Separate confirmed failures from hypotheses and tooling limitations. Preserve existing accessible behavior while fixing the responsible layer.

Re-check the corrected interaction and any shared primitive consumers it affects. More scans do not compensate for a known unresolved keyboard trap.

## Verification

- Scope and standard are explicit.
- Automated and manual findings have appropriate evidence.
- Visual, keyboard, and assistive-technology claims are distinguished.
- Barriers are prioritized by impact on the task.
- Compliance and independence are never claimed without adequate proof.
