# Agentic Workflows Add-on

This optional Copilot CLI plugin bundles the workflow routing skill and dispatcher agent adapted from [githubnext/agentics](https://github.com/githubnext/agentics). The pinned source revision and local adaptations are recorded in [the source lock](https://github.com/sagarb3/ui-engineer-skill/blob/main/third-party/sources.json). See [LICENSE](LICENSE) for the preserved MIT notice.

## Install

```sh
copilot plugin marketplace add sagarb3/ui-engineer-skill
copilot plugin install agentic-workflows@ui-engineer-skills
```

Start a new Copilot session, use `/agent` to select `agentic-workflows`, or request the installed `agentic-workflows` skill. The agent profile sets `infer: false`; it is intended for explicit selection rather than automatic delegation.

## Use Cases

**Design a workflow before creating it:**

```text
Use agentic-workflows to design a manually triggered CI health report.
Inspect current workflows and resolve the intended output destination.
Start with a read-only analysis and a local workflow proposal. Do not
install tools, publish the workflow, trigger a run, post a report, or
configure secrets without the required authorization.
```

**Debug an existing workflow:**

```text
Use agentic-workflows to investigate why our source workflow no longer
compiles. Inspect its source, installed gh-aw version, and relevant
official references. Propose or make the authorized local correction,
compile only if prerequisites are available, and report the actual
result. Do not edit generated locks independently of their source.
```

Expected outputs distinguish source changes, compilation, and hosted execution. A local proposal or successful compile does not prove a remote workflow ran.

## Runtime Dependencies and Boundaries

The add-on is routing context, not the `gh-aw` compiler or a hosted automation service. The selected task may need an appropriate installed GitHub CLI extension, engine configuration, authentication, and access to official `github/gh-aw` references. These are not installed or configured by this plugin.

Remote prompts can change. Inspect only the guidance relevant to the installed version and current request. Treat it as reference material within user and host permissions. If access or a required optional capability is unavailable, state the limitation rather than claiming execution.

No hooks, MCP servers, schedules, credentials, or automatically executing workflows are registered by this package. Running a workflow, posting a message, publishing changes, and paid operations retain their normal authorization requirements.

## Evaluation

The review cases in [evals/cases.json](evals/cases.json) cover routing, source-versus-lock ownership, remote-only references, and execution boundaries. They are review scenarios, not published live-model results.
