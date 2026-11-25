# Quality Approach: mini-project guide

Reference guide for the mini-project of the Quality Approach course (Master 2 STAPS, UFR STAPS Montpellier): the brief, a quality checklist, practical guides, document templates and a working example.

**The site: <https://simide.github.io/quality-approach-guide/>**

The site is in English, with a French translation available from the language menu.

This repository is meant to be consulted, not copied. Your project can be organised in a completely different way.

## Running the site locally

You need [Node.js](https://nodejs.org/) 20 or later.

```bash
npm ci
npm start                  # English
npm start -- --locale fr   # French
```

The site opens at <http://localhost:3000/quality-approach-guide/>. The development server serves one language at a time; `npm run build` builds both. To check the site as the CI does: `node scripts/check-navigation.mjs` then `npm run build`.

English pages live in `docs/`, their French translations in `i18n/fr/docusaurus-plugin-content-docs/current/`, with the same file names.

## Running the example locally

You need Python 3.11 or later and [uv](https://docs.astral.sh/uv/). From the root of the repository:

```bash
uv run python examples/training-load/run.py   # data, pipeline, checks, report
uv run pytest -q                              # tests
```

The report is written to `examples/training-load/output/report.md`. See the [example's README](examples/training-load/README.md).

## Licence

Code under the MIT licence, texts under the CC BY 4.0 licence. See [LICENSE](LICENSE).
