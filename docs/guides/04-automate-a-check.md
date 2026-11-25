---
title: "04 · Automate a check"
sidebar_position: 4
---

*How do I get my checks to run on their own?*

## The problem

Your tests and data checks exist, but everyone forgets to run them before pushing their work. Hugo merges a change that breaks the load calculation, and the error is only discovered the day before delivery.

## The bare minimum

GitHub Actions runs commands on a GitHub machine on every change to the repository, free of charge for a public repository. A *workflow* is a YAML file placed in `.github/workflows/` that says when and what to run.

This workflow runs pytest on every *push* (sending commits to GitHub) and on every pull request (request to merge a branch):

```yaml
# .github/workflows/tests.yml
name: Tests

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7        # fetches the repository's code
      - uses: astral-sh/setup-uv@v10.4.0 # installs uv (exact version)
      - run: uv sync                     # installs the pinned dependencies (uv.lock)
      - run: uv run pytest -q            # runs the tests; a failure fails the workflow
```

It assumes a project managed with uv and pytest tests (see [guide 03](./03-make-it-rerunnable.md)). Your data checks can run the same way, written as tests or launched by one more `run:` line (`uv run python checks.py`), as long as the script exits with an error when a check fails.

**Reading a failure.** A red cross appears next to the commit and in the pull request.

1. Click the cross, then *Details*: the list of steps is shown, and the one that failed is marked.
2. Open that step and scroll down to the first lines in error: pytest gives the name of the test and the value obtained against the value expected.
3. Reproduce locally with the same command (`uv run pytest -q`), fix, push: the workflow starts again on its own.

**Two real examples in this repository:**

- [example.yml](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/example.yml) installs the example's environment, generates the data, runs the pipeline and then the tests;
- [docs.yml](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/docs.yml) builds this site on every pull request and publishes it on every merge.

## Going further

- Add a linter such as Ruff in one more step, to check the code style.
- Run the data checks every night with a `schedule` trigger, useful if the source changes on its own ([GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart)).
- Require the workflow to be green before any merge, in the main branch's protection settings.

## How to know it's done

- The repository's *Actions* tab shows a run for every push and every pull request.
- A deliberately broken test on a branch makes a red cross appear in the pull request.
- Every group member knows how to find the failed test in the run log.
