# Team Adoption

Use this rollout path to evaluate the collection against your own repositories, clients, models, and engineering controls. It is a suggested adoption process, not a claim of organizational certification or guaranteed productivity gains.

## Start With a Bounded Pilot

Choose one repository, a supported client, and a few representative tasks. Include an ordinary change, an ambiguous requirement, an error or recovery path, and a read-only review. Identify the owners who will assess code quality, task completion, and policy adherence.

Select a reviewed revision and an approved subset of skills. Install the complete folders in the target application's supported project skill directory, or use a managed personal distribution process. Preserve existing instructions and resolve conflicts rather than silently replacing them.

## Establish Baseline Rules

Merge the relevant [baseline instructions](installation.md#make-harness-the-baseline) into the project's existing instruction mechanism. Keep organizational rules for secrets, dependencies, branch protection, review, publication, and external services authoritative.

Confirm that the host discovers the skills and follows its intended activation mechanism. A file in a directory does not prove discovery or permission enforcement. Distinguish UI metadata from configured specialist profiles.

## Evaluate Real Outcomes

Use the [evaluation cases](../evals/README.md) as a starting point and add task-specific cases from your own acceptance requirements. Keep protected source material, credentials, and customer information in appropriate environments.

Compare baseline and with-skill runs under equivalent conditions. Record the client version, model, permissions, starting data, and existing personal instructions. If baseline isolation is incomplete, report it rather than treating the result as a controlled comparison.

Review evidence separately for completed behavior, scope discipline, accessible interaction, recovery, output isolation, and honest reporting. Do not combine incomplete evidence into an artificial pass rate. Use actual observations to decide whether a skill helps the team's work.

## Manage Change Through Git

Pin approved revisions or copy reviewed versions through the team's normal process. Review instruction, guide, index, and evaluation changes together. Re-run the affected cases when behavior or routing changes; avoid a blanket claim that every guide edit requires every test.

Keep the previous approved version available for rollback. Do not rewrite published history to represent a content update. Git approvals, merge protection, and deployment controls remain the team's responsibility.

## Adoption Checklist

| Area | Decision or evidence |
| --- | --- |
| Ownership | Named reviewers for skill changes and evaluation results |
| Distribution | Approved installation path and revision-management process |
| Compatibility | Host and version tested with the selected skill subset |
| Permissions | Native controls for writes, publication, external calls, and destructive actions |
| Data handling | Provider and host policies suitable for the organization's source and data |
| Evidence | Actual task outputs, tool logs, checks, and incomplete criteria |
| Output isolation | Product diffs contain no workflow provenance or unintended instruction files |
| Licensing | Organizational distribution terms reviewed; no repository-wide license is currently included |

## Current Delivery Scope

The repository includes eleven core skills, 45 guides, reference indexes, UI metadata, 58 evaluation cases, local fixtures, and Python/Git evaluation tooling. It does not provide a hosted management service, SSO integration, centralized policy enforcement, certification, or a guaranteed model-performance result.

Live-model evaluations and native-client validation must be performed in the intended environment. The optional Agentic Workflows plugin includes one explicitly selected Copilot profile. The six UI specialist roles remain examples, and automatic delegation is not configured. Establish those roles and permissions explicitly before adding runtime configuration.
