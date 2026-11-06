# Project Setup and Execution

Read before adding or running tests in an unfamiliar React project, or when a test fails before reaching its assertions.

## Inspect the Actual Setup

Read package scripts, lockfile, Vitest configuration, installed versions, aliases, environment, setup files, DOM matchers, cleanup, and existing render helpers. Determine whether globals are enabled and whether the project uses a simulated DOM or browser mode.

Do not assume every browser API exists in the test environment. A missing observer or native feature may require the project's approved boundary stub, a browser test, or a different verification method. Do not replace a substantial platform behavior with a fake implementation and then claim browser correctness.

## Respect Project Conventions

Use the existing file naming, location, test structure, providers, and package manager. Do not replace the runner or create an additional configuration for one test without a concrete need. Follow explicit customer naming requirements rather than assuming one universal Arrange/Act/Assert style.

Use supported installed APIs. Import test functions explicitly when globals are not configured. Load DOM matchers in the established setup rather than depending on another test's side effects.

## Run the Focused Check

Use the project's non-watch command with an appropriate file or case filter. Avoid package-manager commands that download a runner implicitly. Run required type and lint gates because test transpilation alone does not establish type correctness.

Check exit status and the actual test count. A successful command that selected zero tests is not a passing regression test. Remove accidental `.only` and inspect skipped tests that affect the accepted coverage.

## Diagnose the Right Failure

Separate configuration/import failures, missing environment capabilities, assertion failures, and cleanup leaks. Fix a test bug without weakening the product contract. Do not update snapshots or expected values merely to make the suite pass when actual behavior is wrong.

If a failure predates the task, preserve evidence and report it accurately. Do not rewrite unrelated application code to silence it. When test scope is read-only, report an application defect rather than fixing it without authorization.

## Understand the Limits

Simulated DOM tests can verify meaningful semantics and state, but they do not prove layout, clipping, real input geometry, native integration, or screen-reader behavior. Use the project's real-browser checks for those claims.

Report commands actually executed, outcomes, and missing prerequisites. Distinguish generating a test file from compiling, running, or measuring coverage.

## Verification

- Tests use the installed setup and established conventions.
- The focused command selects and executes the intended cases.
- Type and required project checks are accounted for.
- Failures are classified without weakening assertions.
- Browser-only and environment-limited claims remain explicit.
