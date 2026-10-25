# Completeness and Risk

Read when a smaller implementation or shorter response might omit behavior, safeguards, or evidence.

## Preserve the Non-negotiable Parts

Do not cut boundary validation, authorization, error handling that prevents data loss, accessibility, or required checks. A smaller UI still needs usable labels, keyboard behavior, and the accepted recovery path.

Do not hide a rejected operation with a catch that returns success. Do not replace a server permission check with a disabled button. Do not remove error descriptions to reduce markup or weaken a type because the correct union is longer.

Trim optional work, not the accepted outcome. Remove speculative features, redundant state, unnecessary configuration, and unrelated cleanup before touching necessary behavior.

## Verify the Chosen Scope

Map the changed behavior to one discriminating check. A bug fix needs the trigger that previously failed. A shared contract needs representative consumers. A visual change needs rendered evidence at the affected conditions. Run required project gates in addition to the focused proof.

Do not write tests that merely mirror an implementation expression or assert an arbitrary internal call count. Prefer a behavior that could regress independently of how the code is organized.

For a cosmetic text correction, the existing check or direct inspection may be sufficient. Do not create a testing framework just to make a trivial edit appear formal. Scale verification to actual risk and project requirements.

## Handle Limits Explicitly

If the environment cannot run a check, report that fact and the remaining claim. Do not say "verified" when only a file was generated. Do not run a paid or external workflow without the required authorization to avoid reporting a limit.

If a deliberate limitation is acceptable within the request, state it in ordinary engineering language where relevant. Do not tag every decision with a mode name or add workflow fingerprints to comments. A limitation that prevents the accepted outcome needs resolution, not a disclaimer.

## Stop Repeating Failed Guesses

When an approach fails repeatedly, identify the assumption it depends on. Collect a new observation that can distinguish causes. Ask when expected behavior remains unclear. Do not respond to failure by adding a new abstraction, dependency, or configuration switch without evidence.

For Git rejection or a destructive next step, preserve current work and obtain exact authorization. The trimming ladder never bypasses approval boundaries.

## Verification

- The complete accepted behavior remains implemented.
- Security, validation, error recovery, and accessibility are preserved.
- Verification addresses meaningful failure modes rather than implementation trivia.
- Unchecked claims and limitations are explicit.
- Work stops at the accepted outcome rather than expanding into adjacent projects.
