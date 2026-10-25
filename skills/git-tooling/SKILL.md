---
name: git-tooling
description: Execute requested Git status, staging, commits, pulls, pushes, and branch switches directly; pause for unclear targets, destructive operations, or history rewriting.
---

# Git Tooling

## When to Use

Use for requested Git operations. A request to edit code alone does not authorize a push, publication, or history rewrite.

## Process

1. Run an obvious read-only request immediately: `git status`, `git diff`, or `git log`. Do not add an exploratory workflow to a simple command.
2. For an authorized mutation with clear targets, perform only the checks needed to protect current work, then execute. Stage named paths explicitly; before committing, inspect the staged diff so unrelated changes are excluded. Use a concise English message describing the actual change.
3. For an ordinary pull with no specified integration strategy, prefer `git pull --ff-only`. Respect an explicitly requested strategy. Stop on divergence or conflicts; do not silently rebase, reset, or stash user work.
4. Switch to a named existing branch without force when requested. Push normally when the branch and destination are clear. If multiple remotes, missing upstreams, or local changes make the request ambiguous, ask before choosing or changing anything.
5. Always ask before force pushes, hard resets, or deleting branches/files, including merged branches and untracked files. Also ask before other destructive actions or history rewriting, including amend and rebase. Show the exact command, target, and consequence. If approval already names that exact action and target, proceed without asking again.
6. Check the command's exit status and resulting Git state. On rejection or failure, report the cause and ask if the next action requires a choice. Do not bypass hooks, branch protections, or failed checks.

Generated code must contain no AI attribution. Keep all newly written content in English. Do not add authoring-tool names, parent-agent references, source-repository links, or generated-by/co-author trailers to commits or downstream files. Preserve existing legal notices.

## Choose the Path Without Over-analysis

| Request | Action | Stop condition |
| --- | --- | --- |
| Show status, diff, or recent commits | Run the requested read command | The repository itself is unclear |
| Stage named files | Stage those paths after checking their contents | Paths include unrelated or sensitive changes |
| Commit with a clear message | Check the staged content, then commit | The index includes unrelated work or hooks fail |
| Switch to a named existing branch | Switch without force | Local changes would be overwritten or carried unexpectedly |
| Pull the current branch | Use the requested strategy; otherwise fast-forward only | No upstream, divergence, or conflicts |
| Push the current branch | Use its clear upstream or explicitly named remote and branch | Destination is unclear or the push is rejected |
| Amend, rebase, force push, reset hard, or delete | Prepare an exact command and ask | Exact action and target lack explicit approval |

An explicit request to push a named branch is authorization for an ordinary push to its clear destination. It is not authorization to force push, publish tags, delete remote branches, or change repository settings.

## Staging and Committing

For a named implementation change, a typical sequence is:

```sh
git status --short
git diff -- src/components/SearchField.tsx
git add -- src/components/SearchField.tsx
git diff --cached
git commit -m "Fix search field clear behavior"
```

Adapt paths and message to the actual task; do not run examples literally. Inspect existing staged files before adding yours. Do not unstage another person's work without permission. If a file contains both requested and unrelated changes, use selected hunks only when the distinction is clear; otherwise ask how to separate them.

Review newly added files directly because ordinary `git diff` does not show untracked contents. Use `--` before path arguments. Do not stage credentials, local configuration, screenshots, build outputs, or dependencies merely because they are untracked. Follow the project's established commit convention when one exists, without adding attribution trailers.

Run the checks required for the commit. If hooks change files, inspect their changes and stage the intended results before retrying. If a hook fails, address the failure or report the blocker. Do not use `--no-verify`, disable signing, or change Git identity to bypass it.

## Branches, Pulls, and Pushes

When the current branch and upstream are already clear, avoid repeatedly inspecting every remote and branch. If destination evidence is missing, `git branch -vv` and `git remote -v` can resolve it. Never print credential-bearing URLs unredacted in a report.

Use `git switch existing-branch` for a requested existing branch, or the supported project equivalent. If switching carries local changes, ensure that matches the user's intent; ask when the placement of those changes is unclear. Do not automatically stash, reset, or create a new branch to make switching succeed.

For a normal pull with no specified strategy, `git pull --ff-only` avoids silently choosing merge versus rebase. A divergence means the integration policy needs a decision. Explain that local and remote histories differ and ask which policy to use. Do not transform a failed fast-forward into an automatic rebase.

For a push, check whether the destination matches the requested repository and branch. A missing upstream is not an excuse to choose `origin/main`. If the user explicitly requests publishing `feature/search` to `origin`, `git push -u origin feature/search` is concrete and appropriate. Do not use `--all`, `--mirror`, or tag publication for a single-branch request.

## Conflicts and In-progress Operations

Read the conflict and both sides before editing. Preserve both intended behaviors where compatible. Ask when the conflict represents a product decision, a deletion, or incompatible API contracts. Do not resolve all files with `--ours` or `--theirs` as a shortcut.

Check `git status` for an operation already in progress. Do not start a second merge or rebase. Continue or abort only within the authorized operation and when the effect on existing work is understood. After resolving conflicts, inspect the staged resolution, run relevant checks, and continue the same operation.

If a command fails, distinguish authentication, network failure, rejected history, missing refs, and hook failure. A retry is reasonable for a transient transport failure once its effects are known. Repeatedly pushing does not fix a history rejection, and changing global configuration does not resolve an unclear destination.

## Destructive-action Approval

Approval must identify what will be affected. "May I clean up?" is insufficient. A useful request names the command, branch or paths, destination if remote, and possible loss. Read-only inspection or `git clean -nd` may establish the affected files before asking; a preview does not authorize deletion.

Require approval for `git push --force`, `--force-with-lease`, `git reset --hard`, branch deletion, file deletion, and commands that overwrite or discard edits. Treat `git restore` and path checkout as destructive when they discard user changes. A request to remove a named branch is already exact approval for that deletion; do not ask again unless the consequences differ from what was requested.

If an approved history rewrite needs a remote update, use the narrowest suitable safeguard, such as an explicit lease against the expected remote commit. Re-check the target immediately before acting. If remote state has changed, stop rather than weaken the safeguard. Never treat a recovery ref or reflog as permission to destroy work.

## Completion Evidence

Report the resulting branch and relevant state. For a commit, include its short identifier and subject; for a push, identify the destination and whether it succeeded. A successful local commit is not a successful push. Leave the worktree exactly as the task requires; do not manufacture a clean status by deleting unrelated files.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Branches and Remotes](guides/branches-and-remotes.md) | Read when branch identity, worktrees, upstreams, pulls, or push destinations need resolution. |
| [Conflicts and History](guides/conflicts-and-history.md) | Read for merge conflicts, rebase or amendment requests, destructive cleanup, and failed history updates. |
| [Index and Commits](guides/index-and-commits.md) | Read for staging, selective commits, pre-existing index content, and hook failures. A simple status request still needs only the requested command. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Anti-patterns / Red Flags

- Using `git add .` without knowing what it includes, or committing pre-existing staged changes unintentionally.
- Retrying a rejected push with force, or treating `--force-with-lease` as exempt from approval.
- Using checkout, restore, clean, or reset to discard changes without approval.
- Changing remotes, Git identity, signing, hooks, or global configuration to make a command succeed.

## Verification Criteria

- The requested command succeeded against the intended repository, paths, branch, and remote.
- Only intended changes were staged or committed; unrelated work remains intact.
- Required approvals were obtained before destructive actions or history rewriting.
- The reported outcome matches the command result and contains no attribution fingerprints.
