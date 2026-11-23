# GitHub Actions Security

## Contents

- Threat model
- Token permissions
- Action pinning
- Untrusted input and script injection
- Pull request trust boundaries
- Secrets
- OIDC
- Runners
- Artifacts and caches
- Release security
- Security review checklist

## Threat Model

A GitHub Actions workflow can access repository content, tokens, secrets, packages, cloud systems, deployment environments, and release channels. Treat workflow files as privileged code.

Primary risks:

- malicious or compromised third-party actions,
- excessive `GITHUB_TOKEN` permissions,
- script injection from event context,
- privileged execution of untrusted pull request code,
- secret leakage through logs or artifacts,
- poisoned caches or artifacts,
- compromised self-hosted runners,
- unsafe package or release publication,
- reusable workflow privilege confusion.

## Token Permissions

Set top-level permissions to read-only or empty and grant additional scopes per job.

```yaml
permissions:
  contents: read
```

For a release job, grant only the required write scopes. Do not use a personal access token when `GITHUB_TOKEN` or a GitHub App token is sufficient.

Understand that token permissions can differ by event, repository settings, fork status, and organization policy.

## Action Pinning

For high-assurance workflows, pin third-party actions to a full commit SHA. A tag or branch can move; a full commit SHA is immutable in normal Git object semantics.

Document:

- the human-readable release corresponding to the SHA,
- how updates are reviewed,
- whether Dependabot or another tool updates action references.

Review action source and publisher trust. Prefer minimal actions with narrow responsibility.

## Untrusted Input and Script Injection

Treat these as untrusted:

- issue and pull request titles and bodies,
- comments and review text,
- branch and tag names,
- commit messages,
- actor-controlled labels,
- external webhook/API payloads,
- file contents from a pull request.

Do not interpolate untrusted context directly into `run` scripts.

Unsafe pattern:

```yaml
run: echo "${{ github.event.pull_request.title }}"
```

Safer pattern:

```yaml
env:
  PR_TITLE: ${{ github.event.pull_request.title }}
run: printf '%s\n' "$PR_TITLE"
```

Environment variables reduce expression-to-script injection, but the called program must still handle arbitrary input safely.

Prefer structured action inputs or scripts that receive data through files or environment variables.

## Pull Request Trust Boundaries

### `pull_request`

Use for testing untrusted proposed changes. Secrets are not normally passed to forked pull request workflows. Keep token permissions read-only.

### `pull_request_target`

Runs in the base repository context and may have access to privileged tokens or secrets. Never combine it with checkout and execution of untrusted pull request code.

Safe uses may include labeling or commenting based on validated metadata without executing contributor code.

### Fork approval

Review first-time contributor workflow runs before approval. Approval is not a substitute for secure workflow design.

## Checkout Behavior

Understand which ref is checked out. For pull request validation, the default may be a merge commit. If checking out contributor head explicitly, preserve the untrusted-code boundary.

Disable credential persistence when subsequent Git operations do not require it:

```yaml
with:
  persist-credentials: false
```

Do not use a write-capable token in a checkout step that executes untrusted code.

## Secrets

- Store secrets in repository, environment, or organization secret stores according to scope.
- Use environment secrets for protected deployments.
- Never print, transform, or serialize secrets into logs.
- Avoid passing secrets as command-line arguments visible to process listings.
- Do not upload secrets in artifacts or caches.
- Rotate credentials after suspected exposure.
- Prefer short-lived credentials.

Secret masking is not a guarantee. Derived or encoded values may not be masked automatically.

## OIDC

Use OpenID Connect federation when a cloud or external provider supports it. OIDC avoids long-lived cloud credentials stored in GitHub.

A secure OIDC design includes:

- `id-token: write` only on the deployment job,
- restrictive provider trust conditions,
- repository, branch, tag, workflow, and environment claims as appropriate,
- protected GitHub environments,
- short session duration,
- provider-side least privilege.

## Self-Hosted Runners

Treat self-hosted runners as persistent infrastructure unless proven ephemeral and isolated.

Risks include:

- secret or token persistence,
- cross-job contamination,
- access to internal networks,
- compromised toolchains,
- untrusted pull request code.

Do not run public fork pull requests on privileged self-hosted runners. Prefer ephemeral runners, isolated networks, immutable images, and automatic cleanup.

## Artifacts and Caches

Do not trust artifacts or caches solely because GitHub stored them. Validate producer identity and integrity before using them in privileged release or deployment jobs.

Avoid workflows where an untrusted job uploads an artifact that a privileged workflow later executes.

Use separate trusted builds for releases.

## Reusable Workflows

Define explicit inputs and secrets. Permissions in nested reusable workflows can remain the same or be reduced, not safely assumed to increase.

Pin external reusable workflow references. Review inherited secrets carefully; prefer named secrets over `secrets: inherit` when practical.

## Release Security

- Build release artifacts from a trusted ref.
- Prevent unreviewed workflow changes from controlling publication.
- Separate build, signing, and publishing when risk warrants it.
- Generate checksums and provenance.
- Use immutable releases or protected tags when supported and appropriate.
- Verify package registry ownership and token scope.
- Test that reruns cannot publish conflicting artifacts.

## Security Review Checklist

Reject a production workflow if:

- it lacks explicit permissions,
- it executes untrusted code with secrets or write tokens,
- it interpolates untrusted event data into shell,
- it uses mutable third-party references without an accepted policy,
- it publishes from an untrusted or ambiguous ref,
- it exposes environment secrets to validation jobs,
- it uses privileged self-hosted runners for public pull requests,
- it has no timeout or failure recovery for external operations,
- it can publish duplicate or mismatched artifacts on rerun.
