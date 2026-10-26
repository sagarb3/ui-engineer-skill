# Branches and Remotes

Read when branch identity, worktrees, upstreams, pulls, or push destinations need resolution.

## Resolve Only Missing Facts

Run an obvious requested command directly. Inspect branch tracking or remotes only when they affect safe execution. A configured upstream can answer where a normal push goes; it does not authorize publishing additional branches or tags.

In a detached state, do not guess which branch should receive new commits. In a repository with several remotes, distinguish the source of incoming changes from the intended publication destination. Redact credential-bearing remote URLs in reports.

Check worktree constraints when switching branches. A branch already checked out elsewhere should not be forced into the current worktree. Do not modify the other worktree to make the switch succeed.

## Preserve Local Changes

Switch without force to a requested existing branch. If Git would carry local edits onto the target branch and their intended home is unclear, ask before switching. If the switch would overwrite edits, stop; do not automatically stash, restore, or reset.

A stash is a mutation of the user's working state, not a neutral read. Use it only when requested or clearly authorized. If a stash operation is authorized, preserve its identity and verify restoration instead of assuming a clean exit means no work was lost.

## Integrate Incoming History

Use the explicitly requested integration strategy. Otherwise prefer fast-forward-only for an ordinary pull so divergence does not silently select merge or rebase. A rejected fast-forward requires a history decision, not an automatic fallback.

Check for an existing operation before starting another. Conflicts, missing upstreams, authentication failure, and transport failure require different responses. Do not modify global pull policy or credentials merely to avoid asking about the actual problem.

## Push Narrowly

Verify the intended repository, branch, and destination. Publishing a named new branch can use a corresponding explicit upstream when authorized. Do not infer that an absent upstream means `origin/main`.

For a single-branch request, avoid `--all`, `--mirror`, tag publication, or deletion refspecs. Do not convert a rejected push into a force push. Confirm whether a failure occurred before or after the remote accepted the update before retrying consequential actions.

If remote state changed after a proposed rewrite, stop and re-evaluate the exact approval and lease conditions. Never weaken a lease or branch protection to make an old plan succeed.

## Verification

- Current branch and worktree are the intended ones.
- Local edits and other worktrees remain intact.
- Pull behavior matches the authorized history strategy.
- Pushes affect only the named destination and requested refs.
- A successful local operation is not misreported as remote publication.
