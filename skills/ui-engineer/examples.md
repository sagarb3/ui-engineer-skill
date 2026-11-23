# UI Engineer Examples

## Secure a Workspace CI Pipeline

**Inputs:** A pnpm workspace with `packages/ui`, `packages/tokens`, and `apps/web`; root lint/type/unit/build scripts; Storybook and Playwright configuration; a required `UI gate` check. Existing preview deployment uses privileged fork code.

```text
Use ui-engineer to audit the UI CI and preview workflows. Keep our
package manager and existing scripts. Make the required gate report
for docs-only changes and shared-token changes. Add only the missing
Storybook/browser coverage. Separate fork validation from trusted
preview deployment. Ask about any unresolved provider or environment
policy; report settings you cannot inspect. Do not deploy.
```

**Expected deliverable:** An evidence-backed finding and scoped workflow patch with complete command contracts, stable gate behavior, verified action pins, read-only PR permissions, explicit preview prerequisites, and bounded useful artifacts.

**Verification:** Parse/lint YAML, run relevant local commands if permitted, inspect UI/shared/docs/fork/merge-queue paths and job conditions, and verify hosted settings separately. A locally valid file is not a passing GitHub run or a deployed preview.

## Add CI Doctor Without Autonomous Production Changes

**Inputs:** A deterministic workflow named `UI CI`, access to failed-job logs, approved Copilot billing/authentication mode, a policy allowing one deduplicated failure issue, and a compatible gh-aw compiler.

```text
Use ui-engineer to add CI Doctor for failed UI CI runs on main. Read
logs and relevant changes, classify the likely cause with confidence,
and create at most one deduplicated issue. No shell writes, patches,
reruns, dispatches, or merges. Keep agent permissions read-only and
use safe outputs. Compile strictly and review source plus lock.
Do not run paid inference or enable a schedule.
```

**Expected deliverable:** Adapted Markdown source and compiler output with failure-only producer gating, limited GitHub reads, bounded output, duplicate/no-op conditions, explicit trust rules, and a truthful compiler result.

**Verification:** Compile with the named installed version, review generated permissions/network/handlers, and test successful/cancelled/duplicate/missing-log cases under separately authorized runtime evaluation. Dynamic Copilot extensions are a different optional feature and must not be enabled by this request.
