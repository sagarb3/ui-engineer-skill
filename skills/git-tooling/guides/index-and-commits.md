# Index and Commits

Read for staging, selective commits, pre-existing index content, and hook failures. A simple status request still needs only the requested command.

## Distinguish Three States

The committed tree, index, and working tree can each differ. Inspect status, the unstaged diff, and the staged diff when preparing a commit. An ordinary diff omits untracked file contents, so read new files directly before staging them.

If a file has staged and unstaged edits, adding the whole file will also stage the unstaged portion. Do not assume an existing staged version is already the intended commit. Ask when ownership of mixed changes is unclear.

## Stage the Intended Change

Use explicit paths and `--` before path arguments. For selected hunks, inspect the resulting staged diff rather than trusting the selection operation. Preserve unrelated staged content; do not unstage it simply to simplify your own workflow without approval.

If the user asks to commit only one change while unrelated edits are staged, make the conflict concrete and ask how to handle the index unless the session already establishes a permitted method. Do not silently include or discard someone else's work.

Review file names and contents for credentials, generated output, caches, private fixtures, and temporary screenshots. Do not use broad staging to make status clean. Follow established ignore rules without changing global configuration.

## Commit Accurately

Use the user's clear message or the project's existing convention. Describe the actual behavior changed in English. Do not add authoring-tool attribution or generated-by trailers. Do not alter Git identity, signing policy, or hooks to make the commit succeed.

Before committing, run the checks required by the task and project. If a hook reformats a file, inspect the new change and stage only intended results before retrying. A rejected commit is not a reason to bypass validation.

After committing, inspect the resulting commit and status. A hook may have changed additional files, and a commit may leave intended edits unstaged. Report the actual identifier and subject. Do not amend automatically to repair a mistake; amendment rewrites history and needs exact approval.

## Failure Recovery

For an empty commit, determine whether changes were already committed, never staged, ignored, or made in another worktree. Do not create an empty commit unless that is explicitly intended.

For a failed hook, preserve its output and identify the responsible check. For an index lock, inspect whether an operation is active before proposing cleanup. Do not delete lock files blindly or terminate another process.

## Verification

- The staged content matches the authorized change.
- Mixed staged and unstaged work was not silently combined or discarded.
- Commit identity, hooks, signing, and attribution remain correct.
- The resulting commit and remaining worktree state are reported truthfully.
