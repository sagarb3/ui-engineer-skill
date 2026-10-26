# Task Boundaries

Read when scope, authorization, or acceptance criteria need to be established. A working contract should make the next action clear without creating unnecessary planning documents.

## Identify the Requested Outcome

Separate the user's goal from a suggested implementation. "Keep the draft after a failed save" is behavior; "add another state hook" is a possible implementation. Inspect existing ownership before deciding whether that suggestion is necessary. Preserve explicitly required implementation constraints.

Identify the entry point, desired result, behavior that must remain intact, and evidence needed for completion. Distinguish an implementation request from a review, investigation, explanation, or Git operation. A read-only review does not authorize applying its findings.

## Resolve Uncertainty at the Right Place

Repository facts such as formatter settings, installed dependencies, and current callers should be investigated directly. Product choices such as retry policy, persistence, or acceptable breaking changes need clarification when not established.

Ask one question that names the consequence. For example, a choice between clearing a draft on navigation and preserving it for later editing should be resolved before adding storage or route guards. Do not silently select the easiest interpretation.

Independent read-only work can continue while a question is pending, but do not implement the dependent choice. An unanswered question remains unanswered regardless of elapsed time.

## Preserve Authorization Boundaries

Editing code does not imply pushing, publishing, sending messages, spending money, or changing account settings. An authorized ordinary push does not authorize a force push. An exact instruction to delete a named obsolete branch supplies approval for that deletion; ask again only if the actual consequence differs.

Read-only inspection and reversible local preparation should make a consequential action concrete before requesting approval. Show the exact target and effect rather than asking a broad question such as "May I continue?"

If an operation is rejected by an external permission system, diagnose the cause without changing identity, disabling protections, or escalating unrelated access. Complete unaffected work and report the unresolved action honestly.

## Avoid Scope Drift

Do not turn a small correction into a package migration, design-system rewrite, global formatting pass, or unrelated documentation project. If the existing architecture prevents a correct fix, explain the narrow structural change that is required and confirm any new product choices.

Preserve pre-existing work. When changed lines overlap with another task, inspect their intent before editing. Do not reset the worktree to create a clean baseline.

## Verification

- The accepted outcome and task type are clear.
- Repository facts were investigated rather than delegated back to the user.
- Unresolved product choices stop only their dependent work.
- External and destructive actions stay within exact authorization.
- Completion is measured against the request, not an expanded feature list.
