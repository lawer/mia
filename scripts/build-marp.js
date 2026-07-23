#!/usr/bin/env node

const { execFileSync } = require("node:child_process");
const { existsSync, readdirSync, readFileSync, writeFileSync } = require("node:fs");
const { basename, dirname, join, relative } = require("node:path");

const root = process.cwd();
const notesDirectory = join(root, "apunts");
const themePath = join(root, "themes", "lawer.css");
const defaultContentFrontMatter = "---\nlayout: default\ntitle: Continguts\n---\n";

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

function removeScopedStyles(markdown) {
  return markdown.replace(/<style scoped>[\s\S]*?<\/style>\s*/g, "");
}

function removeMarpComments(markdown) {
  return markdown.replace(/<!--\s*[\s\S]*?\s*-->/g, "");
}

function normaliseImageAltText(alt) {
  return alt
    .replace(/\b(bg|left|right|center|fit|inline|opacity)\b/g, "")
    .replace(/(?:\b(?:w:\d+|width:\d+px)|\b\d+%)/g, "")
    .replace(/[:\s]+/g, " ")
    .trim();
}

function convertMarpImages(markdown) {
  return markdown.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (match, alt, url) => {
    return `![${normaliseImageAltText(alt)}](${url})`;
  });
}

function removeSlideSeparators(markdown) {
  return markdown.replace(/^---\s*$/gm, "");
}

function convertImageOnlyHeadings(markdown) {
  return markdown.replace(/^(#{1,6})[ \t]+!\[\]\(([^)]+)\)[ \t]*$/gm, "![]($2)");
}

function normaliseWhitespace(markdown) {
  return markdown
    .replace(/[ \t]+$/gm, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function contentBodyFromMarp(marpBody) {
  return normaliseWhitespace(
    convertImageOnlyHeadings(
      removeSlideSeparators(
        convertMarpImages(
          removeMarpComments(
            removeScopedStyles(marpBody),
          ),
        ),
      ),
    ),
  );
}

function contentFrontMatter(contentPath) {
  if (!existsSync(contentPath)) {
    return defaultContentFrontMatter;
  }

  return splitFrontMatter(readFileSync(contentPath, "utf8")).frontMatter || defaultContentFrontMatter;
}

function contentFromMarp(sourcePath, markdown) {
  const { body } = splitFrontMatter(markdown);
  const sourceName = basename(sourcePath);
  const contentPath = join(dirname(sourcePath), "continguts.md");
  const contentBody = contentBodyFromMarp(body);

  return `${contentFrontMatter(contentPath)}\n> Aquesta pàgina es genera automàticament a partir de la presentació MARP \`${sourceName}\`. No l'edites directament.\n\n${contentBody}\n`;
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

function buildMarpMaterials() {
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
}

if (require.main === module) {
  buildMarpMaterials();
}

module.exports = {
  contentBodyFromMarp,
  convertImageOnlyHeadings,
  convertMarpImages,
  normaliseImageAltText,
  removeMarpComments,
  removeScopedStyles,
  removeSlideSeparators,
};
