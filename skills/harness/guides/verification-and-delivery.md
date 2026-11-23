# Verification and Delivery

Read when selecting checks, diagnosing failures, or deciding whether work is complete.

## Match Evidence to the Claim

| Changed behavior | Useful evidence | Insufficient on its own |
| --- | --- | --- |
| Pure transformation | Boundary and regression cases | A successful build |
| Public props | Type checking and representative consumer behavior | One updated call site |
| Async interaction | Controlled completion, rejection, and relevant races | A snapshot of initial state |
| Layout | Browser inspection at affected widths and content states | Source inspection |
| Persistence | Supported read-back after a real successful operation | A success toast |
| Git publication | Successful push to the intended destination | A local commit |

Run the narrowest check that can expose the changed defect, then required project gates. Use installed tooling and documented commands. Do not download a new runner implicitly through a package-manager shortcut.

## Classify Failures

Determine whether a failure was caused by the change, already existed, reflects missing configuration, or remains uncertain. Fix a patch-caused failure. Preserve evidence for other failures and state the limit without calling them passes.

Repeated failure should produce a new observation. Inspect the assumption that the failure challenges rather than alternating cosmetic edits. Do not widen the change simply to make unrelated checks green.

If a check cannot run, identify the missing prerequisite, what was actually inspected, and which claim remains unverified. A code review is useful, but it is not an executed test.

## Audit the Deliverable

Inspect Git status and the actual diff. Read untracked files directly. Check scope, secrets, debug output, required assets, examples, unresolved markers, attribution text, and accidental workflow files. Preserve pre-existing staged changes and unrelated work.

New product code, comments, commit messages, and documentation must be English-only and contain no AI attribution or links back to the skills collection. Required legal notices remain. Do not copy tool logs, source prompts, or evaluation rubrics into product artifacts.

## Report and Stop

Lead with changed behavior. Name checks actually run and material limitations. Include the relevant branch, commit, preview address, or file only when it helps review the result. Never claim independent review, deployment, accessibility compliance, or browser validation unless it occurred.

Stop when the accepted outcome is complete and verification is accounted for. Optional adjacent improvements are not unfinished required work. Do not push, publish, or install globally merely to finish a local editing task.

## Verification

- Every reported claim has evidence appropriate to its level.
- Failed and unavailable checks are classified accurately.
- The final diff is intentional, isolated, and reviewable.
- Delivery preserves the original task and authorization boundaries.
