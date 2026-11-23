# Repository Architecture

## Contents

- Repository purpose and boundary
- Repository types
- Single repository vs monorepo
- Directory architecture
- Documentation architecture
- Generated files and vendored content
- Template repositories
- Naming and metadata
- Architecture decision checklist

## Repository Purpose and Boundary

Define one primary reason for the repository to exist. A repository boundary should make ownership, release cadence, access control, and change review understandable.

Use a separate repository when one or more of these are materially different:

- ownership or access policy,
- release lifecycle,
- deployment boundary,
- legal or licensing constraints,
- security classification,
- external contribution model,
- independent archival lifecycle.

Do not split repositories only to make the tree look smaller. Do not combine unrelated products only to centralize CI.

Document:

- what belongs in the repository,
- what does not belong,
- authoritative source locations,
- generated output policy,
- release unit,
- support status.

## Repository Types

### Application repository

Include deployable source, configuration, migrations, tests, operational docs, and deployment automation. Define environment boundaries and rollback expectations.

### Library or SDK repository

Prioritize public API stability, compatibility policy, package metadata, examples, changelog, semantic versioning, deprecation policy, and package publishing integrity.

### CLI repository

Include installation methods, shell completion strategy, platform support matrix, release artifacts, checksums, update policy, and command reference.

### Infrastructure repository

Separate reusable modules from environment instances. Require plan validation, environment protection, least-privilege deployment identity, and state/back-end documentation.

### Documentation repository

Define source format, build system, link checks, style guide, versioning, publication workflow, and content ownership.

### Configuration or policy repository

Treat changes as high impact. Define schema validation, test fixtures, staged rollout, policy ownership, and consumers.

### Data or dataset repository

Document provenance, schema, license, update cadence, privacy classification, checksums, and large-file strategy. Avoid storing sensitive or frequently changing operational data directly in Git.

### Template repository

Keep placeholders explicit, test generated output, minimize organization-specific assumptions, and document post-generation setup. A template should produce a coherent repository without carrying the original repository history.

### Skill, prompt, or agent repository

Separate runtime instructions from references, examples, assets, tests, and distribution bundles. Define supported agent environments, installation procedure, validation, packaging, and security boundaries.

## Single Repository vs Monorepo

Use a monorepo when shared changes, atomic refactors, unified dependency policy, and coordinated releases create more value than independent access and release boundaries.

A monorepo should define:

- workspace/package boundaries,
- ownership by path,
- affected-project detection,
- dependency direction rules,
- package-level tests and releases,
- shared tooling ownership,
- cache and artifact strategy.

Avoid a monorepo when teams require incompatible access policies, unrelated release lifecycles, or high-volume history that harms normal operations.

## Directory Architecture

Prefer predictable top-level names. A typical software repository may contain:

```text
.github/       GitHub-specific configuration
src/           production source
lib/           reusable implementation where ecosystem conventions expect it
tests/         automated tests
docs/          extended documentation
examples/      executable or copyable examples
scripts/       repository automation
config/        checked-in configuration
assets/        static project assets
.github/       issue forms, PR templates, workflows, funding, CODEOWNERS
```

Do not introduce directories with overlapping responsibility. Follow language ecosystem conventions before inventing custom names.

For monorepos, prefer explicit roots such as:

```text
apps/
packages/
services/
libs/
tools/
docs/
```

Define package boundaries in a root architecture document.

## Documentation Architecture

At minimum, decide whether the repository needs:

- `README.md` for orientation and verified quick start,
- `LICENSE` for legal reuse terms,
- `CONTRIBUTING.md` for contribution workflow,
- `SECURITY.md` for private vulnerability reporting,
- `CODE_OF_CONDUCT.md` for community behavior,
- `SUPPORT.md` for support boundaries,
- `CHANGELOG.md` for human-readable release history,
- `CODEOWNERS` for path ownership,
- `docs/architecture.md` or ADRs for durable decisions,
- runbooks for operations and incident response.

Keep the README concise enough to orient a new user. Move deep architecture, API reference, and operations material into `docs/` and link it clearly.

Do not claim installation, compatibility, security, or performance properties that are not tested.

## Generated Files and Vendored Content

For generated files, document:

- source file,
- generator command and version,
- whether generated output is committed,
- validation in CI,
- review expectations.

Commit generated output when consumers require it directly, releases require reproducibility, or generation tools are not universally available. Otherwise prefer generation during build or release.

For vendored dependencies, document provenance, version, license, update process, and integrity verification.

## Large Files

Avoid large binaries in normal Git history. Use release assets, package registries, object storage, or Git LFS according to the access and retention model. Do not use Git LFS without documenting clone/build requirements and storage implications.

## Template Repositories

A repository template should include:

- placeholder inventory,
- setup checklist,
- removable example content,
- valid CI in the generated state or clear activation steps,
- license selection instructions,
- secret and environment setup instructions,
- a post-generation validation command.

Do not include production secrets, inherited issue history, or assumptions tied to one organization.

## Naming and Metadata

Use a repository name that is:

- concise,
- discoverable,
- lowercase when ecosystem conventions permit,
- free of ambiguous internal acronyms for public projects,
- stable enough to survive implementation changes.

Repository description should state the product or capability, primary audience, and differentiator without marketing claims that cannot be verified.

Topics should improve discovery. Prefer 8-15 accurate topics over the maximum number of loosely related tags.

## Architecture Decision Checklist

Before finalizing a repository architecture, verify:

- the boundary matches ownership and release behavior,
- the default branch contains a usable project state,
- the root tree is understandable without tribal knowledge,
- generated and vendored content are governed,
- security-sensitive paths have owners,
- build and test commands are deterministic,
- public and private information are separated,
- archives, releases, and packages have clear retention rules,
- the repository can be handed to another maintainer.
