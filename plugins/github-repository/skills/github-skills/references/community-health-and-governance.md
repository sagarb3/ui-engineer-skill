# Community Health and Governance

## Contents

- Governance model
- Community health files
- Maintainer roles
- Contributor workflow
- Support and discussions
- CODEOWNERS
- Decision records
- Stale and inactive projects
- Governance checklist

## Governance Model

Define governance according to repository risk and contributor model. Use the lightest model that still answers:

- who can merge,
- who can release,
- who owns security response,
- who can change automation and deployment paths,
- how maintainers are added or removed,
- how disputes and breaking changes are decided,
- how an inactive project is archived or transferred.

For a small personal repository, one maintainer may own all responsibilities. For a multi-maintainer or organization repository, separate review, merge, release, and administration permissions when feasible.

## Community Health Files

Use repository-specific files when expectations differ by repository. Use an organization-wide `.github` public repository for default community health files only when the policy truly applies across repositories.

Recommended files by project type:

### Public open-source project

- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md` when support boundaries matter
- issue forms and pull request template

### Internal repository

- `README.md`
- ownership and escalation information
- contribution/development instructions
- security classification and incident route
- operational runbook when production-affecting

### Archived repository

- clear archived/deprecated notice
- replacement or migration link
- final supported version
- security and maintenance status

Do not create a community health file with fake contacts, placeholder legal text, or policies the maintainers will not follow.

## Maintainer Roles

Define roles such as:

- **Repository administrator** — settings, access, rulesets, integrations.
- **Maintainer** — issue triage, reviews, merges, release preparation.
- **Release manager** — tags, artifacts, package publication, rollback.
- **Security contact** — vulnerability intake, embargo, remediation coordination.
- **Code owner** — required subject-matter review for paths.
- **Contributor** — changes through documented workflow.

A role may be held by one person, but responsibilities must remain explicit.

## Contributor Workflow

A useful `CONTRIBUTING.md` should include:

1. supported contribution types,
2. issue-before-PR expectations,
3. local development setup,
4. test, lint, format, and build commands,
5. branch and commit expectations,
6. pull request requirements,
7. documentation and changelog requirements,
8. security reporting exception,
9. license or contributor agreement implications,
10. maintainer response expectations.

Avoid requiring issue approval for trivial fixes unless maintainers actually enforce it. Avoid asking contributors to run unavailable internal tooling.

## Support and Discussions

Separate channels by purpose:

- Issues: actionable defects and accepted work.
- Discussions: questions, proposals, showcases, open-ended design.
- Security channel: private vulnerability reports only.
- Support channel: usage help when maintainers commit to providing it.

Use `SUPPORT.md` to redirect non-bug requests and define response expectations. Do not promise service levels for a volunteer-maintained project unless they are sustainable.

## CODEOWNERS

Use CODEOWNERS to route review and optionally require owner approval through branch protection or rulesets.

Design principles:

- assign teams instead of individuals for organizational continuity,
- keep ownership patterns specific and understandable,
- include automation, security, release, and infrastructure paths,
- avoid a single catch-all owner when specialized review is required,
- verify owners have repository access,
- document escalation when an owner is unavailable.

Typical sensitive paths:

```text
/.github/workflows/
/.github/CODEOWNERS
/security/
/infrastructure/
/deploy/
/package publishing configuration
lockfiles and dependency policy files
```

CODEOWNERS does not replace repository permissions or rulesets.

## Decision Records

Use Architecture Decision Records or equivalent decision logs when choices affect long-term compatibility, security, or operations.

A compact ADR includes:

- status,
- context,
- decision,
- alternatives,
- consequences,
- date and owners.

Do not use issue comments as the only durable record for foundational decisions.

## Maintainer Continuity

Document:

- at least one backup administrator for organizational repositories,
- release credential ownership,
- package registry ownership,
- domain and deployment access,
- recovery codes or break-glass policy outside Git,
- transfer or archival criteria.

Never commit recovery material to the repository.

## Inactive and Deprecated Projects

When maintenance stops:

- update README status prominently,
- disable or redirect issue intake when appropriate,
- mark final supported version,
- archive the repository if no further changes are expected,
- preserve security reporting guidance if users remain exposed,
- link maintained alternatives without overstating compatibility.

## Governance Checklist

Verify:

- merge, release, admin, and security responsibilities are known,
- community files contain real and maintainable policies,
- issue and discussion channels have distinct purposes,
- sensitive paths have durable ownership,
- maintainer continuity is addressed,
- contributor setup is reproducible,
- project status is obvious to users.
