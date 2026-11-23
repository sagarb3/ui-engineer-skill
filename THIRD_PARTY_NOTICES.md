# Third-party Notices

The ten original React UI and Git skills remain separate from the optional third-party add-ons. The add-ons reuse the following MIT-licensed material with its license and copyright notices preserved.

## GitHub Repository Engineering

- Source: [he8um/github-skills](https://github.com/he8um/github-skills).
- Revision: `93fb4a9c6b11bf34b4e00d7621a08cfc44014640`.
- Copyright: 2026 AmirHesam Piri.
- License: [MIT](plugins/github-repository/LICENSE).
- Included: the `github-skills` skill, its references, helper scripts, schemas, starter templates, UI metadata, and example repository blueprint.
- Adaptation: added local English-only, output-isolation, clarification, authorization, runtime-dependency, and helper-path rules to `SKILL.md`.

The license is also included inside the skill folder so copying the whole skill preserves its notice. Starter files are templates; they are not applied to a consuming repository by installing the plugin.

## Agentic Workflows

- Source: [githubnext/agentics](https://github.com/githubnext/agentics).
- Revision: `139fa09ef17cde4135e696ff8e7af09bc5ddfa6e`.
- Copyright: 2025 GitHub.
- License: [MIT](plugins/agentic-workflows/LICENSE).
- Included: the Agentic Workflows routing skill and workflow dispatcher agent.
- Adaptation: added English-only isolation and explicit task boundaries, mapped explicit invocation to Copilot CLI's `infer: false`, enabled repository instruction loading, and clarified external references and tool dependencies.

The contribution-checker agent, generated workflows, remote prompt library, hosted services, compiler, and CLI extension are not included. The routing material refers to official `github/gh-aw` documentation, which is retrieved only as needed for an authorized task. That external repository is a runtime reference, not vendored source in this package.

## Version and Update Records

[third-party/sources.json](third-party/sources.json) records each imported file's source path, upstream Git blob, local path, installed SHA-256, and whether it was adapted. These hashes describe the reviewed local snapshot; they are not a signature or certification from the upstream authors.

Updates require a reviewed upstream revision, inspection of changes and license terms, refresh of the recorded file hashes, and relevant checks. Installation does not follow upstream branches or run an update script.

New integration manifests, examples, and maintenance documentation are maintained in this repository separately from the imported source. No upstream endorsement or affiliation is implied. The upstream MIT notices do not establish a repository-wide license for the original collection.
