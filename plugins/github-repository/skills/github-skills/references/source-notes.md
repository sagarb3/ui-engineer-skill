# Source Notes and Freshness Rules

## Source Priority

Use sources in this order:

1. Current GitHub Docs for hosted behavior and feature syntax.
2. GitHub CLI manual for `gh` behavior.
3. GitHub REST or GraphQL API documentation for automation contracts.
4. Official action repositories and release metadata for action versions.
5. Language or package-registry official documentation for ecosystem-specific publishing.
6. Community discussions only as practitioner evidence, never as authoritative platform behavior.

## Core Official Sources

- Repository best practices: https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- Repository rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- CODEOWNERS: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- Issue forms: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
- Community health files: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- GitHub Actions workflow syntax: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- Reusable workflows: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
- Actions secure use: https://docs.github.com/en/actions/reference/security/secure-use
- GITHUB_TOKEN: https://docs.github.com/en/actions/tutorials/authenticate-with-github_token
- OpenID Connect: https://docs.github.com/en/actions/concepts/security/openid-connect
- Deployment environments: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
- Releases: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- GitHub security features: https://docs.github.com/en/code-security/getting-started/github-security-features
- GitHub CLI manual: https://cli.github.com/manual/

## Freshness Rules

Verify current documentation before asserting:

- feature availability by plan or repository visibility,
- issue form schema fields,
- Actions runner images or runtime versions,
- permission names and defaults,
- merge queue behavior,
- ruleset capabilities,
- security feature availability,
- API preview headers or endpoint behavior,
- official action versions and commit SHAs,
- package trusted-publishing support.

## Practitioner Patterns

The skill includes opinionated patterns such as small label taxonomies, short-lived branches, explicit repository boundaries, least-privilege workflows, and release idempotency. Treat these as engineering recommendations, not GitHub platform guarantees.

When a user provides a conflicting organizational standard, preserve it if it is intentional, safe, and compatible with GitHub behavior.
