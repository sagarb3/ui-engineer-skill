# Git Tooling Examples

These scenarios use illustrative paths and branches. Inspect the actual repository before acting. The prompts authorize only the operations they name; they are not commands that this document has executed.

## Commit One Finished Change

**Use case:** A tested search-field repair is ready, but the working tree also contains an unrelated design draft.

```text
Use git-tooling. Commit only src/components/SearchField.tsx and its
matching test with the message "Fix search clear behavior". Leave the
unrelated design draft and all other changes untouched. Inspect any
pre-existing staged content before committing. Do not push.
```

**Expected deliverable:** One commit containing only the authorized change, with the unrelated draft preserved. If pre-existing staged work makes that separation unclear, the agent should ask rather than include or unstage it silently.

**Review:** Inspect the resulting commit's file list and staged diff, then check that the draft still exists with its original contents and state. The report should identify the actual commit and remaining worktree changes. A local commit must not be described as a remote push.

## Stop After a Rejected Push

**Use case:** A normal push is rejected because another contributor updated the remote branch.

```text
Use git-tooling. My normal push to the current upstream was rejected
because remote history changed. Inspect the branch relationship and
explain the next integration choice. Do not rebase, reset, merge, stash,
or force push until the intended strategy is clear.
```

**Expected deliverable:** Evidence about local and remote divergence and a concrete integration question if needed. Repeated pushes, a changed global pull policy, and an automatic force push are not acceptable substitutes for that decision.

**Review:** Local edits and published history should remain intact. Any proposed destructive action must name its target and consequences. A lease is a safeguard, not permission to overwrite history.

## Small Requests Stay Small

For `Use git-tooling. Show Git status.`, the expected behavior is simply to run status and report it. No feature planning, repository migration, or staging workflow is necessary.
