# Instructions for coding agents

## The repository

This repository is the guide for the mini-project of the Quality Approach course (Master 2 STAPS). It contains a documentation site (Docusaurus, in `docs/`) and a minimal *data product* example (in `examples/training-load/`). The documentation is in English, with a French translation in `i18n/fr/docusaurus-plugin-content-docs/current/` (same file names). Common technical terms are defined at their first use.

## Commands

```bash
# Install the Python environment
uv sync

# Run the example end to end
uv run python examples/training-load/run.py

# Run the tests
uv run pytest -q

# Run the site locally (one language at a time)
npm ci
npm start                  # English
npm start -- --locale fr   # French

# Check the site as the CI does
node scripts/check-navigation.mjs
npm run build
```

## Rules

- Do not make up data or sources.
- Write the tests before the code.
- Never change a test to make it pass.
- Never handle personal data.
- Propose a plan before any change touching more than one file.
- Any page change in docs/ must be mirrored in the French translation (i18n/fr/...), and vice versa.
