# Conflicts and History

Read for merge conflicts, rebase or amendment requests, destructive cleanup, and failed history updates.

## Make Consequences Concrete

Always obtain exact approval before a force push, hard reset, or deleting branches/files, including ignored or untracked files. A request naming the exact deletion already supplies that approval unless inspection reveals different consequences.

Also ask before other history rewrites or operations that discard edits. Explain the command, target, remote if relevant, and potential loss. Read-only inspection or a dry-run preview can establish the affected paths; the preview does not grant permission to act.

`--force-with-lease` is a safeguard, not an exemption. A backup ref or reflog may support recovery but does not authorize destruction.

## Inspect the Operation in Progress

Use Git's actual state to determine whether a merge, rebase, cherry-pick, or other operation is active. Do not start a second operation, remove metadata, or reset the index to silence the status.

Continue or abort within the authorized scope. Aborting can change the current working state; verify the effect on pre-existing edits. Do not assume that aborting every operation is always harmless.

## Resolve Meaning, Not Markers

Read both sides and the surrounding contract. A syntactically valid union of changes may still break state ownership, validation, callback arguments, or public behavior. Resolve compatible intent together; ask when the conflict requires a product choice or deletion.

Do not apply `--ours` or `--theirs` across all files as a generic strategy. Their meaning also depends on the operation. Inspect renamed and deleted files, generated lockfiles, and binary conflicts using the project's appropriate process rather than treating them as ordinary text.

After editing, inspect the staged resolution and run relevant checks. Removing conflict markers alone does not prove correctness. Continue only the existing approved operation.

## Rewrite With an Explicit Boundary

Before an approved rebase or amendment, identify affected commits and whether they are published. Preserve the intended commit content and message conventions. If a rewritten remote update is approved, use a narrow destination and a safeguard tied to the expected remote state where suitable.

If the remote changes, stop rather than automatically updating the expected value. The other contributor's work is new evidence, not a reason to escalate force.

## Recover Without Expanding Damage

Inspect status and relevant history before proposing recovery. Do not repeatedly reset or force push in an attempt to undo an uncertain result. Make the recovery target and effect reviewable before acting.

Report what succeeded, what remains in progress, and what was not executed. Do not hide a failed operation by deleting its working files or claiming a clean status means the intended history was preserved.

## Verification

- Exact targets and consequences were approved before destructive actions.
- Resolutions preserve both compatible intentions and required checks.
- No protection or safeguard was weakened after rejection.
- Remaining state and recovery limits are explicit.
