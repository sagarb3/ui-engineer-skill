# Component API Design Examples

These examples refer to consuming applications. Inspect the actual public surface and callers first. Expected outcomes are acceptance criteria, not results already observed.

## Define a Text Field's Ownership Contract

**Use case:** A shared field accepts both `value` and `defaultValue`, overwrites valid empty strings through truthiness defaults, and has unclear reset behavior.

```text
Use component-api-design to review our TextField contract and consumers.
Controlled empty strings must remain empty. Define supported controlled
and uncontrolled modes, callback arguments, and invalid combinations.
Ask about unresolved reset behavior before changing it. Preserve native
label and form attributes. Identify breaking changes and obtain a
compatibility decision before updating existing callers.
```

**Expected deliverable:** A clear proposed contract, a list of affected consumers, and focused implementation only within the authorized compatibility boundary. Types should support the runtime contract rather than substitute for it.

**Review:** Exercise empty controlled values, parent acceptance or rejection of edits, initial uncontrolled defaults, and the agreed reset path. Confirm existing callback shapes and native associations remain correct.

## Add Pending Feedback Without a Universal Button API

**Use case:** Existing callers need a pending save state, but no current requirement calls for polymorphic rendering or a custom slot framework.

```text
Use component-api-design to add pending behavior to the existing
SaveButton. Inspect real callers and current conventions. Define the
relationship between pending, disabled, activation, and accessible
feedback. Preserve native attributes, event cancellation, form type,
and existing defaults. Add only the props needed by current callers
and verify public behavior without introducing a universal factory.
```

**Expected deliverable:** A small API extension with explicit behavior and compatible consumers. Appearance must not imply duplicate-submission protection that the implementation does not provide.

**Review:** Check ordinary activation, the pending state, caller-provided disabled state, native form behavior, callback arguments, and focus. Type checking and runtime interaction address different parts of the contract.

## Useful Combination

Use `design-system-consistency` for appearance and `vitest-react-testing` for consumer behavior. Neither pairing authorizes changing unrelated exports or publishing a package.
