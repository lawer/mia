const test = require("node:test");
const assert = require("node:assert/strict");
const {
  contentBodyFromMarp,
  contentFromMarp,
  normaliseImageAltText,
} = require("./build-marp.js");

test("removes MARP-only layout directives while preserving content", () => {
  const marpBody = `<!--
_class: lead
-->

<style scoped>
h1 { color: red; }
</style>

# Títol

![bg right:35% fit](../../images/example.png)

---

## Explicació

Text de prova.`;

  assert.equal(
    contentBodyFromMarp(marpBody),
    "# Títol\n\n![](../../images/example.png)\n\n## Explicació\n\nText de prova.",
  );
});

test("normalises MARP image modifiers and image-only headings", () => {
  const marpBody = "## ![inline w:400](diagram.png)\n\n![left 70%](chart.png)";

  assert.equal(contentBodyFromMarp(marpBody), "![](diagram.png)\n\n![](chart.png)");
  assert.equal(normaliseImageAltText("bg right:35% fit"), "");
});

test("generated student content does not expose authoring instructions", () => {
  const page = contentFromMarp("/tmp/topic/lesson.md", "# Contingut per a l'alumnat");

  assert.match(page, /# Contingut per a l'alumnat/);
  assert.doesNotMatch(page, /generada automàticament|no l'edites/i);
});
