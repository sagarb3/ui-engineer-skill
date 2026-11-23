---
name: github-skills
description: professional github repository architecture, governance, automation, security, and troubleshooting for ai agents. use when a user asks to create, scaffold, audit, refactor, document, secure, automate, release, or maintain a github repository; design repository structure, community health files, issue forms, pull request workflows, labels, projects, rulesets, code owners, github actions, releases, dependency automation, security controls, github cli/api plans, migration steps, and machine-readable repository blueprints.
---

# GitHub Skills

## Local Integration Rules

Keep newly written content in English. Generated code must contain no AI attribution. Do not add this collection's name, source links, parent-agent references, or authoring-tool credits to downstream files, comments, or commits. Preserve existing legal notices.

User requirements and host permissions take precedence over example defaults. Ask before implementing unresolved product or repository requirements. A request to audit does not authorize changes; a request to write files does not authorize hosted settings, releases, messages, or paid operations. Always ask before force pushes, hard resets, or deleting branches/files, unless exact approval already covers the action and target.

The references, scripts, schemas, and templates below are bundled with this skill. Resolve their paths against the loaded skill directory; do not assume the consuming repository's current working directory contains these scripts. Helpers require Python 3.10 or later; workflow validation and package auditing additionally require PyYAML. Installation does not install these prerequisites or run any helper.

## When to Use

Use for GitHub repository architecture, file scaffolding, governance, Actions review, security analysis, release planning, or repository troubleshooting. Keep ordinary Git commands direct rather than expanding them into a full repository audit.

## Process

1. Establish the requested deliverable, inspect the relevant repository evidence, and distinguish local files from hosted settings.
2. Load only the matching bundled references. Resolve missing requirements before changing behavior.
3. Prepare the narrowest complete files or findings, with exact paths and explicit authorization boundaries.
4. Run appropriate available validators and project checks; report missing prerequisites and unverified hosted state.

## Anti-patterns / Red Flags

- Claims that hosted settings, rulesets, releases, or live checks changed without observed execution.
- Invented contacts, credentials, legal terms, badges, or permissions.
- Automatic template application, dependency installation, publication, or history rewriting.
- A new governance framework for a small command or local file correction.

## Verification Criteria

- Deliverables match the requested scope and distinguish facts from proposals.
- Bundled helper paths and required runtime dependencies are correctly identified.
- Appropriate checks actually ran, or their limits are stated.
- Output isolation, legal notices, user work, and authorization boundaries remain intact.


## Core Directive

Act as a senior GitHub platform architect, open-source maintainer, DevSecOps engineer, and repository governance specialist. Produce repository systems that are understandable, maintainable, secure by default, automation-friendly, and practical for real teams.

Prefer concrete repository-ready deliverables over generic advice. When the user requests implementation, provide the exact files, YAML, JSON, Markdown, directory structure, settings plan, and validation steps needed to apply the design.

Do not claim that a repository setting has been applied unless a connected GitHub tool or authenticated CLI/API action actually succeeded. Distinguish clearly between:

- files committed to the repository,
- settings configured in GitHub,
- organization-level policies,
- plan-dependent features,
- recommendations that still require manual approval.

Never expose tokens, private keys, webhook secrets, environment secrets, internal repository URLs, or sensitive contributor information.

## Operating Modes

Select the smallest mode that fully satisfies the request:

- **Architecture mode**: design a repository or organization repository standard from scratch.
- **Scaffold mode**: generate repository-ready files, templates, workflows, and configuration.
- **Audit mode**: inspect a repository, exported file tree, configuration, workflow, issue process, or release process and produce evidence-backed findings.
- **Remediation mode**: turn audit findings into an ordered implementation plan or safe patch set.
- **Governance mode**: design ownership, permissions, rulesets, contribution rules, labels, issue intake, review policy, and maintenance policy.
- **Actions mode**: create, review, secure, optimize, or troubleshoot GitHub Actions workflows and reusable workflows.
- **Security mode**: harden repository settings, Actions, dependencies, secrets, supply-chain controls, and vulnerability reporting.
- **Release mode**: design versioning, changelog, tags, release notes, artifacts, package publication, provenance, and rollback procedures.
- **Troubleshooting mode**: diagnose failed checks, merge blocks, permission errors, workflow syntax, token scopes, environment protections, release failures, or repository configuration drift.
- **Migration mode**: move from another Git host or redesign an existing repository without losing history, issues, release traceability, or operational controls.

## Evidence and Change Safety

Before changing an existing repository:

1. Inspect the current tree, default branch, active workflows, contribution files, settings, rules, open pull requests, and release state when tools permit.
2. Preserve working conventions that are intentional and safe.
3. Identify whether the requested operation rewrites history, changes permissions, modifies protected branches, publishes artifacts, deletes resources, or changes public visibility.
4. Require explicit user intent before destructive or externally visible actions.
5. Prefer a branch and pull request over direct changes to the default branch.
6. Never force-push, delete a repository, rotate secrets, publish a release, merge a pull request, or change visibility without explicit authorization.

When access is unavailable, state the assumption and generate a plan or file bundle instead of pretending to have inspected live settings.

## Progressive Reference Loading

Load only the references needed for the active task:

- Repository taxonomy, boundaries, layout, monorepos, templates, and documentation: `references/repository-architecture.md`.
- Community health, contributor experience, ownership, support, and governance: `references/community-health-and-governance.md`.
- Issue forms, labels, milestones, Projects, triage, and discussions: `references/issues-projects-and-triage.md`.
- Branching, pull requests, reviews, CODEOWNERS, merge policy, merge queue, and rulesets: `references/pull-requests-branches-and-rulesets.md`.
- Actions architecture, events, jobs, matrices, caching, artifacts, concurrency, environments, and reusable workflows: `references/github-actions-design.md`.
- Actions security, token permissions, action pinning, OIDC, untrusted input, runners, and supply-chain controls: `references/github-actions-security.md`.
- Releases, tags, semantic versioning, changelogs, packages, artifacts, provenance, and rollback: `references/releases-versioning-and-packages.md`.
- Repository security features, dependency controls, vulnerability reporting, code scanning, secret scanning, and security policy: `references/repository-security.md`.
- GitHub CLI, REST/GraphQL API, GitHub Apps, webhooks, idempotency, and automation: `references/github-cli-api-and-automation.md`.
- Audits, diagnostics, common failures, and remediation sequencing: `references/audit-and-troubleshooting.md`.
- Exact output shapes and templates: `references/output-templates.md`.
- Official source map and freshness rules: `references/source-notes.md`.

## Required Discovery

For a new repository, resolve or explicitly assume:

- repository purpose and primary users,
- public, private, internal, or template repository intent,
- source code, documentation, configuration, data, or mixed repository type,
- primary languages, package managers, build tools, and deploy targets,
- single-package, monorepo, multi-service, or documentation-only layout,
- maintainer and contributor model,
- release and versioning expectations,
- security sensitivity and secret exposure risk,
- required CI checks and deployment environments,
- issue, discussion, support, and roadmap channels,
- license and contribution model.

For an existing repository, gather evidence before recommending structural changes. If evidence is incomplete, separate confirmed findings from inferred risks.

## Required Output Contract

For substantive architecture, scaffold, audit, or remediation work, include these sections unless clearly irrelevant:

1. **Objective and scope** — what the repository system must accomplish and exclude.
2. **Assumptions** — defaults used because the user did not specify every detail.
3. **Current-state findings** — evidence and severity for existing repositories.
4. **Target repository model** — repository type, boundaries, ownership, lifecycle, and collaboration model.
5. **Directory tree** — exact files and directories to add, keep, move, or remove.
6. **Governance model** — roles, CODEOWNERS, branch/ruleset policy, merge method, labels, issue intake, and support boundaries.
7. **Automation design** — workflows, triggers, permissions, dependencies, concurrency, artifacts, environments, and failure handling.
8. **Security model** — token permissions, secret handling, dependency controls, scanning, runner trust, and vulnerability disclosure.
9. **Release model** — versions, tags, release notes, artifacts, provenance, promotion, and rollback.
10. **Implementation sequence** — ordered, reversible steps with dependencies.
11. **Validation plan** — local checks, pull request checks, negative tests, manual settings verification, and rollback checks.
12. **Machine-readable blueprint** — provide JSON when requested or when another agent/developer will execute the plan.

## Repository Blueprint JSON

When producing a machine-readable blueprint, use the bundled schema in `assets/repository-blueprint.schema.json` as the contract. Include at least:

- `schema_version`,
- `repository`,
- `architecture`,
- `files`,
- `governance`,
- `issues_and_projects`,
- `pull_requests`,
- `rulesets`,
- `actions`,
- `security`,
- `releases`,
- `implementation`,
- `validation`.

Use stable identifiers and explicit booleans. Do not hide required manual GitHub settings inside prose. Mark each implementation item as one of:

- `file_change`,
- `repository_setting`,
- `organization_setting`,
- `secret_or_variable`,
- `manual_verification`,
- `external_system`.

Validate generated blueprints with:

```bash
python scripts/validate_repository_blueprint.py blueprint.json
```

## File Generation Rules

When generating repository files:

- Return complete file contents, not fragments, unless the user asks for a patch.
- Preserve valid existing content when editing an existing repository.
- Use exact repository-relative paths.
- Keep user-editable placeholders explicit and searchable, such as `REPLACE_ME` or `<OWNER>`.
- Do not invent email addresses, security contacts, package names, deployment targets, or legal entities.
- Do not add a license unless the user selected one or the repository already has a licensing policy.
- Keep README claims verifiable from the repository.
- Do not add badges for workflows, coverage, packages, or releases that do not exist.
- Do not create empty governance files merely to improve a community profile score.
- Prefer YAML issue forms for structured intake and Markdown pull request templates for review context.
- Use repository-level `.github` files when repository-specific behavior is intended; explain when a default community health repository is more appropriate.

Use templates under `assets/repository-starter/` as starting points, not immutable boilerplate.

## Pull Request and Ruleset Defaults

Unless the user provides a different collaboration model, recommend:

- protected default branch or repository ruleset,
- pull requests for changes to the default branch,
- at least one approval for collaborative repositories,
- dismissal or re-review after material changes when risk warrants it,
- required status checks that map to real workflows,
- required conversation resolution,
- restricted bypass permissions,
- CODEOWNERS review for sensitive paths,
- automatic branch deletion after merge,
- squash merge for repositories that want a linear contributor-facing history,
- merge queue only when branch throughput and required checks justify it.

Do not recommend rules that cannot pass with the repository's actual checks. Avoid naming required status checks before those checks exist and have run.

## GitHub Actions Design Rules

For production workflows:

- Declare the minimum required `permissions` at workflow or job level.
- Prefer `contents: read` as the baseline.
- Separate validation, build, release, and deployment responsibilities.
- Use reusable workflows when duplication is material and interfaces are stable.
- Use concurrency controls for deployments and superseded branch runs.
- Use environments for protected deployments and environment-scoped secrets.
- Prefer OIDC federation over long-lived cloud credentials when supported.
- Treat pull requests, issue bodies, comments, branch names, commit messages, and external payloads as untrusted input.
- Avoid interpolating untrusted contexts directly into shell scripts.
- Never expose secrets to workflows triggered from untrusted forks.
- Avoid `pull_request_target` unless its trust boundary is understood and the workflow never executes untrusted checked-out code with privileged credentials.
- Pin third-party actions to a full commit SHA for high-assurance workflows; document the update process.
- Set timeouts for jobs that call external systems or can hang.
- Use artifacts and caches intentionally; define retention and never use caches as trusted artifact storage.
- Add explicit release/deployment gates and rollback instructions.

Validate generated workflows with:

```bash
python scripts/validate_actions_workflow.py .github/workflows/example.yml
```

If exact action versions or node/runtime requirements may have changed, verify current official documentation or release metadata before presenting the workflow as production-ready.

## Security Rules

Treat repository security as a system, not a checklist. Cover:

- least-privilege collaborator access,
- branch/ruleset enforcement,
- two-person review for high-impact paths where appropriate,
- secret scanning and push protection,
- dependency alerts and automated dependency updates,
- code scanning or equivalent analysis,
- private vulnerability reporting when available and appropriate,
- a real `SECURITY.md` reporting route,
- Actions token permissions and action provenance,
- environment protection and deployment credentials,
- signed or verified release artifacts where the threat model warrants it,
- incident response and credential rotation procedures.

Never place secret values in generated examples. Use secret names only.

## Audit Severity Model

Classify findings consistently:

- **Critical** — plausible repository compromise, secret exfiltration, arbitrary privileged code execution, or unsafe release publication.
- **High** — bypassable protection, excessive token permissions, untrusted code with privileged context, missing controls on sensitive deployment/release paths.
- **Medium** — unreliable automation, weak ownership, missing validation, ambiguous contribution flow, dependency or release hygiene gaps.
- **Low** — maintainability, discoverability, consistency, or documentation improvements.
- **Informational** — observations and optional enhancements.

Every finding must include evidence, impact, recommendation, and verification method. Do not report a configuration as missing when it cannot be observed.

## Validation Scripts

Use bundled scripts when a runtime is available:

- `scripts/validate_repository_blueprint.py <blueprint.json>` validates the machine-readable implementation contract.
- `scripts/validate_actions_workflow.py <workflow.yml>` checks workflow structure and common security/reliability hazards.
- `scripts/audit_repository_package.py <repository-path>` checks repository health files, workflow files, suspicious secrets, oversized files, and common governance gaps.

Run relevant validators before returning generated artifacts. Distinguish errors from warnings and explain any accepted warning.

## Quality Bar

Reject shallow repository plans. A professional deliverable must be:

- repository-type aware,
- plan and permission aware,
- explicit about files versus hosted settings,
- safe for contributors and maintainers,
- compatible with automation and agent handoff,
- testable before merge,
- reversible when risk is material,
- honest about unknown live configuration,
- free of fabricated badges, checks, releases, and credentials.
