# Composition and Native Behavior

Read when adding children, slots, polymorphism, native attributes, event composition, or refs.

## Compose Meaningful Content

Use children or focused slots when callers need content variation. Do not expose every internal wrapper or state setter. A heading slot can be useful without a schema describing all spacing, markup, and interaction decisions.

Introduce compound components, render props, or polymorphic rendering only for current use cases. Each increases the supported contract. Avoid brittle child introspection, arbitrary cloning, and undocumented child order.

If context is genuinely needed, define provider requirements and useful failure behavior. Do not add a provider solely to avoid passing one ordinary prop.

## Preserve Element Semantics

A link styled like a button still needs navigation behavior; an action needs button behavior. Polymorphism must retain attributes, refs, keyboard expectations, and accessible relationships appropriate to the rendered element.

Forward useful native attributes intentionally, including IDs, names, form association, descriptions, `aria-*`, and `data-*`. Do not spread component-only props onto the DOM. Check whether internal defaults override caller values deliberately or accidentally.

## Events and Pending State

When internal and caller handlers both run, define order and the meaning of a prevented default. Do not silently swallow caller behavior or run a destructive action after the caller cancelled it.

Choose button types explicitly in forms. Native `disabled` and `aria-disabled` have different effects; implement the accepted interaction consistently. Pending appearance should not imply duplicate-submission protection that does not actually exist.

## Refs and Escape Hatches

Use the installed React version's supported ref convention. Do not migrate ref syntax incidentally while fixing a local prop. Expose a stable focus capability when necessary rather than the component's entire internal state.

Offer styling escape hatches that fit the current system. A `className` or documented slot may be sufficient; overlapping style objects, schemas, and variant overrides create ambiguous precedence.

Preserve accessible names and ID relationships when content is split across slots. A flexible API is incomplete if ordinary consumers cannot label or focus it correctly.

## Verification

- Composition serves real caller variation without leaking internals.
- Native attributes and semantics survive wrappers.
- Handler order and cancellation behavior are explicit.
- Disabled, pending, form, and focus behavior remain correct.
- Refs and styling escape hatches fit installed conventions.
