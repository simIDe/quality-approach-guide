---
title: How this site is built
---

# How this site is built

This site applies to itself what the guide suggests for your project: every change goes through a *pull request* (a request to merge, reviewed before it enters the main branch), an automated check, then publication with no manual step.

## The pipeline in four steps

1. **I write in Markdown.** Each page is a file in the [`docs/`](https://github.com/simIDe/quality-approach-guide/tree/main/docs) folder. The site is built by [Docusaurus](https://docusaurus.io/), an open-source static site generator; its configuration lives in [`docusaurus.config.mjs`](https://github.com/simIDe/quality-approach-guide/blob/main/docusaurus.config.mjs) and the navigation in [`sidebars.mjs`](https://github.com/simIDe/quality-approach-guide/blob/main/sidebars.mjs). Locally, `npm start` shows the site while you write.
2. **I open a pull request.** The change is made on a branch, then proposed. A real example: [pull request #3](https://github.com/simIDe/quality-approach-guide/pull/3), which added the practical guides, one guide per commit. See [guide 01](./guides/01-collaborate-on-github.md).
3. **The check runs.** The [`docs.yml`](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/docs.yml) workflow checks that every page appears in the navigation, then builds the site: a broken internal link or anchor makes the build fail. A second workflow, [`example.yml`](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/example.yml), reruns the example and its tests on Linux, Windows and macOS. As long as a check is red, nothing is merged. See [guide 04](./guides/04-automate-a-check.md).
4. **Merging publishes.** Once the pull request is merged into `main`, the same workflow publishes the site on GitHub Pages through the official GitHub Actions mechanism. Nobody copies files by hand. See [guide 05](./guides/05-publish-a-release.md).

## Two languages

The site is bilingual: English by default, French through the language menu at the top right. The English pages live in `docs/`; their French translations live in [`i18n/fr/docusaurus-plugin-content-docs/current/`](https://github.com/simIDe/quality-approach-guide/tree/main/i18n/fr/docusaurus-plugin-content-docs/current), with the same file names. The navigation check, [`scripts/check-navigation.mjs`](https://github.com/simIDe/quality-approach-guide/blob/main/scripts/check-navigation.mjs), also verifies that both languages have the same pages.

## Why these choices

- **Docusaurus** is maintained, open source (MIT licence) and reads ordinary Markdown files: the content stays readable on GitHub and reusable with another tool.
- **Search** is built with the site ([`docusaurus-search-local`](https://github.com/easyops-cn/docusaurus-search-local)): no third-party service, no account.
- **Versions are pinned** in `package-lock.json` (site) and `uv.lock` (example): the site built today will be the same in six weeks.

Your project needs none of these tools. The idea to remember is the pipeline: write, propose, check automatically, publish.
