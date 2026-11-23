# Contracts and Ownership

Read when designing props, callbacks, state modes, defaults, and valid combinations.

## Start From Consumers

Inspect real call sites, current use cases, installed types, and compatibility requirements. Separate a domain component from a low-level primitive. A reusable address form can know address rules; a text-field primitive should not inherit those business assumptions.

Expose only variation current consumers need. Do not add generic parameters, a configuration schema, or several extension points to support hypothetical future callers.

## Model Valid States

Use coherent variants or discriminated unions when they prevent meaningful contradictions. Independent booleans are appropriate only when their combinations make sense. Avoid an interface where `loading`, `failed`, and `complete` can all be true without a defined meaning.

Define omitted, empty, null, and zero deliberately. Truthiness defaults can overwrite valid empty strings or zero values. Preserve existing defaults unless their change is authorized.

## Define Callback Meaning

Specify whether a callback receives an event, a value, an ID, or a domain object. Follow local conventions and the consumer's actual need. Avoid vague callbacks whose arguments reveal implementation state rather than a useful public outcome.

Define whether a change callback reports an accepted result or requests a parent-owned update. Do not display success or permanently update controlled output when the parent rejects the request.

## Controlled and Uncontrolled Modes

In controlled mode, the parent value determines rendering. In uncontrolled mode, an initial default seeds internal state and the component owns subsequent edits. Do not switch ownership silently or reinitialize drafts on every prop update.

Use types to distinguish modes where the project supports them, but preserve runtime behavior for JavaScript consumers too. Type-level exclusivity alone cannot repair an undefined reset policy.

Clarify initialization, reset, record switching, cancellation, and submitted-state behavior. A field's default changing is not automatically an instruction to erase current input.

## Verification

- Current consumers can express the accepted use cases directly.
- Defaults and empty-value meanings are explicit.
- Invalid combinations are prevented or handled deliberately.
- Callback arguments and ownership are clear.
- Controlled, uncontrolled, reset, and prop-change behavior follow the contract.
