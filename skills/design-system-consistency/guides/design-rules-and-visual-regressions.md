# Design Rules and Visual Regressions

Read when documentation conflicts with implementation, visual baselines change, or a UI task affects shared rules.

## Separate Rules From Observations

Identify explicit approved rules, observed conventions, deprecated patterns, and proposed changes. A repeated implementation is evidence, not automatically a new standard. A design document may be stale without granting permission to rewrite it.

When rules disagree, describe the conflict and the affected outcome. Ask which authority governs an unresolved decision. Do not merge or delete documents simply to make the repository appear consistent.

If documenting an existing system is requested, label inferred conventions until confirmed. Update the existing canonical document rather than creating parallel standards with subtly different rules.

## Establish Comparable Visual Evidence

Compare the same route, content, viewport, fonts, theme, and state. A changed screenshot caused by different fixtures or missing assets does not establish a design regression. Inspect captures before using them as evidence.

For existing-product polish, assess hierarchy, alignment, spacing, text roles, control dimensions, focus, and error treatment within the current identity. Do not recommend a new font or palette solely because it matches personal taste.

## Handle Baselines Intentionally

If visual tests exist, inspect the actual difference before accepting a new baseline. Do not update all snapshots automatically to make checks pass. Confirm that each changed region is intended and that unrelated states are unaffected.

If screenshot differences are nondeterministic, fix or control the source where suitable. Mask only regions allowed by the project's policy; do not mask the changed component or hide a real failure.

## Bound the Review

Re-check the changed region and shared consumers it can affect. Add more evidence when a specific unresolved risk warrants it. A small token correction does not require a new design-system audit unless its shared impact actually reaches that far.

State whether checks were code-only, rendered, automated, or manually operated. A static screenshot cannot prove keyboard behavior or transition quality.

## Verification

- Approved decisions, observed patterns, and proposals remain distinguishable.
- Conflicts are clarified rather than silently resolved.
- Visual comparisons use consistent conditions and current evidence.
- Baseline updates represent intentional changes only.
- Review scope and unverified claims remain explicit.
