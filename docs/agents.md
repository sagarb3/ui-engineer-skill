# Skills, Metadata, and Specialist Agents

A skill is a workflow loaded for a relevant task. A specialist agent is a separately configured role or execution context. Installing a skill does not create an agent, and a file under a skill's `agents/` directory is not necessarily an executable agent definition.

## What Is Included

Every skill includes `agents/openai.yaml` with its display name, short description, and an invocation example. This is skill UI metadata. It does not launch a process, configure automatic delegation, choose a paid model, or grant additional permissions.

The reference indexes and evaluation cases describe content and verification. Neither is a runtime orchestration configuration. The evaluation tool prepares local workspaces and records reviewer judgments; it does not create model sessions.

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
