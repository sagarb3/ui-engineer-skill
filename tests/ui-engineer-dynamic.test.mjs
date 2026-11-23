import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const source = await readFile(
  new URL("../skills/ui-engineer/templates/dynamic-review/workflow.mjs.template", import.meta.url),
  "utf8",
);
const { uiReview } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

function context(path, result = { findings: [] }) {
  const calls = [];
  return {
    args: { path }, calls,
    phase(name) { calls.push({ phase: name }); },
    async agent(prompt, options) { calls.push({ prompt, options }); return result; },
  };
}

test("reject traversal, unexpected roots, and injected arguments before delegation", async () => {
  for (const path of ["packages/ui/../../secrets.ts", "apps/web/./src/A.tsx", "apps/web//A.tsx", "docs/A.tsx", "packages/ui/A.tsx;touch pwned", "/apps/web/A.tsx", null, "apps/web/" + "a".repeat(250) + ".tsx"]) {
    const ctx = context(path);
    await assert.rejects(uiReview.run(ctx), /Provide one source file/);
    assert.equal(ctx.calls.filter((call) => call.prompt).length, 0);
  }
});

test("review one approved file and return source-only evidence", async () => {
  const ctx = context("packages/ui/src/Button.tsx", { findings: ["Use a native button for keyboard activation."] });
  const result = await uiReview.run(ctx);
  assert.deepEqual(result, { path: ctx.args.path, findings: ["Use a native button for keyboard activation."], verification: "source review only" });
  assert.equal(ctx.calls.filter((call) => call.prompt).length, 1);
});

test("reject missing, excessive, and oversized structured findings", async () => {
  for (const result of [null, {}, { findings: "pass" }, { findings: [42] }, { findings: Array(6).fill("x") }, { findings: ["x".repeat(2001)] }]) {
    await assert.rejects(uiReview.run(context("apps/web/src/App.vue", result)), /invalid result/);
  }
});

test("accept an empty evidence-backed review without inventing findings", async () => {
  const result = await uiReview.run(context("apps/web/src/App.svelte"));
  assert.deepEqual(result.findings, []);
});
