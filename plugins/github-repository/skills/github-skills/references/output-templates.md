# Output Templates

## Repository Architecture Report

```markdown
# Repository Architecture

## Objective
## Assumptions
## Repository Type and Boundary
## Target Users and Maintainers
## Directory Tree
## Documentation Model
## Governance and Ownership
## Issue and Pull Request Workflow
## Ruleset and Merge Policy
## GitHub Actions
## Security Controls
## Release Model
## Implementation Sequence
## Validation Checklist
## Open Decisions
```

## Audit Finding

```markdown
### GH-001 — Finding title

- **Severity:** High
- **Domain:** GitHub Actions
- **Status:** Confirmed
- **Evidence:** `.github/workflows/release.yml`, lines ...
- **Impact:** ...
- **Recommendation:** ...
- **Implementation type:** `file_change` and `repository_setting`
- **Verification:** ...
```

## Repository Blueprint JSON

Use `assets/repository-blueprint.schema.json`. Example skeleton:

```json
{
  "schema_version": "1.0",
  "repository": {
    "name": "example-repo",
    "visibility": "public",
    "default_branch": "main",
    "repository_type": "library"
  },
  "architecture": {
    "layout": "single-package",
    "primary_languages": ["Python"],
    "package_managers": ["pip"]
  },
  "files": [],
  "governance": {},
  "issues_and_projects": {},
  "pull_requests": {},
  "rulesets": [],
  "actions": {},
  "security": {},
  "releases": {},
  "implementation": [],
  "validation": []
}
```

## File Bundle Output

````markdown
## `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
complete file content
```

## `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
complete file content
```
````

## Ruleset Plan

```markdown
### Default branch ruleset

- Target: `main`
- Enforcement: Active
- Bypass actors: repository administrators only, emergency use
- Require pull request: Yes
- Required approvals: 1
- Dismiss stale approvals: Yes for sensitive repositories
- Require code owner review: Yes for protected paths
- Require status checks:
  - `validate / test`
- Require conversation resolution: Yes
- Block force pushes: Yes
- Block deletion: Yes
- Notes: Create the workflow and observe the check before requiring it.
```

## Actions Workflow Review

```markdown
# Workflow Review

## Trust Boundary
## Trigger Analysis
## Token Permissions
## Third-Party Actions
## Untrusted Input
## Secrets and Environments
## Runner Trust
## Artifacts and Caches
## Concurrency and Idempotency
## Findings
## Corrected Workflow
## Verification
```

## Remediation Plan

```markdown
| Order | Finding | Change | Type | Risk | Dependency | Verification |
|---:|---|---|---|---|---|---|
| 1 | GH-001 | Restrict workflow token | file_change | Low | None | Run permission test |
```

## GitHub CLI Plan

```bash
# Read current state first
gh repo view OWNER/REPO --json name,visibility,defaultBranchRef

# Proposed write command; run only after review
# gh api --method PATCH ...
```
