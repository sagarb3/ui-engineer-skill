# Reviewed Sources and Freshness

Research snapshot: November 23, 2026. These are original UI-specific instructions and templates synthesized from the sources below. Existing optional packages elsewhere in the collection vendor separate upstream material; this skill does not depend on those packages.

## GitHub Agentic Workflows

Repository: [github/gh-aw](https://github.com/github/gh-aw), reviewed main commit `b2079f45216d1e64599b1663d8dcc66380df0567`.

Read the authoring index and its constraints/editing/validation references; frontmatter, safe outputs, engine and network documentation; and the Copilot dynamic workflow smoke test and packaged extension. Key decisions retained here are read-only agent jobs, bounded safe-output writes, precise triggers, source/lock ownership, evidence-backed completion, minimum network/tool access, and opt-in experimental extensions.

- [Authoring index at the reviewed revision](https://github.com/github/gh-aw/blob/b2079f45216d1e64599b1663d8dcc66380df0567/.github/aw/github-agentic-workflows.md)
- [Execution and security boundaries](https://github.com/github/gh-aw/blob/b2079f45216d1e64599b1663d8dcc66380df0567/.github/aw/workflow-constraints.md)
- [Safe-output reference](https://github.com/github/gh-aw/blob/b2079f45216d1e64599b1663d8dcc66380df0567/docs/src/content/docs/reference/safe-outputs.md)
- [Copilot authentication and dynamic support](https://github.com/github/gh-aw/blob/b2079f45216d1e64599b1663d8dcc66380df0567/docs/src/content/docs/reference/engines/copilot.md)
- [Packaged dynamic smoke test](https://github.com/github/gh-aw/blob/b2079f45216d1e64599b1663d8dcc66380df0567/.github/workflows/smoke-copilot-dynamic-workflow.md)

The example gh-aw sources were compiled locally with released compiler **v1.2.2**. Main-branch research and compiler release are distinct snapshots. Compilation used release action mode pinned to the release commit:

```sh
gh aw compile ci-doctor docs-sync dynamic-review --strict \
  --action-mode release \
  --action-tag 399a445fe2d8926c616b54b1b82a16b5b2be4445
```

This is a reproducible reference command for those IDs and that reviewed release, not a universal version policy. With another installed compiler, resolve and review its compatible release commit first. A plain compile with v1.2.2 emitted mutable helper-action references; the explicit release pin removed those warnings. Inspect generated references rather than assuming strict mode alone guarantees every helper is pinned.

All three sources compiled; the dynamic extension retained its expected experimental-feature warning. No hosted workflows, inference, provider authentication, safe-output writes, or dynamic SDK execution were run. See the skill's README for prerequisite adaptation. Do not copy compiled lock files from this research workspace into another repository.

## Agentics

Repository: [githubnext/agentics](https://github.com/githubnext/agentics), reviewed main commit `139fa09ef17cde4135e696ff8e7af09bc5ddfa6e`.

Studied CI Doctor, Repo Assist, efficiency/test/doc improvers, accessibility review, link checker, and issue triage. Followed `daily-*` redirects to maintained files. Retained root-cause evidence, measured improvements, meaningful test gaps, user-facing docs, duplicate/open-PR checks, and explicit no-op outcomes.

- [CI Doctor](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/ci-doctor.md)
- [Repo Assist](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/repo-assist.md)
- [Test improver](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/test-improver.md)
- [Efficiency improver](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/efficiency-improver.md)
- [Docs updater](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/doc-updater.md)
- [Accessibility review](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/accessibility-review.md)
- [Link checker](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/link-checker.md)
- [Issue triage](https://github.com/githubnext/agentics/blob/139fa09ef17cde4135e696ff8e7af09bc5ddfa6e/workflows/issue-triage.md)

Deliberate adaptations: bounded tasks instead of broad backlog campaigns; minimal toolsets instead of all-tools defaults; manual activation before schedules; draft reviewable changes; no optional promotional/authoring attribution in downstream artifacts. Do not remove platform-required provenance or legal notices. Upstream examples are task inspiration, not permission or a current security baseline for a different repository.

## GitHub Repository Skills

Repository: [he8um/github-skills](https://github.com/he8um/github-skills), reviewed main commit `93fb4a9c6b11bf34b4e00d7621a08cfc44014640`.

Studied the skill entry point plus repository architecture, Actions design/security, governance, audits, and output templates. Retained discovery-first changes, event trust boundaries, immutable action references, cache/artifact provenance, evidence/severity reports, and explicit implementation types for settings versus files.

- [Core skill](https://github.com/he8um/github-skills/blob/93fb4a9c6b11bf34b4e00d7621a08cfc44014640/github-skills/SKILL.md)
- [Actions design](https://github.com/he8um/github-skills/blob/93fb4a9c6b11bf34b4e00d7621a08cfc44014640/github-skills/references/github-actions-design.md)
- [Actions security](https://github.com/he8um/github-skills/blob/93fb4a9c6b11bf34b4e00d7621a08cfc44014640/github-skills/references/github-actions-security.md)
- [Audit and troubleshooting](https://github.com/he8um/github-skills/blob/93fb4a9c6b11bf34b4e00d7621a08cfc44014640/github-skills/references/audit-and-troubleshooting.md)

The smaller report schema here is authored for frontend delivery, not a replacement for the upstream repository-blueprint validator.

## Update Policy

[sources.json](../sources.json) records reviewed files, immutable source revisions, and action SHA/release mappings. These records are research provenance, not a signature or an automatic updater. Recheck upstream diffs, installed compiler/engine capabilities, action publisher/release mappings, and generated locks when updating. Review changes; do not blindly refresh pins or hashes to silence validation.
