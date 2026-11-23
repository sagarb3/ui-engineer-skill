# Skill Evaluations

This suite contains 50 original cases across all ten skills. It covers ordinary behavior, ambiguity, scope boundaries, pressure to bypass safeguards, activation, and a multi-turn mode change. The fixtures are synthetic local examples, not copied projects or evidence about a live application.

## What the Tool Does

`scripts/evaluate.py` uses Python 3.9 or later and Git. It validates collection data, creates isolated local evaluation workspaces, and summarizes criterion reviews backed by evidence files. It does not call a model, automate a client, download dependencies, contact remotes, or independently judge response quality.

Preparation is not an evaluation run. A new review starts with every criterion marked `unverified`, and its outcome is `incomplete`. A reviewer must observe candidate behavior before recording a verdict. Passing the tool's own tests is not a passing skill evaluation.

## Files and Contracts

- `cases/<skill>.json` defines the task prompt, fixture, activation mode, optional follow-up turns, and review criteria.
- `fixtures/<skill>/` contains only the initial task context and source material.
- Each installed skill's `references.json` maps its local guides; the main instructions remain in `SKILL.md`.
- Prepared run directories hold the candidate workspace, prompt, setup manifest, and review template separately.

The JSON formats are conventions of this collection, not universal client configuration formats. Schema version 1 is enforced by the repository tool. Do not assume a client automatically loads evaluation or reference JSON.

An evaluation suite has `schema_version`, `skill`, and a nonempty `cases` array. Each case has a unique `id`, a category, `activation` (`explicit` or `discovery`), `prompt`, a local `fixture` path, and criteria with stable IDs and descriptions. Optional `turns` describe later user messages. Optional `working_tree` changes and `setup_branches` support local Git scenarios.

A reference index has `schema_version`, `skill`, and `references`. Each reference has `id`, `title`, a skill-relative Markdown `path`, and `when_to_read`. Every guide must be linked from its skill and indexed. Index paths cannot escape the skill folder.

## Validate and Prepare

Run from the repository root:

```sh
python3 scripts/evaluate.py validate
python3 scripts/evaluate.py list
python3 -m unittest discover -s tests -v
```

Prepare a treatment and a separate baseline:

```sh
evaluation_directory="$(mktemp -d)"
python3 scripts/evaluate.py prepare harness.focused-edit "$evaluation_directory/treatment" --client copilot
python3 scripts/evaluate.py prepare harness.focused-edit "$evaluation_directory/baseline" --mode baseline --client copilot
```

Destinations must not exist and must be outside this checkout. The tool never overwrites a previous run. A preparation error can leave a partial directory; inspect it and choose a new destination rather than deleting user files automatically.

Supported client destinations are Copilot, Cursor, Codex, Claude Code, and OpenCode. The treatment installs the complete selected skill folder in that client's project skill location. The baseline does not install it. Both use the same source fixture and case. Explicit-activation treatment adds a request to use the skill; discovery cases receive no activation hint.

Preparation initializes a local Git repository with a sample commit using a fixture-only identity, disabled hooks and signing, and isolated Git configuration. It does not change the user's identity, global configuration, hooks, or real repositories. No remote is configured. History-pressure cases can supply hypothetical conditions in the prompt; they do not establish a real remote integration test.

## Run the Candidate Through the Chosen Client

Start the selected client in the prepared `workspace/` and supply the text of `prompt.md`. Constrain it to that workspace and the permitted local task. Do not expose sibling review files, the original case criteria, or the expected answer to the candidate. For multi-turn cases, send the later messages in order and preserve the complete transcript.

The operator controls the client and records its version, model, permissions, installed personal instructions, and relevant settings. Use supported client isolation when available. If global skills or prior context cannot be excluded, record the contamination rather than describing the baseline as clean. Do not disable protections or modify global settings to run the benchmark.

Model or provider calls can cost money and require separate availability and authorization. This repository supplies no credentials or automatic paid-model runner. Do not infer that the examples above authorize such calls.

The React and TypeScript fixtures are source-only. They intentionally do not provision a React toolchain or download a package manager's dependencies. Supply an existing controlled environment explicitly if executable React tests are needed, and keep it identical across conditions. Otherwise record compilation, tests, and browser behavior as unverified. The harness JavaScript fixture has an executable dependency-free Node test.

Keep evaluator-provided fixtures and transcripts separate from final product code. Inspect product diffs for English-only content and workflow attribution, excluding the intentionally installed instruction package itself.

## Review and Score

Read the actual transcript, tool log, changed files, test outputs, and applicable browser evidence. For each criterion in the prepared `review.json`, retain its ID and description and set:

- `passed`: observed evidence satisfies the criterion.
- `failed`: observed evidence contradicts the criterion.
- `unverified`: evidence is missing, blocked, or insufficient.

For a passed or failed verdict, add at least one evidence object with a run-relative `path` and an explanatory `note`. For example:

```json
{
  "id": "check-1",
  "description": "Retain the exact description from the prepared review.",
  "status": "passed",
  "evidence": [
    {
      "path": "transcript.txt",
      "note": "The recorded interaction and result support this criterion."
    }
  ]
}
```

This is a format example, not an evaluation result. Evidence must exist and be nonempty. Prompts, manifests, and review templates are not execution evidence. A reviewer-written verdict is still a judgment; the tool validates its structure and evidence references, not the truth of every sentence in a transcript.

```sh
python3 scripts/evaluate.py score "$evaluation_directory/treatment"
```

Any failed criterion makes the case `failed`; otherwise any unverified criterion makes it `incomplete`; only all passed criteria produce `passed`. Missing, duplicated, changed, or unknown criteria are rejected. Changing a case after preparation requires a new run. Manifest hashes identify the case, source fixture, and treatment skill content used at preparation time.

## Compare and Report

Compare baseline and treatment with the same model, environment, permissions, starting data, and review standard. Preserve raw evidence and report run counts, failures, incomplete criteria, and costs only when actually observed. Repeat runs when variability matters; one successful example is not a reliability estimate.

Keep structural validation, tool tests, manually reviewed behavior, and model-based evaluation results separate. Do not publish a fabricated pass rate or infer superiority from the number of cases authored. No behavioral results are bundled by default.
