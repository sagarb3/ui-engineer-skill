# Task Artifacts and Design Rules

Use when a UI task produces candidates, raw images, recordings, screenshots, investigation notes, or proposed design rules. Keep working material separate from the application without inventing a new project structure for every task.

## Respect Existing Locations

User-specified paths and repository conventions come first. Inspect applicable instructions and current design documents before creating anything. Keep product code, formal tests, final documentation, and runtime assets in their established project locations.

Use the existing task workspace or an environment-provided temporary directory for transient material when no project convention exists. Create only the subdirectories the actual task needs. Do not add a collection-branded folder, metadata file, or comment to the application.

Check whether a destination already exists and belongs to the current task. Do not overwrite another task's candidate set. If a destination is a file, points elsewhere through a symlink, or has unclear ownership, stop and clarify before writing through it.

Never clear old task directories to create a clean-looking workspace. Deletion and branch/file cleanup require the user's authorization. An ignored directory is not disposable merely because Git does not track it.

## Separate Working and Final Material

| Material | Appropriate location | Delivery rule |
| --- | --- | --- |
| Unselected concepts and comparison previews | Existing task workspace or temporary location | Do not bundle them with the product by default |
| Raw downloads, intermediate crops, image candidates | Working asset area | Promote only selected, rights-cleared output |
| Screenshots and recordings | Approved evidence area | Keep them out of application dependencies |
| Final images, fonts, or models | Existing project asset location | Verify every runtime reference resolves |
| Maintained rules and approved examples | Existing design documentation | Update only within the requested scope |
| Tool logs, private notes, or sensitive fixtures | Protected task context where appropriate | Never publish or commit inadvertently |

Final code must not depend on a temporary image, local absolute path, private preview URL, cached download, or comparison iframe. Promote the actual approved assets to stable locations and update their references together.

Do not change global ignore rules or repository configuration merely to hide task output. Respect existing local ignore behavior. If temporary files appear in status, identify them and keep them unstaged rather than deleting them or broadening configuration silently.

## Keep Paths and Runtimes Clear

Separate the server root, current working directory, asset base URL, and evidence output path. A screenshot destination does not determine where a server resolves imports. A path that works inside a task workspace may fail when copied into application code.

For comparison previews, keep candidate identity and revision unambiguous. The same short label in a later round must not silently refer to an earlier file. If the user selects an option, verify which set is current and record the selection in existing task context.

Do not build a new artifact-management script unless repeated real work demonstrates a need. Clear paths and a small amount of task context are usually sufficient.

## Reconcile Existing Design Rules

Inspect current design documents, theme tokens, component exports, and representative screens. Distinguish explicit approved rules from observed conventions and proposed changes. A frequent implementation pattern is evidence, not automatically a new policy.

When documents disagree with each other or with the running product, identify the conflict, affected surface, and practical consequence. Ask which authority should govern the change when the answer is not established. Do not silently merge, replace, delete, or rewrite design documents to eliminate the disagreement.

For a task that explicitly requests documenting an existing design system, separate confirmed decisions, observed behavior, and unresolved questions. Keep inferred rules labeled until confirmed. Do not write a speculative direction as though the user approved it.

Update the existing canonical document rather than creating parallel standards. Keep links, examples, and affected consumers consistent when a change is authorized. Avoid adding a design document during an unrelated small fix simply to memorialize the work.

## Isolation, Rights, and Sensitive Material

Do not put skills-collection names, source-repository links, authoring-tool names, generation logs, or parent-agent references in downstream code, comments, commits, or product documentation. Keep normal product explanations in ordinary engineering language.

Preserve required licenses, legitimate ownership records, and unrelated attribution. Output isolation is not permission to remove legal notices. Keep prompts, private screenshots, credentials, customer data, and service tokens out of published assets and evidence. Strip accidental sensitive metadata through an appropriate supported process when needed, while retaining records the license requires.

An asset being publicly viewable does not establish redistribution rights. Confirm rights before promotion into final application assets. Do not upload source material to an external service without authorization.

## Delivery Audit

Inspect Git status and the final diff. Review untracked files directly because an ordinary diff omits their contents. Confirm that only intended final files are staged if staging was requested, and preserve pre-existing user work.

Check asset paths, case-sensitive filenames, imports, route entry points, and required runtime configuration. Confirm that the application can work without the task directory. Run existing build and relevant checks when appropriate.

Provide final file locations and the evidence needed for review, with any unverified conditions. Do not publish the site, push a branch, or upload the evidence without task authorization. Stop once the accepted deliverable and verification are complete.

## Verification

- Working files and final application files have clear, established destinations.
- No existing files, task history, or design rules were overwritten or deleted without authorization.
- Final runtime dependencies resolve independently of temporary material.
- Approved rules, observations, and proposals remain distinguishable.
- The delivered diff contains no accidental secrets, provenance, or unrequested artifacts.
