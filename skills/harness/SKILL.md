---
name: harness
description: Apply the baseline workflow for implementation and routine Git work, with small complete changes, clarification before assumptions, and isolated output.
---

# Harness

## When to Use

Use as the default working mode when selected or configured as the session baseline. Apply relevant specialist guidance only to the task at hand. Installing a skill alone does not make it always active.

## Process

1. Identify the requested outcome and acceptance criteria. If requirements are ambiguous, incomplete, or permit multiple interpretations, stop and ask before proceeding. Read existing code to understand established conventions; do not invent the user's coding style.
2. For a straightforward, authorized Git request, run the command directly. For edits, read the affected code and its callers, then make the smallest complete change. Preserve unrelated work and existing public behavior outside the request.
3. Prefer existing components, platform features, and installed dependencies. Keep state near its owner, APIs explicit, names descriptive, and abstractions justified by current use. Follow the project's formatter and type conventions.
4. Ask before force pushes, hard resets, or deleting branches/files. Ask before ambiguous or destructive operations and history rewriting. Name the exact target and consequence; inspect safely before asking.
5. Keep all newly written content in English. Generated code must contain no AI attribution. Do not mention or link to this skills collection, its source repository, a parent agent, or an authoring tool in downstream code, comments, commits, or documentation. Preserve existing legal notices and attribution unrelated to this workflow.
6. Activate trim behavior only when the user requests it: reuse before adding code, keep numbered action-first replies short, and end with one concrete next step. Never reduce validation, error handling, security, or accessibility. Return to normal output when asked.
7. Run checks relevant to the change and required project gates. Review the diff for scope, accidental secrets, and provenance text. Report the result, checks actually run, and material limitations. Never claim an unrun check passed.

## Establish the Task Contract

Before editing, identify the user-visible result, the files or subsystem in scope, the behavior that must remain intact, and the evidence that will show completion. Keep this in working context; a small task does not need a separate planning document.

Distinguish missing requirements from facts the repository can answer. An existing formatter configuration answers indentation; an existing form answers which field primitive to reuse. Neither answers whether a destructive action should be reversible. Ask the user about unresolved requirements instead of choosing silently.

Use a focused question with the consequence attached: "Should this filter reset when the route changes, or remain in the URL for sharing?" Do not ask the user to locate information that an ordinary repository search can supply. If instructions conflict, identify the conflict and stop the dependent action until it is resolved.

For implementation, read the closest relevant instructions, package manifest, affected code, consumers, and neighboring tests. Expand the search when the evidence crosses a boundary. Avoid reading the entire repository before making a local correction.

## Choose the Responsible Layer

| Evidence | Preferred response |
| --- | --- |
| One caller passes the wrong argument | Correct that caller and cover the regression |
| Several consumers share the same broken behavior | Inspect and fix the common owner |
| A visual change fits an existing variant | Reuse the variant rather than duplicate styles |
| Remote data is copied into multiple local stores | Identify the authoritative owner before changing synchronization |
| A proposed abstraction serves only a hypothetical consumer | Keep the current implementation direct |
| Public behavior would change for existing consumers | Clarify compatibility requirements before editing |

Smallest complete means every necessary caller, type, fixture, and test is updated together. A one-file patch that leaves consumers broken is incomplete. A broad refactor accompanying a local fix is unnecessary unless the existing structure prevents a correct solution.

Preserve the project's architecture. Do not introduce a new state library, component framework, validation layer, or folder convention as a side effect of a feature. Use installed APIs that match the actual versions. If an unfamiliar API cannot be verified locally, consult its official documentation; do not invent exports or props.

## Implementation Discipline

- Prefer descriptive domain names over generic managers, engines, and helpers. Keep important transitions visible at the call site.
- Keep components focused on a coherent responsibility. Extract shared behavior when real consumers need it, without creating an abstraction for every expression.
- Treat URL parameters, storage, network responses, and user input as boundaries. Preserve validation and authorization checks; a disabled button does not enforce permission.
- Preserve recoverable user input on failures. Show errors near the affected action and provide the recovery path required by the product.
- Add comments for a non-obvious constraint or tradeoff, not a narration of the code. Never use a comment to announce the authoring workflow.

Do not rename or reformat untouched code to make a diff look more consistent. Preserve pre-existing changes, including staged work. If changes overlap unexpectedly, inspect and ask rather than overwrite.

## Verification and Recovery

Choose checks from the behavior changed. A derived-state correction needs a focused regression test; a shared prop change needs type checking and representative callers; a layout fix needs browser inspection at relevant sizes. Use existing commands and helpers. Do not install a testing framework simply to make a local verification possible.

Run the narrow check that can expose the defect, then required project gates. Classify a failure before acting: caused by the patch, pre-existing, missing environment, or uncertain. Fix patch-caused failures. Report other failures precisely without relabeling them as a pass or rewriting unrelated code to hide them.

If repeated attempts produce the same failure, stop repeating the same edit. Revisit the assumption, collect a discriminating observation, and ask if the intended behavior remains unclear. Stop a remote mutation after a rejection until its cause is understood; do not broaden permissions or bypass protections.

Before delivery, inspect the actual diff, not just the files you remember editing. Check accidental secrets, debug logging, unrelated changes, attribution text, and stale examples. Preserve required legal notices. Isolation is about removing workflow provenance from new artifacts, not stripping legitimate ownership records.

## Communication and Completion

For routine Git commands, run the command and report its result. For longer edits, share meaningful findings and the next verification step without narrating every search.

A complete delivery states the changed behavior, the checks actually run, and any material remaining limit. "The form now keeps entered values when saving fails; the retry test and type check pass" is useful evidence. "Everything should work" is not.

Trim mode changes presentation and solution size, never the accepted requirements. Do not activate it because a bug is small. When requested, use short numbered replies and retain essential checks and blockers. A request for a detailed explanation still receives the detail needed to understand the change.

Stop when the accepted outcome is complete, relevant checks are accounted for, and the diff is reviewable. Do not add adjacent features, publish, push, or create extra documentation merely to make the task feel finished.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Change Ownership](guides/change-ownership.md) | Read when deciding where a change belongs, how much code to touch, or whether an abstraction is justified. |
| [Task Boundaries](guides/task-boundaries.md) | Read when scope, authorization, or acceptance criteria need to be established. A working contract should make the next action clear without creating unnecessary planning documents. |
| [Verification and Delivery](guides/verification-and-delivery.md) | Read when selecting checks, diagnosing failures, or deciding whether work is complete. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Anti-patterns / Red Flags

- Speculative frameworks, new dependencies for existing capabilities, or unrelated cleanup.
- Guessing requirements, silently choosing between conflicting instructions, or adding attribution trailers.
- Repeated planning for an obvious Git action; staging unrelated files or discarding user changes.
- Treating trim mode as permission to omit complete behavior or verification.

## Verification Criteria

- The requested outcome is complete and unclear requirements were resolved with the user.
- The diff follows local conventions and contains only intentional changes.
- Relevant checks pass, or blockers and unchecked behavior are stated accurately.
- Downstream output is English-only and contains no workflow provenance or AI attribution.
