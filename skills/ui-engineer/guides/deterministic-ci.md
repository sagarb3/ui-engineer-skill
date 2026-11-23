# Deterministic UI CI

## Establish the Contract

Map each workspace to its dependents, public assets, tokens, configuration, lockfile, runtime, and generated outputs. Read the scripts before running them. A root `build` may already build every package; adding workspace matrices can repeat the same work.

Choose job boundaries by failure/reuse cost: fast lint/types/unit; production build; Storybook/browser; trusted preview/release. Parallelize independent jobs when saved latency outweighs repeated installs and runner startup. Use artifacts to reuse a verified build only when runner/platform/configuration match.

For React/Vue/Svelte, retain the existing Vite/framework toolchain. For Next.js, distinguish static export from SSR/server actions and build-time versus runtime variables. For a component library, verify package exports/types and representative consumers, not only a development server.

## Path Filters and Required Checks

For a non-required opt-in UI workflow, an example scope is:

```yaml
on:
  pull_request:
    paths:
      - 'packages/ui/**'
      - 'apps/web/**'
      - 'packages/tokens/**'
      - 'package.json'
      - 'pnpm-lock.yaml'
      - 'pnpm-workspace.yaml'
      - 'tsconfig*.json'
      - 'playwright.config.*'
      - 'vitest.config.*'
      - '.github/workflows/ui-ci.yml'
```

Add real consumers, shared config, fonts/assets, environment schema, Storybook configuration, and the chosen task runner's dependency graph. Positive paths above are illustrative, not a complete graph.

Do not put this workflow-level filter on a required check without an accepted skipped-check strategy: GitHub can leave a skipped workflow's check pending. Prefer an always-triggered workflow, changed-file/graph detection, conditional expensive jobs, and an `always()` gate that fails if an applicable dependency failed/cancelled. Treat an unknown diff as affected, not clean. Never append `|| true` to the required gate. Include `merge_group` for merge queues and validate its diff semantics.

## Efficiency Without Weaker Gates

- Cancel superseded PR runs with a workflow+PR concurrency key; do not cancel an in-flight production deployment. Use job/workflow identity to avoid unrelated cancellations.
- Pin pnpm in `packageManager`, Node in `.nvmrc`/existing policy, and action references to verified commits with release comments. Setup pnpm before setup-node's pnpm cache lookup.
- Use frozen installs. Cache the package store by lockfile/runtime/platform. Do not cache `.env`, authenticated npmrc files, tokens, or arbitrary `node_modules` across incompatible contexts.
- Use one primary browser and runtime for routine PRs. Reserve compatibility matrices for supported releases, changed platform-sensitive code, or scheduled sweeps.
- Record job time and flake rate before adding cache services, sharding, or remote task runners. Optimize the dominant work; do not assume more jobs are cheaper.
- Give artifacts a job/run identity when matrices would collide. Set explicit retention and upload only useful reports. Review traces/screenshots for personal data and secrets.

## Storybook and Browser Checks

Build static Storybook using the repository's configured command. Configure Playwright `webServer` to serve that output, probe an actual readiness URL, fail within a bounded startup timeout, and stop at teardown. Run interactions for keyboard, focus, errors, and representative variants. Use existing Storybook/Vitest integration if it already covers the intended contract; avoid duplicating the same suite under another runner.

The template assumes `test:storybook` and `test:e2e` own their Playwright configuration. An illustrative Storybook web-server contract is `command: "pnpm exec http-server storybook-static -p 6006"`, `url: "http://127.0.0.1:6006"`, `reuseExistingServer: !process.env.CI`, `timeout: 120000`; use it only if that server is already installed. The application e2e suite needs its own production-like server and deterministic data.

Visual checks need an accepted baseline source and controlled browser/OS, viewport, fonts, theme, animations, and data. Separate baseline updates from accidental acceptance of every screenshot. A screenshot diff neither proves keyboard behavior nor satisfies an accessibility audit.

## Forks, Previews, and Releases

`pull_request` validation executes untrusted proposed code with read-only tokens and no deployment secrets. Hosted runners are preferred for public fork execution. `pull_request_target` must never check out and execute the fork head with privileged credentials.

For previews, choose one documented model: a provider-managed isolated fork-safe preview; a protected environment for reviewed changes; or an explicitly trusted-ref manual deployment. A same-repository PR is not automatically trusted. Environment approval does not make arbitrary code safe to run with a production token.

`workflow_run` is privileged relative to the producer. Verify event, repository, branch, conclusion, SHA, and artifact producer before consuming output; never execute an untrusted artifact with deployment credentials. Build again from an approved trusted ref when needed. Use provider-scoped OIDC, environment restrictions, immutable artifacts, link publication, expiry/cleanup, and a documented rollback. Do not invent a provider-specific deployment command.

Check that GITHUB_TOKEN-created PRs will actually run required CI under the organization's event policy. Do not bypass that limitation by silently adding a broad PAT.
