# Skills, Metadata, and Specialist Agents

A skill is a workflow loaded for a relevant task. A specialist agent is a separately configured role or execution context. Installing a skill does not create an agent, and a file under a skill's `agents/` directory is not necessarily an executable agent definition.

## What Is Included

Each core skill includes `agents/openai.yaml` with its display name, short description, and an invocation example. This is skill UI metadata. It does not launch a process, configure automatic delegation, choose a paid model, or grant additional permissions.

The reference indexes and evaluation cases describe content and verification. Neither is a runtime orchestration configuration. The evaluation tool prepares local workspaces and records reviewer judgments; it does not create model sessions.

## Bundled Copilot Agent

The optional [Agentic Workflows package](../plugins/agentic-workflows/README.md) includes a native profile at `com.github.copilot/agents/agentic-workflows.agent.md`. Install `agentic-workflows@ui-engineer-skills`, start a new session, and select it through `/agent`.

The profile routes workflow creation, changes, and debugging to relevant upstream guidance. It sets `infer: false` for explicit selection and includes repository instructions. It does not install gh-aw, configure an engine, supply authentication, or grant permission to publish or run hosted workflows. Those dependencies and actions require their normal setup and authorization.

Its two use cases and five review scenarios are in the package. Plugin installation and skill discovery were tested locally; live agent dispatch, model behavior, and hosted runs are separate checks. The original six UI roles below remain proposed roles rather than bundled profiles.

## Practical Role Examples

See [agent role use cases](agent-use-cases.md) for six detailed examples: UI architect, React builder, test engineer, UI reviewer, performance auditor, and Git operator. Each includes inputs, a copyable role prompt, an expected handoff, and a review boundary.

These examples work as role instructions in an ordinary session with the named skills installed. They are not claims that native specialist profiles exist. Each skill also includes its own `examples.md` with two worked scenarios, and its UI metadata supplies a task-specific starting prompt.

## Reusable Specialist Profiles

Native agent profiles define a role, appropriate tasks, expected inputs, process, output contract, and scope boundaries. They can be selected explicitly, and some hosts also use them for delegation. The host determines discovery, context isolation, tool availability, and permissions.

For example, a React test specialist can focus on public behavior and deterministic asynchronous tests. A visual reviewer can inspect current screenshots without editing product files. A Git operator can carry out authorized commands while requiring exact approval for destructive operations.

Each profile should distinguish instructions from enforced permissions. Saying "read-only" in prose is not proof that the runtime denies writes. Configure supported native restrictions where available, inspect their effect, and state limitations honestly.

Copilot CLI uses [custom agent profiles](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli) in `.github/agents/` or `~/.copilot/agents/`. Cursor has its own [subagent files](https://cursor.com/docs/subagents). Claude Code and OpenCode have their own formats and permissions. Do not rename one configuration into another client's directory and assume equivalent behavior.

These native specialist profiles are distinct from the UI metadata already included. They should be created only after the intended roles and selection/delegation behavior are established.

## Automatic Delegation

Automatic delegation additionally needs routing rules: what triggers a specialist, what context it receives, whether it can edit, what it returns, and who integrates the result. It is a behavior choice rather than a property of `SKILL.md` alone.

Avoid automatically spawning a team for every task. A single obvious Git operation should stay direct. A useful specialist handoff has a bounded task and a clear reason such as independent review or isolated investigation. Do not give concurrent writers ownership of the same files.

Provide the task, accepted constraints, relevant inputs, available tools, and permitted side effects. For an independent review, do not supply the desired verdict or ask the implementer to certify its own work as independent. Require actual evidence for review and execution claims.

Child contexts do not expand authorization. Destructive Git actions, external publication, paid calls, and messages still require the authority applicable to the task. Set appropriate stopping conditions for retries and avoid recursive delegation loops.

## Portability and Evaluation

Keep the role's substantive guidance consistent across clients, while adapting native frontmatter and permission settings to the installed version. Do not pin an arbitrary model or request unavailable tools merely to populate configuration fields.

Test profile discovery, explicit selection, intended routing, permissions, and output boundaries separately from skill behavior. Record the host and version. A valid Markdown or YAML file is not proof that the host loaded it or enforced its permissions.

Native profile creation and automatic delegation are separate deliverables. Decide whether profiles should be explicitly selected, eligible for automatic use, or both before creating their runtime configuration.
