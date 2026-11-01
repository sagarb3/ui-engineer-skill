# Usability Walkthrough

Use to check whether someone can understand the interface and complete an important task. A visual critique asks how the screen communicates; this walkthrough asks what a user can actually do and understand through the interaction.

## Choose the Kind of Walkthrough

For acceptance testing, use the confirmed task and expected outcome. For an exploratory first-use walkthrough, begin with the visible page and identify what it appears to offer before reading implementation rationale. Do not confuse these methods or claim that one establishes the other.

If a separate reviewer is authorized and available, provide the entry point, intended device conditions, necessary test materials, and safety boundaries. Avoid giving a rehearsed click sequence when the question is discoverability. If performing the walkthrough yourself, acknowledge prior knowledge rather than describing it as independent first-use evidence.

Do not create extra reviewers by default or claim a separate review happened when it did not. A useful self-check is preferable to fictitious independence.

## Set Safe Boundaries

Use local or designated test data and existing approved test accounts. Identify which actions mutate state and which could send messages, spend money, publish, delete, or affect another person. A request for a UI review alone does not authorize those external consequences.

Stop before a consequential step without the required authorization. Record where the walkthrough stopped and what result remains unverified. Do not fabricate successful completion or use a dangerous live operation merely to make the report look complete.

Keep secrets out of screenshots, recordings, URLs, and reports. If the environment lacks a safe test path, ask for the missing environment or authority while continuing read-only inspection where useful.

## Start From What Is Visible

Before acting, describe the apparent product, target user, and likely main task in plain language. Check whether the page provides a clear starting point, sufficient context, and understandable action labels.

Choose one representative primary path rather than clicking every control. Include its real entry point; do not start from a hidden deep link that bypasses the navigation problem being evaluated. For an established acceptance case, preserve its required entry and outcome.

An unclear starting point is an observation, not proof that every user will fail. Record it with the evidence and the interpretation that led to the next action.

## Observe Each Transition

Record what was visible, the action chosen, the expected result, the actual result, and the resulting state. The record should support a concrete diagnosis without relying on the implementer's intention.

```text
Visible: A selected invoice and a button labeled Send.
Expected: A chance to inspect the recipient before sending.
Action: Open the supported safe preview path.
Result: The preview shows the recipient and a clear return action.
Limit: Live sending was outside the walkthrough's authorization.
```

For each important step, check discoverability, input requirements, progress feedback, outcome clarity, and recovery. Distinguish inability to proceed from an unexpected result or a decision requiring guesswork. Do not create artificial confusion, but do not fill missing context from source knowledge.

Check whether validation identifies the actual field, whether a failure preserves entered data, and whether retry or cancellation has a predictable result. Observe pending states rather than assuming the interface is frozen because a response takes time.

## Complete and Verify the Outcome

Confirm an observable result appropriate to the contract: a changed record, an added item, a saved draft, or a navigated view. A toast alone may not prove durable persistence. If persistence is required, use a safe reload or read-back through the supported path and verify that the result remains.

Check back navigation and restoration when they are part of the flow. Verify that the user understands whether work is complete, still pending, or failed. If the actual state is unknown after an interrupted request, inspect the authoritative result before retrying a potentially non-idempotent action.

Use keyboard traversal for the relevant path and any supported alternate input. A pointer-only success does not establish keyboard usability. Mark sound, haptics, native integrations, and device-specific behavior unverified when the environment cannot observe them.

## Report Evidence, Then Interpretation

For each material finding, separate:

- Observed fact: location, input, action, result, and supporting evidence.
- Interpretation: why the presentation or interaction may cause the problem.
- Desired correction: the outcome the interface should make possible or clear.

Rank findings by effect on task completion rather than aesthetic preference. Keep the report focused on meaningful obstacles. A tool crash, missing fixture, or unavailable backend is not automatically a product defect; reproduce or label the uncertainty.

Report the path actually taken and whether it completed, partially completed, or stopped. State the remaining limits. Do not invent user success rates, satisfaction, task-time estimates, or general population conclusions from a single walkthrough.

## Re-check Corrections

When fixes are authorized, reproduce the reported issue and verify the repaired transition. Then complete the affected path with its recovery behavior. Do not solve discoverability only by adding a paragraph telling users how to work around the interface.

A targeted re-check is normally sufficient. Repeat an independent walkthrough only when requested or when a major interaction change creates a new question that the original evidence cannot answer.

## Verification

- The method, environment, input conditions, and safety limits are clear.
- A real path was observed from a meaningful entry to the supported outcome.
- Facts, hypotheses, product defects, and tool failures are distinguished.
- No live external consequence occurred without authorization.
- Independence, persistence, accessibility, and other claims match actual evidence.
