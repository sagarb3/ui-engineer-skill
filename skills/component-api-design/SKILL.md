---
name: component-api-design
description: Design or revise React component props and composition boundaries with clear ownership, valid states, accessible semantics, and compatibility for existing consumers.
---

# Component API Design

## When to Use

Use when creating reusable component interfaces or changing props, events, variants, slots, or controlled state. Do not redesign a public API for an internal implementation fix.

## Process

1. Read real call sites and identify current use cases, state ownership, semantic HTML, and compatibility constraints. Ask before proceeding if consumer needs or acceptable breaking changes are unclear.
2. Expose the smallest API that expresses those use cases. Prefer descriptive props and coherent variants over interacting booleans. Follow existing naming and typing conventions; avoid generic parameters or polymorphic rendering without a present need.
3. Make controlled and uncontrolled behavior explicit. Define defaults, change callbacks, and ownership; do not switch ownership during the component's lifetime. In TypeScript, use discriminated unions when they prevent meaningful invalid combinations.
4. Support composition where consumers need it, without exporting implementation details. Forward appropriate native attributes and refs according to the installed React version and project conventions. Preserve labels, keyboard behavior, and semantic roles when allowing customization.
5. Preserve existing consumers unless an API change is authorized. For an approved change, update affected call sites and examples together. Verify representative valid usage, rejected invalid combinations where typed, and runtime interaction through the public API.

Generated code must contain no AI attribution. Write new content only in English. Keep skills-repository links, parent-agent references, authoring-tool names, and provenance text out of downstream code, comments, commits, and documentation. Preserve existing legal notices.

## Begin With Real Consumers

Read existing usages before designing props. Identify what varies, what is fixed by the domain, and what behavior consumers need to observe. A reusable component does not need to support every HTML element, every styling system, and every asynchronous pattern.

Separate domain components from low-level primitives. A billing address form may know field names and validation timing. A text-field primitive should expose useful native behavior without embedding billing rules. Do not erase useful domain meaning in pursuit of a universal abstraction.

Check whether the task changes implementation or the public contract. A rendering fix should preserve caller syntax. A new interaction may require a callback, but it does not automatically justify replacing all existing props or changing defaults.

## Props, Defaults, and Valid States

| Question | Preferred design | Risk to avoid |
| --- | --- | --- |
| Are two options mutually exclusive? | A meaningful variant or discriminated union | Independent booleans permitting contradictions |
| Is content genuinely variable? | Children or a focused slot where needed | A configuration schema for ordinary composition |
| Does a prop mirror native behavior? | Preserve its familiar meaning | Renaming a standard attribute without benefit |
| Does the next value belong to the parent? | An explicit value and change contract | Hidden duplicate state |
| Is an option only hypothetical? | Leave it out until there is a consumer | Extension points without a current requirement |
| Will a default change affect callers? | Preserve it or obtain migration approval | Silent behavior changes |

Use names that communicate domain meaning. A callback named `onSelect` should make clear whether it receives an ID, an item, or an event. Choose event-shaped callbacks when callers need event details; choose value-shaped callbacks when the contract is the value itself. Follow local conventions rather than converting every API to one style.

Define omitted, empty, null, and zero values intentionally where they differ. Do not use truthiness to replace valid empty strings or zero values with defaults. Prefer explicit status values to several booleans when they model one mutually exclusive state machine.

## Controlled and Uncontrolled State

Choose ownership for the component's lifetime. In controlled mode, the parent value determines rendering and callbacks request a change. In uncontrolled mode, an initial default seeds internal state; later default changes do not silently become controlled updates.

An illustrative TypeScript contract for a custom text value can make the two modes explicit:

```tsx
type ControlledValue = {
  value: string;
  defaultValue?: never;
  onValueChange: (value: string) => void;
};

type UncontrolledValue = {
  value?: never;
  defaultValue?: string;
  onValueChange?: (value: string) => void;
};

type TextValueProps = ControlledValue | UncontrolledValue;
```

This is a contract example, not a requirement to wrap native inputs. Adapt naming, reset behavior, and callback arguments to the actual component. Types alone do not protect JavaScript consumers or every runtime input; handle supported runtime transitions deliberately.

For a controlled component, verify a change notification does not make the UI permanently display a value the parent rejected. For an uncontrolled component, verify initial value, user editing, and the requested reset behavior. Ask if reset semantics are unspecified rather than guessing that every prop change should clear a draft.

## Composition and Escape Hatches

Use composition when it lets consumers arrange meaningful content without leaking implementation. A heading slot can be useful; exposing every internal wrapper, state setter, and layout number creates a larger compatibility burden.

Do not introduce compound components, render props, or polymorphic `as` support unless current consumers need their flexibility. If polymorphism is required, preserve valid attributes, refs, keyboard behavior, and semantic roles for the rendered element. A link styled as a button still needs link behavior.

Use explicit IDs and accessible relationships when content is split across slots. Avoid brittle child introspection, cloning arbitrary children, or reliance on a particular undocumented child order. Keep provider requirements and missing-provider errors understandable for any compound API that genuinely needs context.

Provide only the styling escape hatches the project supports. Forwarding `className` can be sufficient. Do not add both a custom style schema and several overlapping override mechanisms without a real need.

## Native Attributes, Events, and Refs

Forward useful native attributes intentionally. Check IDs, names, form association, `aria-*`, `data-*`, disabled state, and event handlers. Avoid spreading custom component-only props onto DOM elements. When internal and caller handlers both run, define their order and whether a prevented default stops internal behavior.

Set form button defaults deliberately and document them in existing examples. Native `disabled` and `aria-disabled` have different behavior. A pending action must not appear unavailable while its handler remains freely activatable unless that distinction is intentional and accessible.

Forward refs only where consumers need a stable imperative capability, such as focus. Use the installed React version's convention; do not migrate ref syntax incidentally. Prefer a narrow focus method over exposing internal mutable state, and avoid an imperative API when ordinary props express the requirement.

## Compatibility and Verification

Locate all affected consumers before renaming props, changing callback shapes, altering defaults, or moving exports. Inspect direct imports, re-exports, tests, examples, and adapters. A successful type check does not prove JavaScript consumers or runtime semantics remain compatible.

For an approved breaking change, update the actual consumers and examples together. Add a temporary adapter only when the migration requires it, with a concrete retirement condition. Do not create indefinite compatibility machinery for imagined users.

Verify the smallest representative set: ordinary use, an important edge state, controlled or uncontrolled ownership as supported, native attributes and focus, disabled or pending activation, and any changed callback. Use compile-time checks for meaningful type constraints when the project already supports them, and behavior tests for runtime contracts.

Stop when real consumers can express the accepted use cases cleanly and the compatibility impact is verified. Do not publish a component package or design a new framework as a side effect of one prop change.

## Detailed Guides

Read only the guides relevant to the current task. All guides are included in this skill folder; no companion skill is required.

| Guide | When to read |
| --- | --- |
| [Compatibility and Consumer Tests](guides/compatibility-and-consumer-tests.md) | Read before changing defaults, renaming props, moving exports, altering callback shapes, or adding a migration adapter. |
| [Composition and Native Behavior](guides/composition-and-native-behavior.md) | Read when adding children, slots, polymorphism, native attributes, event composition, or refs. |
| [Contracts and Ownership](guides/contracts-and-ownership.md) | Read when designing props, callbacks, state modes, defaults, and valid combinations. |

The [reference index](references.json) is a machine-readable map of these local files. It is a collection convention, not a client configuration or an instruction to load every guide.

## Examples

See [worked use cases and copyable prompts](examples.md) for two application scenarios, expected deliverables, and verification. Paths and outcomes are illustrative; adapt them to the actual project and report only checks that ran.

## Anti-patterns / Red Flags

- Boolean combinations with undefined behavior, ambiguous callbacks, or duplicate sources of truth.
- Universal component factories, deeply configurable schemas, and leaking internal state to consumers.
- Silently breaking callers, swallowing native attributes, or customization that removes accessible semantics.

## Verification Criteria

- Representative consumers can express current requirements without workarounds.
- State ownership, defaults, event contracts, and invalid combinations are explicit.
- Existing consumers remain compatible or were updated within the authorized change.
- Types and behavior checks pass; downstream output contains no attribution fingerprints.
