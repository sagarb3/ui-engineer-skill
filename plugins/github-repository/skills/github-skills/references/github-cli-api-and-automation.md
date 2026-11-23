# GitHub CLI, API, and Automation

## Contents

- Choosing CLI, REST, GraphQL, Apps, or Actions
- Authentication
- Safe command planning
- Idempotency
- Pagination and rate limits
- Webhooks
- GitHub Apps
- Auditability
- Common patterns

## Choosing the Interface

Use GitHub CLI when a human or agent is operating interactively on repositories, issues, pull requests, releases, Actions, and API endpoints.

Use the REST API for resource-oriented operations with stable endpoint semantics.

Use GraphQL when one query must retrieve connected data or when reducing request count materially improves the workflow.

Use a GitHub App for production integrations that need installation-scoped permissions, webhook delivery, short-lived tokens, and auditable access.

Use GitHub Actions for repository-native event automation, not as a general substitute for an external service that requires durable state or continuous execution.

## Authentication

Prefer:

- `GITHUB_TOKEN` inside Actions for repository-scoped operations,
- GitHub App installation tokens for production integrations,
- fine-grained personal access tokens only when user-scoped automation is truly required,
- OIDC for external cloud authentication.

Never embed tokens in commands, workflow files, URLs, logs, or generated examples. Reference environment variables or secret names.

## Safe CLI Planning

Before a write command:

1. identify repository and authenticated account,
2. read current state,
3. show intended change,
4. avoid destructive defaults,
5. verify result.

Use `--repo OWNER/REPO` when current-directory ambiguity is possible.

Prefer machine-readable output:

```bash
gh pr list --json number,title,state,headRefName,baseRefName
```

Use `gh api` for settings not covered by high-level commands. Preserve request and response evidence without storing tokens.

## Idempotency

Automation should safely rerun.

Patterns:

- fetch before create,
- update by stable identifier,
- use deterministic names,
- compare desired and current state,
- skip unchanged resources,
- use conditional requests where supported,
- record external operation IDs,
- treat duplicate release/package publication as a controlled error.

Do not create duplicate labels, milestones, releases, webhooks, or comments on every run.

## Pagination and Rate Limits

Handle pagination explicitly. Do not assume one page contains all repositories, issues, workflow runs, or releases.

Respect primary and secondary rate limits. Use conditional requests, caching, GraphQL batching, and backoff. Do not retry authorization or validation errors as if they were transient.

## Webhooks

For GitHub webhooks:

- validate the signature,
- use the raw request body for validation,
- reject stale or malformed payloads,
- record delivery ID for deduplication,
- acknowledge quickly and process asynchronously when work is slow,
- handle redelivery idempotently,
- log event type and delivery ID without sensitive payloads,
- rotate webhook secrets safely.

Do not trust repository, sender, branch, or action fields without validation against the integration's authorization model.

## GitHub Apps

Design permissions from required operations. Separate repository permissions from organization permissions. Subscribe only to required events.

Use installation IDs and short-lived installation tokens. Store private keys in a dedicated secret manager. Plan key rotation.

## Auditability

For automation changes, capture:

- actor or app identity,
- repository,
- operation,
- old and new state when feasible,
- timestamp,
- external request/delivery ID,
- result and retry classification.

Avoid logging issue bodies, secret values, or private repository content unless required and protected.

## Common Patterns

### Repository bootstrap

1. create repository,
2. set description/topics/visibility,
3. push initial files,
4. create labels,
5. configure Actions permissions,
6. enable security features,
7. create ruleset after checks exist,
8. verify contributor flow.

### Bulk governance rollout

1. inventory repositories,
2. classify exceptions,
3. dry-run desired state,
4. apply low-risk file changes through pull requests,
5. apply settings in batches,
6. verify ruleset and workflow compatibility,
7. record exceptions and owners.

### Release automation

Use a deterministic version, trusted ref, least-privilege token, idempotent package publication, and post-publish verification.
