const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
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

test("Spanish MARP sources use a separate Spanish contents page", () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), "mia-marp-es-"));
  const spanishContentsPath = path.join(directory, "continguts-es.md");
  fs.writeFileSync(spanishContentsPath, "---\nlayout: default\ntitle: Contenidos\n---\n");

  try {
    const page = contentFromMarp(path.join(directory, "lesson-es.md"), "# Tema");
    assert.match(page, /title: Contenidos/);
  } finally {
    fs.rmSync(directory, { recursive: true, force: true });
  }
});
