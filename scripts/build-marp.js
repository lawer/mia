#!/usr/bin/env node

const { execFileSync } = require("node:child_process");
const { existsSync, readdirSync, readFileSync, writeFileSync } = require("node:fs");
const { basename, dirname, join, relative } = require("node:path");

const root = process.cwd();
const notesDirectory = join(root, "apunts");
const themePath = join(root, "themes", "lawer.css");

function markdownFiles(directory) {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);

    if (entry.isDirectory()) {
      return markdownFiles(path);
    }

    return entry.isFile() && entry.name.endsWith(".md") ? [path] : [];
  });
}

function splitFrontMatter(markdown) {
  const match = markdown.match(/^(---\r?\n[\s\S]*?\r?\n---\r?\n?)([\s\S]*)$/);
  return match ? { frontMatter: match[1], body: match[2] } : { frontMatter: "", body: markdown };
}

function isMarp(markdown) {
  return /^---\r?\n[\s\S]*?^marp:\s*true\s*$/m.test(markdown);
}

function contentFrontMatter(contentPath) {
  if (!existsSync(contentPath)) {
    return "---\nlayout: default\ntitle: Continguts\n---\n";
  }

  return splitFrontMatter(readFileSync(contentPath, "utf8")).frontMatter || "---\nlayout: default\ntitle: Continguts\n---\n";
}

function contentFromMarp(sourcePath, markdown) {
  const { body } = splitFrontMatter(markdown);
  const sourceName = basename(sourcePath);
  const contentPath = join(dirname(sourcePath), "continguts.md");
  const cleanBody = body
    .replace(/<style scoped>[\s\S]*?<\/style>\s*/g, "")
    .replace(/<!--\s*[\s\S]*?\s*-->/g, "")
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (match, alt, url) => {
      if (/\bbg\b/.test(alt)) {
        return "";
      }

      const contentAlt = alt
        .replace(/\b(left|right|center|fit|inline|opacity)\b/g, "")
        .replace(/\b(?:w:\d+|\d+%)\b/g, "")
        .trim();
      return `![${contentAlt}](${url})`;
    })
    .replace(/^---\s*$/gm, "")
    .replace(/^(#{1,6})\s+!\[\]\(([^)]+)\)\s*$/gm, "![]($2)")
    .replace(/[ \t]+$/gm, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();

  return `${contentFrontMatter(contentPath)}\n> Aquesta pàgina es genera automàticament a partir de la presentació MARP \`${sourceName}\`. No l'edites directament.\n\n${cleanBody}\n`;
}

function validateAssets(sourcePath, markdown) {
  const missingAssets = [...markdown.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)]
    .map((match) => match[1].trim())
    .filter((asset) => !/^(https?:|data:|#)/.test(asset))
    .map((asset) => ({ asset, path: join(dirname(sourcePath), decodeURIComponent(asset.split(/[?#]/)[0])) }))
    .filter(({ path }) => !existsSync(path));

  if (missingAssets.length > 0) {
    const details = missingAssets.map(({ asset }) => `  - ${asset}`).join("\n");
    throw new Error(`Missing MARP assets in ${relative(root, sourcePath)}:\n${details}`);
  }
}

function render(sourcePath, extension) {
  const outputPath = sourcePath.replace(/\.md$/, `.${extension}`);
  execFileSync(
    join(root, "node_modules", ".bin", "marp"),
    [sourcePath, `--${extension}`, "--theme-set", themePath, "--allow-local-files", "--output", outputPath],
    { cwd: root, stdio: "inherit" },
  );

  return outputPath;
}

function validateTheme(htmlPath) {
  if (!readFileSync(htmlPath, "utf8").includes("Marp / Marpit Lawer theme.")) {
    throw new Error(`The Lawer theme was not applied to ${relative(root, htmlPath)}`);
  }
}

const sources = markdownFiles(notesDirectory).filter((path) => isMarp(readFileSync(path, "utf8")));

for (const sourcePath of sources) {
  const markdown = readFileSync(sourcePath, "utf8");
  const contentPath = join(dirname(sourcePath), "continguts.md");

  validateAssets(sourcePath, markdown);
  writeFileSync(contentPath, contentFromMarp(sourcePath, markdown));
  validateTheme(render(sourcePath, "html"));
  render(sourcePath, "pdf");
  console.log(`Generated ${relative(root, contentPath)}`);
}
