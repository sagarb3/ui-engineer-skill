# Focus and Composite Widgets

Read for dialogs, menus, tabs, comboboxes, disclosure groups, and focus after changing content.

## Choose the Interaction Pattern

Similar visual layouts can have different keyboard contracts. A menu, navigation list, select, and editable combobox are not interchangeable. Identify the intended task and reuse the installed accessible primitive that fits it.

Use normal document order for ordinary controls. Avoid positive `tabIndex` or making every visible label focusable. Composite-widget arrow navigation applies to the selected pattern, not every group of buttons.

## Modal Dialogs

Verify the accessible name, appropriate initial focus, contained focus while modal, inactive background, supported dismissal, and a reachable close action. Do not assume focusing the first input is right for every dialog; explanatory content or a consequential action may need a different initial target.

Restore focus to the trigger or a logical successor if the trigger no longer exists. Check content and close controls with long text, narrow height, and the virtual keyboard. The modal must not trap users in a region whose action or exit is unreachable.

Do not duplicate focusable content during entrance and exit animations. A visually hidden old panel can still interfere with keyboard and assistive-technology navigation.

## Selection and Navigation Widgets

Follow the established primitive's selected, expanded, active-descendant, and keyboard model. Keep focus state distinct from selection where the pattern requires it. Do not update ARIA state without implementing the corresponding behavior.

For tabs or selectable collections, define whether focus movement also activates the item. For a combobox, preserve text editing and the accepted completion/cancellation model. Ask about unresolved interaction requirements instead of copying keyboard handlers from another widget.

## Content Replacement

After deleting a row, changing a route, or replacing a region, choose a logical focus destination consistent with the task. Do not send focus to the document body or an unrelated top-level control simply because the original node disappeared.

Keep focus visible and not obscured by sticky headers, footers, or overlays. Scrolling a focused element into view must not break the user's reading or interaction context.

## Verification

Walk the affected path with keyboard only. Open, operate, cancel, close, reverse, and repeat as relevant. Test the state where the trigger disappears or content changes. Then inspect with the relevant assistive technology when available.

- The widget pattern matches the actual user task.
- Focus order, visibility, containment, and restoration are predictable.
- Selection and expanded state remain truthful.
- Motion and content replacement do not leave duplicate or lost targets.
- Unsupported assistive-technology checks are reported rather than assumed.
