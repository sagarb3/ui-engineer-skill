# Semantic Controls and Forms

Read for labels, field feedback, native semantics, accessible names, and validation behavior.

## Match the Element to the Action

Use a button for an action and a link with a real destination for navigation. Preserve native keyboard and form behavior. A clickable generic container with a role is not automatically equivalent to the native control.

Keep visible labels and accessible names consistent. An icon-only control needs a meaningful name, while a decorative icon beside text usually should not add a second announcement. Avoid replacing a useful visible label with an unrelated `aria-label`.

## Associate Information Deliberately

Use unique IDs to connect labels, instructions, and errors. Descriptions support the control's purpose; they should not become a dump of every surrounding paragraph. Repeated field components must not generate duplicate associations.

Keep labels available after input. Placeholder text cannot be the only label. Preserve standard editing, paste, autofill, and password-manager behavior. Use suitable input type and autocomplete semantics according to the actual field contract.

## Choose Validation Timing

Clarify when validation should appear: during editing, after leaving a field, or after submission. Do not announce an untouched empty form as invalid merely because required values are absent initially unless the product explicitly requires that behavior.

When validation fails, identify the affected field and the needed correction in text. Associate the message with the field and expose invalid state truthfully. Preserve recoverable input rather than resetting the form on rejection.

For a multi-field failed submission, use the project's summary and focus pattern when relevant. Links in an error summary should lead to the actual invalid controls. A toast alone is usually insufficient to explain several field errors.

## Dynamic Results

Use status announcements for meaningful asynchronous feedback without stealing focus. Reserve urgent announcements for truly urgent information. Do not flood a live region with every keystroke, count update, or decorative state change.

`aria-disabled` communicates a state but does not prevent activation. Implement behavior consistently when native disabling is not appropriate. Preserve a clear label and useful progress indication during pending work.

Client feedback does not replace server validation, authorization, or rate limits. Accessibility fixes must not move security responsibilities into the browser.

## Verification

- Controls expose accurate names, roles, values, and states.
- Labels, descriptions, and errors remain associated in repeated forms.
- Validation timing and recovery match the product contract.
- Keyboard editing and native integrations remain usable.
- Dynamic feedback is discoverable without excessive announcements.
