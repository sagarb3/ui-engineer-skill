# Synthetic UI Workspace

This source-only fixture represents a pnpm UI workspace. It does not install dependencies, supply secrets, or run GitHub Actions. The preview workflow is intentionally unsafe for security review and lives only inside the local evaluation fixture.

Expected requirements: retain the required UI gate, include shared token/config changes, keep fork validation read-only, and clarify preview-provider policy before deployment. No gh-aw compiler, billing choice, browser, hosted settings, or model account is provisioned.
