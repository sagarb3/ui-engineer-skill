# GitHub Actions Design

## Contents

- Workflow boundaries
- Event selection
- Permissions
- Jobs and steps
- Reusable workflows
- Matrix strategies
- Caching and artifacts
- Concurrency
- Environments and deployment
- Observability
- Cost and performance
- Design checklist

## Workflow Boundaries

Create one workflow for one operational responsibility. Common boundaries:

- pull request validation,
- default branch validation,
- scheduled maintenance,
- release preparation,
- artifact publication,
- deployment,
- security scanning,
- repository automation.

Do not combine unrelated responsibilities only to reduce the number of YAML files. Avoid one workflow per trivial command when the commands share lifecycle and permissions.

## Event Selection

Choose the narrowest event that matches intent.

### `pull_request`

Use for validating proposed changes without granting access to protected secrets from untrusted forks.

### `push`

Use for branch or tag integration after code is accepted. Filter branches, tags, and paths carefully.

### `workflow_dispatch`

Use for explicit operator-controlled execution. Define typed inputs and safe defaults.

### `workflow_call`

Use to expose a stable reusable workflow interface.

### `schedule`

Use for maintenance that can tolerate delayed execution. Scheduled workflows run from the default branch and may be delayed during high load.

### `release`

Use when a GitHub Release lifecycle event is the source of truth. Avoid duplicate publication from both tag and release events unless idempotency is built in.

### `pull_request_target`

Treat as privileged. It executes in the base repository context. Do not check out and execute untrusted pull request code with privileged credentials.

## Trigger Filters

Use branch, tag, and path filters to reduce irrelevant runs, but verify required checks are not left permanently pending when a workflow is skipped.

Document whether a workflow is expected on:

- pull requests from forks,
- draft pull requests,
- merge queue groups,
- tags,
- maintenance branches,
- manual dispatch.

## Permissions

Set explicit least-privilege `permissions`. A validation workflow usually needs only:

```yaml
permissions:
  contents: read
```

Add scopes only to the job that needs them. Common write permissions:

- `contents: write` for releases or repository commits,
- `packages: write` for package publication,
- `pull-requests: write` for PR comments or labels,
- `issues: write` for issue automation,
- `id-token: write` for OIDC federation,
- `attestations: write` for artifact attestations.

Never use `write-all` as a convenience.

## Jobs and Steps

Each job should have:

- descriptive ID and display name,
- explicit `runs-on`,
- least-privilege permissions,
- timeout,
- clear dependencies with `needs`,
- deterministic setup,
- actionable failure output.

Keep shell scripts in repository files when they are long, reused, or need independent tests. Inline shell is appropriate for short, transparent commands.

Use `set -euo pipefail` or shell-equivalent strict behavior when appropriate, but understand tool-specific exit semantics.

## Reusable Workflows

Use reusable workflows when:

- multiple repositories or workflows repeat the same multi-job logic,
- the inputs and outputs are stable,
- permission and secret boundaries can be clearly defined,
- central maintenance creates real value.

Reusable workflows must be in `.github/workflows` and use `workflow_call`. Define typed inputs, explicit secrets, outputs, and documented permissions.

Prefer full commit SHA references for external reusable workflows in high-assurance contexts. Local reusable workflows execute from the same commit as the caller.

Do not create deeply nested reusable workflow chains. Keep permission reduction and secret propagation understandable.

## Composite Actions

Use a composite action for reusable step sequences that run within a job. Use a reusable workflow for reusable jobs, runners, permissions, environments, and matrices.

## Matrix Strategies

Use matrices for supported combinations such as runtime versions, operating systems, or packages.

Control explosion:

- include only supported combinations,
- use `include` and `exclude`,
- define `fail-fast` intentionally,
- set `max-parallel` when external services or cost require it.

Do not test combinations the project does not support merely because they are easy to enumerate.

## Dependency Caching

Cache dependency download data, not build outputs that must be trusted as release artifacts.

A cache key should include:

- operating system,
- runtime or toolchain version when relevant,
- dependency lockfile hash,
- architecture when relevant.

Use restore keys carefully; a broad fallback can introduce stale or incompatible content.

## Artifacts

Artifacts are for passing or retaining workflow outputs such as test reports, binaries, coverage, and logs.

Define:

- artifact name,
- producer and consumer,
- retention period,
- integrity expectations,
- whether the artifact is publishable.

Do not publish artifacts built from untrusted code without a trusted rebuild or review gate.

## Concurrency

Use concurrency to prevent obsolete or conflicting runs.

For pull request validation, cancel superseded runs by branch or PR. For deployments, serialize by environment and normally do not cancel an active production deployment unless the rollout system supports it safely.

Example pattern:

```yaml
concurrency:
  group: ci-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## Environments and Deployment

Use GitHub environments for deployment boundaries such as `staging` and `production`.

Configure:

- allowed branches or tags,
- required reviewers,
- wait timers if needed,
- environment-scoped secrets and variables,
- deployment URL,
- concurrency or external lock,
- rollback workflow.

Prefer OIDC for cloud authentication. Avoid sharing production credentials with build or test jobs.

## Outputs and Data Flow

Use job outputs for small structured values. Use artifacts for files. Avoid transmitting secrets through outputs, logs, artifacts, caches, or pull request comments.

Validate external JSON before passing it between jobs.

## Observability

A workflow should make failures diagnosable. Include:

- clear step names,
- concise summaries through `$GITHUB_STEP_SUMMARY`,
- test reports when supported,
- artifact links,
- deployment URLs,
- failure notifications only where actionable,
- debug procedure that does not reveal secrets.

## Cost and Performance

Reduce cost without weakening confidence:

- cancel superseded PR runs,
- use path filters for independent areas,
- split fast required checks from slow optional checks,
- cache deterministic dependencies,
- use affected-package testing in monorepos,
- avoid repeated setup through reusable workflows or composite actions,
- set timeouts.

## Design Checklist

Verify:

- events match the trust model,
- permissions are explicit and minimal,
- required checks always report for protected changes,
- third-party actions have a version and update policy,
- untrusted input never reaches privileged shell execution,
- jobs have timeouts,
- deployment credentials are isolated,
- artifacts and caches have distinct purposes,
- concurrency prevents unsafe overlap,
- failures have a documented recovery path.
