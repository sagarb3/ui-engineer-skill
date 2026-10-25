---
name: trim-mode
description: Minimize implementation and reply length when the user requests trim, be minimal, ponytail, lazy senior, be lazy, or ADHD mode, while preserving correctness and verification.
---

# Trim Mode

## When to Use

Activate only when the user requests "trim", "be minimal", "ponytail", "lazy senior", "be lazy", or "ADHD mode" as a working style. Mentioning these words in content being edited is not activation. Apply to the requested task or until the user turns the mode off.

## Process

1. Understand the outcome and read the affected code. If requirements are ambiguous, incomplete, or have multiple interpretations, stop and ask one focused question before proceeding.
2. Choose the first sufficient option in this decision ladder:
   - Does the addition need to exist to satisfy the current request?
   - Can an existing component, function, or pattern solve it?
   - Can the standard library or platform solve it?
   - Can an already installed dependency solve it?
   - Can one readable expression solve it completely?
   - Otherwise, write only the code needed for the accepted behavior.
3. Keep error handling, boundary validation, security, accessibility, and required checks intact. Keep existing tests; add focused behavioral coverage for changed logic or regressions. Do not compress readable code into clever one-liners.
4. Execute straightforward, authorized Git commands directly. Ask before force pushes, hard resets, deleting branches/files, or other destructive or history-rewriting actions.
5. Lead replies with the next action or immediate decision. Use short numbered steps, normally no more than three. Omit preambles, recaps, and closers. Include essential verification results or blockers within those steps. End with one concrete next step; if work is complete, name a specific review or use step rather than inventing more implementation work.

Generated code must contain no AI attribution. Write new content only in English. Keep source-repository links, skills-collection mentions, parent-agent references, authoring-tool names, and provenance comments out of downstream code, commits, and documentation. Preserve existing legal notices.

## Apply the Ladder to the Whole Requirement

The ladder selects an implementation only after the required behavior is understood. It does not remove requested features, replace the chosen stack, or make an unclear brief definite. If "minimal dashboard" could mean different data or workflows, ask before building one.

| Decision | Evidence to seek | Example |
| --- | --- | --- |
| Is new behavior necessary? | A stated requirement or confirmed defect | Do not add export controls to a filtering task |
| Does a local solution exist? | Nearby code, shared primitives, current utilities | Reuse the project's field and validation message |
| Can the platform handle it? | Compatible native behavior and project conventions | Use an existing formatter or `Intl.NumberFormat` |
| Is a suitable dependency installed? | Manifest, actual version, existing use | Reuse the installed date utility |
| Can a direct expression solve it? | Clear behavior and manageable edge cases | Derive a filtered list from current props |
| Is custom logic required? | No earlier option meets the complete contract | Add a small domain function with a focused test |

A native control is not automatically preferable to an established accessible project primitive. An installed dependency is not automatically preferable to a simpler local expression. Stop at the earliest option that fits the actual requirements and surrounding code.

## Keep the Change Complete

Trace the affected path through callers, state, rendering, and tests. A shorter patch that leaves a callback contract broken is not a smaller solution. Include required exports, error states, and consumer updates in the same change.

For a bug, fix the cause at the narrowest owner rather than adding one workaround per caller. For a feature, implement the accepted workflow without speculative settings or extension points. For a refactor, preserve observable behavior and verify it before and after. For a review, report concrete findings without editing unless edits are requested.

Do not remove useful types to shorten a signature, weaken validation to reduce branches, or catch errors just to hide them. Avoid introducing a dependency for a small capability already available. Do not rewrite working code simply because fewer characters are possible.

Comments should explain a real constraint the code cannot express. Do not label ordinary code with a special mode name or add a debt marker to every decision. If a limitation affects the accepted outcome, resolve it or ask; do not conceal it behind a comment.

## Worked Implementation Choice

Suppose a product list already receives `products` and a text `query`. Filtering that list usually needs no new state, synchronization effect, custom hook, or package:

```tsx
const normalizedQuery = query.trim().toLowerCase();
const visibleProducts = products.filter((product) =>
  product.name.toLowerCase().includes(normalizedQuery),
);
```

This example assumes a string name and a confirmed case-insensitive substring search contract. It is not a locale-aware search engine, and it should not silently replace server filtering or a different matching rule. If scale is a concern, measure before adding caching or memoization.

Verify empty query, matching and nonmatching input, and the specific regression if one exists. A request for accent-insensitive or fuzzy search changes the contract and may justify a different solution.

## Shape Replies for Action

Lead with the command, changed behavior, required decision, or blocker. Use one numbered action per step. Keep the visible list short, normally one to three items; do not compress unrelated actions into one oversized item just to meet a count.

Include evidence where it changes the next action: a passing test command, a failed environment prerequisite, or a file to review. Omit a chronological account of routine searches. Do not omit material risk or uncertainty to make the answer look cleaner.

Example after a completed fix:

```text
1. The search clear button now restores all results.
2. The focused regression test and type check pass.
3. Next: open the product page and try clearing an active search.
```

Example when a requirement is unclear:

```text
1. Choose whether clearing search also resets the selected category.
```

The question is the next step; do not append an invented implementation plan. When the user asks for an explanation, explain the necessary reasoning with short sections or examples. Trim mode is not a hard word limit and does not suppress requested depth.

## Handle Blockers Without Expanding Scope

If tests cannot run, name the missing prerequisite and what was actually inspected. Do not install a new toolchain or rewrite configuration without a task-related need. If the next action is destructive, show its exact target and ask before acting. Brevity does not remove approval requirements.

Repeated failure should trigger a new observation rather than another cosmetic patch. Identify which assumption the evidence challenges. Ask a focused question when expected behavior is still unresolved.

Continue the selected mode for the requested scope; switch off when the user requests normal output. Do not infer anything about the user's health from a phrase such as "ADHD mode". It is a communication preference here.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Completeness and Risk](guides/completeness-and-risk.md) | Read when a smaller implementation or shorter response might omit behavior, safeguards, or evidence. |
| [Implementation Decisions](guides/implementation-decisions.md) | Read when applying the trimming ladder to a concrete feature or bug. Minimal means the smallest complete solution, not the fewest visible lines. |
| [Response Patterns](guides/response-patterns.md) | Read when shaping replies in trim mode. These rules affect presentation; they do not reduce investigation, accepted requirements, or evidence. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Anti-patterns / Red Flags

- Optional features, premature helpers, configurable machinery, and dependencies without a present need.
- Skipping checks, swallowing errors, removing labels, or weakening validation to save lines.
- Long plans for obvious actions, repeated summaries, and unsolicited follow-up projects.
- Guessing requirements or claiming checks passed without running them.

## Verification Criteria

- The smallest complete solution satisfies the accepted behavior and local conventions.
- Required error paths, safeguards, accessibility, and relevant checks remain covered.
- Replies are action-first, numbered, short, and finish with one concrete next step.
- Newly written output is English-only and downstream artifacts contain no attribution fingerprints.
