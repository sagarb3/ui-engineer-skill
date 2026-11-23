# Repository Practices and Audit Deliverables

## Survey Before Editing

Inspect repository layout and purpose, maintained packages/apps, commands, default branch, workflows, release/deploy model, contribution docs, issue forms, CODEOWNERS, dependency update policy, and security reporting instructions. Inspect rulesets, environments, Actions policy, and token settings only when connected access permits; mark absent access as unverified.

Do not invent maintainers, license, email/security contacts, labels, supported platforms, or compliance requirements. Ask about missing decisions. Existing team instructions and authorization take precedence over example defaults.

## Security Review

- Top-level Actions permissions are read-only or empty; grant only required job scopes. OIDC belongs only on the relevant deployment/authentication job and needs restrictive provider-side claims.
- Resolve every third-party action to an immutable commit and record the release mapping. Pin external reusable workflows; review imports and automated update diffs. A SHA is a version pin, not proof the action is safe.
- Treat event titles, bodies, branch names, logs, artifacts, and external responses as untrusted. Pass data through quoted environment variables/files or structured action inputs, never expression interpolation into shell code.
- Avoid privileged `pull_request_target` execution of fork content. Do not execute uploaded artifacts or restore untrusted caches in privileged jobs. Avoid persistent privileged self-hosted runners for public forks.
- Keep secrets out of logs, caches, traces, and archives. Prefer scoped short-lived credentials and supported OIDC. Never broaden a token automatically after a 403.
- Protect workflow, CODEOWNERS, release, and authentication changes through the existing review policy. A CODEOWNERS file does not enable enforced review by itself.
- Review environment approval and branch constraints, secret scanning and supported code/dependency scanning, dependency update ownership, release provenance, and artifact retention. Describe plan-dependent controls honestly.

## Governance and Housekeeping

Match issue templates to real reproduction needs: browser/OS, package/framework versions, expected/actual behavior, minimal reproduction, and accessibility impact. Keep PR checklists focused on meaningful UI changes, screenshots when useful, and actual test evidence.

Stage required checks only after their exact names have reported successfully. Include merge queue events if used. Do not disable a ruleset to resolve one misnamed or path-filtered check. Separate review policy, merge mode, protected branches/tags, release ownership, and emergency procedures.

Keep CI/deploy owners and dependency updates explicit. Review stale/broken badges, docs commands, archived preview URLs, expired artifacts, caches, obsolete Node matrices, orphaned environments, and redundant schedules. Propose cleanup with retention/ownership evidence; never silently delete user resources.

## Audit Output

For each finding supply ID, severity, status (`confirmed` or `unverified`), evidence, impact, smallest correction, implementation type, and verification. Use `critical` for an evidenced active credential/privileged execution exposure; `high` for a plausible exploitable trust-boundary violation; `medium` for meaningful reliability/governance risk; `low` for a minor maintenance issue. Explain why; do not manufacture severity from a missing preferred convention.

A small original structured report can look like:

```json
{
  "scope": "frontend delivery",
  "findings": [{
    "id": "UI-CI-01",
    "severity": "high",
    "status": "confirmed",
    "evidence": [".github/workflows/preview.yml:24 executes the fork head with a deployment token"],
    "impact": "Unreviewed contributor code can use deployment authority.",
    "correction": "Separate read-only validation from a trusted-ref protected deployment.",
    "implementation_type": "file_change",
    "verification": "Review the fork event and generated job token/environment boundaries."
  }],
  "unverified_settings": ["preview environment approval policy"],
  "checks_run": [],
  "next_action": "Review the scoped workflow patch."
}
```

Use `repository_setting`, `organization_setting`, `secret_or_variable`, `external_system`, or `manual_verification` when a file change cannot apply the control. Include an ordered remediation plan and rollback/verification for consequential changes. Do not call proposed settings applied or a local validation a hosted pass.
