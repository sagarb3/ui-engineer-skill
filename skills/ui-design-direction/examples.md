# UI Design Direction Examples

These are hypothetical product briefs. Supply the real route, constraints, content, and assets. Expected deliverables are acceptance criteria, not evidence that a browser review has happened.

## Redesign an Inventory Working Surface

**Use case:** Warehouse staff must find low-stock items and request replenishment. A large welcome section currently pushes the queue and actions below the first viewport.

```text
Use ui-design-direction to redesign the inventory workspace. Preserve
the existing navy-and-white identity, navigation, and component library.
Prioritize low-stock exceptions, keep filters near results, and make the
restock action discoverable. Use realistic item data. Cover loading,
no matching results, request pending, failure, and success. Define the
responsive behavior, then inspect the rendered main path at the target
desktop width and a representative narrow width. Ask about unresolved
product choices before implementation.
```

**Expected deliverable:** A concrete design direction, a focused implementation using existing primitives, and evidence for the changed hierarchy and workflow. The task should not become a brand replacement, a decorative marketing hero, or a second design system.

**Review:** Check whether the important item, decision context, and next action are visible together. Operate the restock flow separately from judging its appearance. Browser, motion, and independent-review claims require actual evidence.

## Compare Layouts Without Building Two Products

**Use case:** A team is deciding between an inline detail panel and a drawer for selected inventory items.

```text
Use ui-design-direction to compare two inventory layouts: an inline
detail panel and a selection drawer. Use the same data, palette, type,
and target viewport. Show the selected-item state and how the primary
action stays reachable. Deliver a bounded comparison with tradeoffs;
do not implement two complete applications or choose silently for us.
```

**Expected deliverable:** Comparable representative views with meaningful structural differences, clear tradeoffs, and a selection boundary. A theme swap or stronger shadow is not a second layout.

**Review:** Inspect at actual reading size, not only as thumbnails. Check content parity, the action path, and feasibility with the existing stack. Static previews should be identified as static.

## Relevant Guides

Use [brief and exploration](guides/design-brief-and-exploration.md), [responsive reconstruction](guides/responsive-reconstruction.md), [visual review](guides/visual-review.md), and [usability walkthrough](guides/usability-walkthrough.md) for the parts that apply.
