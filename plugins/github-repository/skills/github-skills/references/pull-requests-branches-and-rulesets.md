# Pull Requests, Branches, and Rulesets

## Contents

- Branching strategy
- Pull request contract
- Review policy
- Merge methods
- CODEOWNERS
- Rulesets and protection
- Required checks
- Merge queue
- Automation and bots
- Troubleshooting

## Branching Strategy

Prefer short-lived branches from the default branch for most repositories. Use long-lived release branches only when the support policy requires parallel maintenance.

Common models:

- **Trunk-based**: small pull requests, frequent integration, feature flags for incomplete work.
- **GitHub flow**: branch, pull request, review, checks, merge, deploy.
- **Release branches**: maintain supported versions with explicit backport policy.

Avoid Git Flow complexity unless staged release branches and hotfix branches solve a real operational need.

## Pull Request Contract

A pull request should explain:

- problem and intent,
- scope and non-goals,
- implementation summary,
- test evidence,
- user-facing or operational impact,
- migration or rollback needs,
- linked issues or decisions,
- screenshots or logs when relevant,
- security impact for sensitive changes.

Keep templates concise. Use checkboxes only for requirements maintainers enforce.

## Pull Request Size

Prefer reviewable changes. Split unrelated refactors, dependency updates, generated output, and behavior changes when practical. A large pull request must include a review map and sequencing notes.

Do not split changes so aggressively that intermediate commits are invalid or reviewers cannot understand the outcome.

## Review Policy

Define:

- minimum approvals,
- required owner review paths,
- self-approval rules,
- stale approval behavior after new commits,
- review turnaround expectations,
- emergency bypass process,
- who resolves conflicting reviews.

Require stronger review for:

- workflow and release automation,
- dependency policy,
- authentication and authorization,
- deployment and infrastructure,
- secrets and cryptography,
- schema migrations,
- public API breaking changes.

## Merge Methods

### Squash merge

Good for contributor-facing repositories and a concise default-branch history. Ensure pull request title and final message meet changelog and attribution needs.

### Merge commit

Useful when preserving branch topology or grouped commits matters. Can make history noisier.

### Rebase merge

Maintains linear history while retaining commits, but rewrites contributor commit IDs and requires disciplined commits.

Select one primary method and document exceptions.

## CODEOWNERS

Store `CODEOWNERS` in `.github/`, repository root, or `docs/`; prefer `.github/CODEOWNERS` for discoverability.

Order matters because the last matching pattern wins. Test overlapping rules. Keep comments explaining non-obvious ownership boundaries.

A CODEOWNERS file only requests review. Enforce owner approval through branch protection or rulesets when required.

## Rulesets and Branch Protection

Prefer rulesets when centralized, layered, or organization-visible policy is needed. Use branch protection for simpler repository-specific requirements where appropriate.

A baseline default-branch policy may require:

- pull request before merge,
- one or more approvals,
- required status checks,
- conversation resolution,
- no force pushes,
- no deletion,
- linear history when selected,
- signed commits when threat model and contributor experience justify it,
- code owner review for sensitive paths.

Keep bypass actors minimal and auditable. Do not grant broad bypass to automation unless required.

## Required Status Checks

Only require checks that:

- exist,
- run on the relevant pull request events,
- report consistently,
- are not skipped by normal path filters,
- complete within an acceptable time,
- have clear failure remediation.

Create and run workflows before enforcing their check names. Renaming jobs or workflows can break merge requirements.

Use separate required checks for independent gates such as tests, lint, policy, and security when reviewers need distinct failure signals.

## Merge Queue

Use a merge queue when:

- default branch changes frequently,
- checks are expensive,
- pull requests often become stale before merge,
- required checks must validate the exact queued combination.

Ensure workflows handle the `merge_group` event when GitHub requires it. Do not enable a merge queue without verifying all required checks run for queued changes.

## Dependabot and Bot Pull Requests

Treat bot changes as untrusted until checks pass. Require review for major upgrades, build-system changes, workflow dependencies, and packages with install scripts.

Do not grant broad write tokens to pull request workflows solely to support a bot.

## Emergency Changes

Define a break-glass process:

- named authorized roles,
- reason captured in issue or incident record,
- minimum validation,
- post-change review,
- restoration of bypassed protections,
- credential rotation if exposure is possible.

## Troubleshooting Merge Blocks

Check in order:

1. target branch and ruleset scope,
2. required checks and exact check names,
3. event coverage including merge queue,
4. approval count and code owner requirements,
5. stale approvals after new commits,
6. unresolved conversations,
7. branch update requirement,
8. commit signature or linear-history rules,
9. bypass actor eligibility,
10. conflicting organization rulesets.

Never disable protections as the first troubleshooting step.
