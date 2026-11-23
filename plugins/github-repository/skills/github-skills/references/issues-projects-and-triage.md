# Issues, Projects, and Triage

## Contents

- Intake model
- Issue forms
- Labels
- Issue types
- Triage workflow
- Milestones
- GitHub Projects
- Discussions
- Automation
- Metrics and anti-patterns

## Intake Model

Decide which requests belong in Issues. Common categories:

- reproducible bug,
- accepted feature proposal,
- maintenance task,
- documentation gap,
- security work without vulnerability details,
- operational follow-up.

Route usage questions, broad ideation, and community showcases to Discussions when enabled. Route vulnerabilities privately.

## Issue Forms

Prefer YAML issue forms when structured information improves triage. Use separate forms for materially different request types.

A bug form should normally collect:

- concise problem statement,
- version or commit,
- environment,
- expected behavior,
- actual behavior,
- reproduction steps or minimal reproducer,
- logs with secret-removal reminder,
- regression status,
- duplicate-search confirmation.

A feature form should collect:

- user problem,
- proposed outcome rather than only implementation,
- alternatives or workaround,
- scope and non-goals,
- impact and compatibility concerns,
- willingness to contribute.

Keep optional questions optional. Do not ask for personal contact information by default. Avoid automatically assigning maintainers unless workload and ownership justify it.

Issue forms live under `.github/ISSUE_TEMPLATE/`. Labels referenced by forms must already exist. Pull requests use Markdown templates, not issue forms.

## Label System

Use a small, orthogonal taxonomy. Separate dimensions:

### Type

- `type: bug`
- `type: feature`
- `type: docs`
- `type: maintenance`
- `type: security`

### Status

- `status: needs-triage`
- `status: needs-info`
- `status: accepted`
- `status: blocked`
- `status: in-progress`

### Priority

- `priority: critical`
- `priority: high`
- `priority: medium`
- `priority: low`

### Area

Use repository-specific subsystem labels such as `area: api` or `area: cli`.

### Contribution

- `good first issue`
- `help wanted`

Do not encode the same meaning in multiple labels. Avoid using priority as a promise of delivery date.

## Issue Types

Organization-level issue types can provide consistent high-level classification. Use types for broad semantics and labels for repository-specific detail. Do not create a type taxonomy that duplicates every label.

## Triage Workflow

A practical flow:

1. Validate intake and remove sensitive data.
2. Confirm category and affected version.
3. Reproduce or request the minimum missing evidence.
4. Check for duplicates and related work.
5. Assign type, status, area, and priority only when justified.
6. Decide: accept, defer, redirect, close, or escalate privately.
7. Link milestone, project, pull request, or decision record.
8. Revisit `needs-info` and blocked items on a documented cadence.

For bugs, distinguish severity from priority. Severity measures impact; priority reflects scheduling and strategic context.

## Milestones

Use milestones for a real delivery grouping such as a release or migration phase. Each milestone should have:

- a clear outcome,
- expected timeframe if known,
- included and excluded work,
- owner,
- closure criteria.

Do not use milestones as a permanent backlog taxonomy.

## GitHub Projects

Use Projects when cross-repository planning, custom fields, roadmap views, or workflow automation add value.

Recommended fields:

- status,
- priority,
- iteration or target date,
- repository or area,
- owner,
- effort or size when the team uses it consistently.

Keep repository issue state and project status synchronized conceptually. Avoid dozens of project fields that are not used for decisions.

## Discussions

Use categories such as:

- Announcements,
- Q&A,
- Ideas,
- Show and tell,
- Design proposals.

Define when a discussion becomes an issue. Accepted work should end with a trackable issue or pull request.

## Automation

Safe triage automation can:

- apply labels from issue forms,
- add new issues to a Project,
- request missing information,
- close stale items under a documented policy,
- synchronize milestone or release metadata.

Do not auto-close active bug reports solely by age. Do not let label automation override maintainer decisions without auditability.

## Metrics

Useful operational metrics:

- time to first triage,
- time waiting for reporter information,
- accepted backlog age,
- reopen rate,
- duplicate rate,
- issue-to-PR conversion,
- unresolved critical defects.

Do not optimize for issue closure count at the expense of resolution quality.

## Common Anti-Patterns

- one generic issue template for every request,
- more labels than maintainers understand,
- automatically marking every feature request as accepted,
- mixing security reports with public bugs,
- stale bots that close active discussions,
- milestones with no owner or release meaning,
- Projects that duplicate issue state without workflow value.
