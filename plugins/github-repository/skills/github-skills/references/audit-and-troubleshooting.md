# Audit and Troubleshooting

## Contents

- Audit evidence model
- Audit domains
- Severity
- Remediation sequencing
- Actions failures
- Merge and ruleset failures
- Release failures
- Permission and API failures
- Repository drift
- Audit report format

## Audit Evidence Model

Separate findings into:

- **Observed** — directly visible in files, settings, logs, API responses, or repository metadata.
- **Inferred** — likely based on incomplete evidence.
- **Not observable** — requires plan, organization, or admin access.
- **Not applicable** — irrelevant to the repository type or threat model.

Never report a hosted setting as disabled when only repository files were inspected.

## Audit Domains

Review:

1. repository purpose and boundaries,
2. root structure and documentation,
3. community health and maintainer continuity,
4. issue and project workflow,
5. pull request and review policy,
6. branch protection and rulesets,
7. Actions architecture and security,
8. dependency and code security,
9. releases, tags, packages, and provenance,
10. permissions and external integrations,
11. archival, backup, and recovery.

## Severity

- Critical: direct compromise or unsafe privileged publication path.
- High: protection bypass, excessive privilege, untrusted code in privileged context.
- Medium: reliability, ownership, validation, or lifecycle gaps.
- Low: maintainability and discoverability weaknesses.
- Informational: optional improvement.

Severity must reflect repository context. Missing code scanning is not automatically Critical.

## Remediation Sequencing

Prioritize:

1. exposed or potentially compromised secrets,
2. privileged untrusted workflow execution,
3. unsafe release/deployment paths,
4. missing access and branch protections,
5. unreliable required checks,
6. dependency and scanning gaps,
7. governance and documentation,
8. cosmetic consistency.

Avoid enabling a required check before the workflow reports successfully.

## Actions Failure Diagnosis

Check:

1. event and filter matched,
2. workflow file exists on the expected branch,
3. YAML parses and `on` is valid,
4. permissions and secrets are available for the event,
5. runner label exists and is online,
6. action reference resolves,
7. runtime/toolchain version is supported,
8. cache or artifact assumptions hold,
9. job `if` conditions and `needs` results,
10. environment approval or protection,
11. rate limit or external service failure,
12. shell exit code and working directory.

Classify failures as configuration, code/test, infrastructure, external dependency, permission, or transient.

## Merge and Ruleset Failures

Verify exact required check names, ruleset target patterns, merge queue event support, review requirements, code owner matching, unresolved conversations, stale approvals, branch freshness, signed commit rules, and bypass permissions.

Do not disable the entire ruleset to fix one misnamed check.

## Release Failures

Check:

- version/tag mismatch,
- tag already exists,
- release event duplicated publication,
- package version already published,
- missing `contents` or `packages` permission,
- environment approval,
- registry/OIDC trust conditions,
- artifact names and paths,
- release job built a different commit,
- rerun idempotency.

Never overwrite published artifacts silently.

## Permission and API Failures

Distinguish:

- authentication failure,
- insufficient token scope,
- installation lacks repository access,
- organization policy denial,
- resource not found due to privacy,
- validation error,
- abuse/secondary rate limit,
- feature unavailable on current plan.

Do not respond to a 403 by automatically broadening token permissions.

## Repository Drift

Detect drift between:

- documented and actual branch names,
- README badges and workflows,
- required checks and job names,
- CODEOWNERS and active teams,
- release docs and real tags,
- supported versions and maintained branches,
- issue form labels and existing labels,
- Dependabot config and package ecosystems,
- local templates and organization defaults.

## Audit Report Format

For each finding include:

```text
ID
Severity
Domain
Evidence
Impact
Recommendation
Implementation type
Verification
Dependencies
```

End with:

- executive summary,
- risk distribution,
- quick wins,
- ordered remediation plan,
- blocked or unobservable checks,
- validation commands.
