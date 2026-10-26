# Implementation Decisions

Read when applying the trimming ladder to a concrete feature or bug. Minimal means the smallest complete solution, not the fewest visible lines.

## Work Down the Ladder

First establish the accepted behavior and inspect affected code. An unclear request does not become clear because the shorter implementation is attractive. Ask about unresolved product choices.

Check whether the proposed addition is necessary, whether the repository already owns the behavior, whether platform capabilities fit, whether an installed dependency solves the whole contract, and whether a direct expression is readable. Only then add custom logic.

Treat existing architecture as evidence. A project field primitive may be preferable to a raw native input because it already carries labels, error associations, and theming. An installed package may still be unnecessary for a simple expression. Do not mechanically prefer one category without checking behavior.

## Count the Complete Cost

Include caller changes, error paths, types, tests, and maintenance burden. A one-line expression with a subtle null or mutation bug is more expensive than a few explicit lines. A wrapper that saves two call-site characters but creates a new public API may not reduce complexity.

Do not use shortening as a reason to remove descriptive names, useful types, or meaningful intermediate values. Avoid chained ternaries and clever coercions that make edge cases harder to see.

## Decide Whether to Extract

Extract around a real lifecycle, domain boundary, or repeated behavior. Do not create a helper for every expression or a generic factory for one component. Conversely, do not duplicate validation across several callers just to avoid an extra file.

If an abstraction's purpose can only be explained by a hypothetical future feature, leave it out. If a current consumer requires configurability, expose only that dimension and verify its contract.

## Concrete Examples

A visible count derived from current records normally needs no synchronized state. A local disclosure normally needs no application-wide store. A single known formatting rule may use the installed formatter or platform API instead of a new dependency.

These are starting points, not universal answers. Shared persistence, locale rules, request caching, or a documented architecture can justify a different owner. Preserve the actual requirement rather than choosing the easiest example to copy.

## Verification

- Every addition serves a present requirement.
- Existing capabilities were inspected rather than assumed.
- The chosen solution includes required callers and failure paths.
- Readability and safeguards remain intact.
- No mode-specific provenance or special attribution appears in product code.
