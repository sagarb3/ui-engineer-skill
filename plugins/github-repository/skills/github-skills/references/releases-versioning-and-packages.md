# Releases, Versioning, and Packages

## Contents

- Release source of truth
- Versioning
- Tags
- Changelog and release notes
- Release workflow
- Artifacts
- Package registries
- Provenance and signatures
- Pre-releases
- Rollback and support

## Release Source of Truth

Choose one release trigger and document it:

- approved version file change,
- merge to a release branch,
- protected tag,
- manually created GitHub Release,
- release orchestration tool.

Avoid workflows where tags, releases, and package versions can drift independently.

## Versioning

Use semantic versioning when public compatibility can be described as major, minor, and patch changes. Define what constitutes a breaking change for the project.

For pre-1.0 projects, document whether minor versions may contain breaking changes.

Other valid strategies include date-based versions or build numbers, but document ordering, compatibility, and support policy.

## Tags

Use annotated or signed tags when provenance and human attribution matter. Protect release tag patterns where the GitHub plan and repository policy support it.

A tag should identify the exact commit used to build released artifacts. Do not move published version tags.

## Changelog and Release Notes

A changelog should prioritize user impact:

- added,
- changed,
- deprecated,
- removed,
- fixed,
- security.

Release notes may be generated from pull request labels and then edited. Ensure labels and merge titles produce useful output.

Do not copy raw commit history as the only release note.

## Release Workflow

A safe release sequence:

1. validate version and changelog,
2. verify default or release branch state,
3. run full test and build matrix,
4. build artifacts in a trusted environment,
5. generate checksums and metadata,
6. sign or attest when required,
7. create immutable version tag,
8. publish package or container,
9. create GitHub Release and attach artifacts,
10. verify installation or deployment,
11. announce and monitor,
12. document rollback or hotfix path.

Make publication idempotent. A rerun should detect existing versions and fail safely or verify exact equivalence.

## Artifacts

For downloadable artifacts, define:

- supported operating system and architecture,
- file naming convention,
- compression format,
- checksum algorithm,
- signature or attestation,
- installation instructions,
- retention policy.

Do not attach debug builds or secret-bearing configuration to public releases.

## Package Registries

For npm, PyPI, crates.io, container registries, or GitHub Packages:

- use least-privilege publication identity,
- prefer trusted publishing or OIDC when supported,
- verify package name ownership,
- prevent publication from pull request workflows,
- align package version and Git tag,
- test package contents before publish,
- document deprecation and yanking policy.

## Provenance and Signatures

Use artifact attestations, package provenance, signed tags, or detached signatures according to the threat model and ecosystem.

Verification instructions must be usable by consumers. A signature without documented verification adds little operational value.

## Pre-Releases

Use pre-release identifiers for alpha, beta, release candidate, and preview channels. Define:

- intended audience,
- stability expectations,
- upgrade path,
- data compatibility,
- whether pre-releases receive security fixes.

Do not mark a release stable solely because automated tests passed.

## Support Policy

Document:

- supported versions,
- security-fix window,
- maintenance branches,
- backport criteria,
- end-of-life process.

## Rollback and Hotfix

A rollback plan should state:

- whether artifacts can be withdrawn,
- how package deprecation works,
- how deployments are rolled back,
- how users are notified,
- how a corrected version is numbered,
- whether tags/releases are preserved for audit.

Never silently replace artifacts under an existing published version.
