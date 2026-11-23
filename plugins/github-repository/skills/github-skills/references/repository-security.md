# Repository Security

## Contents

- Security baseline
- Access and permissions
- Security policy and reporting
- Secret scanning
- Dependency security
- Code scanning
- Branch and tag protection
- Supply chain
- Sensitive data
- Incident response
- Security checklist

## Security Baseline

For a public repository, evaluate at minimum:

- Dependabot alerts,
- secret scanning,
- push protection,
- code scanning or equivalent static analysis,
- `SECURITY.md`,
- private vulnerability reporting where available,
- protected default branch or ruleset,
- Actions least privilege.

Feature availability depends on repository visibility, organization policy, and GitHub plan. Do not claim a feature is enabled without observing it.

## Access and Permissions

Apply least privilege:

- prefer teams over direct individual access in organizations,
- separate admin, maintain, write, triage, and read roles,
- review outside collaborators,
- remove inactive access,
- require strong account security through organization policy,
- restrict bypass permissions.

Repository write access includes the ability to modify workflow files, which may create a path to secrets and deployments. Protect sensitive paths with review requirements.

## SECURITY.md

A real security policy should include:

- supported versions,
- private reporting method,
- information reporters should provide,
- expected acknowledgement process,
- disclosure coordination expectations,
- safe-harbor language only when approved,
- public issue prohibition for vulnerability details.

Do not put a personal email address into a generated policy unless the user provides it.

## Private Vulnerability Reporting

Enable private vulnerability reporting when appropriate for public repositories. Define who monitors reports and who can coordinate advisories.

Do not rely on a public issue template to redirect vulnerabilities after details are already exposed.

## Secret Scanning and Push Protection

Enable supported scanning and push protection. Treat an alert as potential compromise, not only a file cleanup task.

Response:

1. revoke or rotate the credential,
2. assess logs and usage,
3. remove the secret from current files,
4. rewrite history only when necessary and coordinated,
5. invalidate caches and artifacts if exposed,
6. document the incident.

Removing a secret from the latest commit does not revoke it.

## Dependency Security

Use:

- dependency graph,
- Dependabot alerts,
- automated security updates,
- version update configuration,
- dependency review in pull requests when available,
- lockfiles,
- package integrity controls.

Review dependency updates according to risk. A green test suite does not prove a dependency is trustworthy.

## Code Scanning

Configure language-appropriate analysis. Ensure scans run on relevant branches and pull requests. Define how alerts are triaged, dismissed, and tracked.

Do not dismiss findings without reason and owner. Tune noisy rules rather than ignoring the entire signal.

## Branch, Tag, and Release Protection

Protect:

- default branch,
- release branches,
- release tag patterns,
- workflow and release configuration paths.

Require trusted checks and reviews for code that can publish packages, create releases, or deploy.

## Supply-Chain Controls

Consider:

- pinned workflow dependencies,
- dependency review,
- artifact attestations,
- signed tags or releases,
- reproducible builds,
- isolated release jobs,
- trusted publishing,
- checksums,
- provenance verification instructions.

## Sensitive Data

Do not store:

- production secrets,
- customer data,
- access logs with personal data,
- private keys,
- credentials in examples,
- internal hostnames in public repos when sensitive,
- proprietary documents in public history.

Use sample data that cannot be confused with real data.

## Security Ownership

Assign owners for:

- vulnerability intake,
- dependency alerts,
- code scanning alerts,
- workflow security,
- release credentials,
- incident communications.

## Incident Response

Maintain a concise runbook:

- containment,
- credential rotation,
- workflow disabling,
- release/package suspension,
- forensic preservation,
- impact assessment,
- user notification,
- remediation and postmortem.

## Security Checklist

Verify:

- write access is limited,
- default branch and release paths are protected,
- secrets cannot reach untrusted workflows,
- security alerts have owners,
- vulnerability reporting is private and monitored,
- package and release identities are least privilege,
- workflow dependencies have an update policy,
- incident response includes credential rotation and publication controls.
