# Reference Notes

This collection was developed using the projects below as research and inspiration. Its original ten skills, guides, fixtures, evaluation tool, tests, and README were written for this repository without vendoring the eight inspiration projects below. The later optional packages do vendor reviewed MIT-licensed sources from two additional projects, documented separately below.

The distinction matters: the references informed decisions and coverage, but this repository is not a translation or repackaging of their implementations. It must not claim their test results, tooling, integrations, licenses, or runtime capabilities as its own.

| Reference | What informed this collection | Boundary |
| --- | --- | --- |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | Necessity-first decisions, reuse, and small complete changes | No plugin implementation, hooks, or benchmark results imported |
| [i-have-adhd](https://github.com/ayghri/i-have-adhd) | Action-first presentation, short numbered steps, and explicit mode changes | Response guidance was written here; no evaluation runner or cases imported |
| [Oil UI](https://github.com/oil-oil/oil-ui) | Detailed coverage of design exploration, composition, imagery, motion, reconstruction, review, and browser evidence | Original English guides were added here; no upstream scripts, media services, or reference files bundled |
| [Syncfusion Pure React component skills](https://github.com/syncfusion/pure-react-ui-components-skills) | Focused topic guides and checking actual installed component APIs | No vendor-specific implementation examples or commercial component code imported |
| [Keiko](https://github.com/oscharko-dev/Keiko) | Customer-specific test conventions, typed boundaries, real controls, and honest execution claims | No workspace engine or test-generation implementation imported |
| [React Doctor](https://github.com/millionco/react-doctor) | React quality concerns and evidence-led performance diagnosis | No detector rules, source code, repository corpus, or measured results imported |
| [Agent Skills](https://github.com/addyosmani/agent-skills) | Engineering workflows, explicit constraints, evaluation cases, and the distinction between skills and agent profiles | This repository's evaluation format, fixtures, and tool were authored separately |
| [UI Skills](https://github.com/ibelick/ui-skills) | Practical interface quality, accessible primitives, and motion/performance considerations | Existing project conventions take precedence; no registry, MCP implementation, or opinionated dependency requirements imported |

## How the Material Was Used

The initial pass produced ten compact skills. Later revisions expanded their decision rules and examples, then added twelve UI design guides, supporting guides for the other skills, local reference indexes, metadata, and evaluation scaffolding.

These changes reflect the actual development conversation. The [initial brief](initial-prompt.md) preserves the original request. The [history reconstruction record](history-reconstruction.md) explains the separately assigned dates and branch topology; those dates are not evidence that the work occurred during the reconstructed period.

## Output and Ownership

These notes describe the collection itself. Do not copy them, the initial brief, authoring provenance, or reference-project links into downstream product code or documentation. Preserve legitimate legal notices for any third-party material a consuming project actually uses.

No repository-wide license has been selected. A reference project's license does not automatically apply to this collection, and inspiration does not transfer permission to redistribute unrelated source material.

## Optional Package Sources

| Project | Bundled material | Review record |
| --- | --- | --- |
| [he8um/github-skills](https://github.com/he8um/github-skills) | Repository engineering skill, reference guides, schemas, templates, validators, sample blueprint, and skill metadata | Adapted entry point; other imported files preserved with their licenses |
| [githubnext/agentics](https://github.com/githubnext/agentics) | Agentic Workflows routing skill and dispatcher profile | Adapted to explicit Copilot plugin selection and local authorization boundaries |

Both sources are MIT licensed. [Third-party notices](../THIRD_PARTY_NOTICES.md) identify copyright holders and adaptations. The [source lock](../third-party/sources.json) records immutable upstream commits, original Git blobs, and installed hashes. No automatic upstream synchronization is enabled.

## Frontend Delivery Skill

The added [ui-engineer skill](../skills/ui-engineer/README.md) synthesizes frontend-specific CI/CD, gh-aw authoring, and repository audit guidance from [github/gh-aw](https://github.com/github/gh-aw), [githubnext/agentics](https://github.com/githubnext/agentics), and [he8um/github-skills](https://github.com/he8um/github-skills). Its guides and templates are authored for this collection; reviewed source revisions and compiler/action mappings are recorded in its [source notes](../skills/ui-engineer/guides/sources.md) and [research index](../skills/ui-engineer/sources.json). Existing optional vendored packages and their preserved notices remain separate.
