---
title: The example
---

# The example: weekly training load

The [`examples/training-load/`](https://github.com/simIDe/quality-approach-guide/tree/main/examples/training-load) folder contains a minimal *data product* (data prepared for a specific user and decision) that runs end to end with a single command. It can be read in twenty minutes: under 300 lines of Python, tests included.

It shows one way of doing things, not the only one. Your project can use other tools and a different organisation.

## What the example does

The user is the coach of a running club. He receives a report with one row per athlete and per week over eight weeks, and the load for each week: perceived effort (0 to 10) × duration in minutes.

1. [`generate.py`](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/generate.py) creates a CSV of synthetic sessions, with a fixed seed and a fixed end date: the file is the same on every run. The athletes (A01 to A06) are fictitious.
2. [`pipeline.py`](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/pipeline.py) loads the CSV into SQLite, cleans the sessions and computes the weekly table in SQL.
3. [`checks.py`](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/checks.py) checks the raw sessions against the five dimensions: accuracy, completeness, timeliness, consistency, uniqueness.
4. [`run.py`](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/run.py) chains the steps and writes the Markdown report.

## The four defects and how they are handled

The generator deliberately introduces four defects. Each one is detected by a check, then handled in one of the three possible ways: corrected, excluded or flagged.

| Defect | Check that detects it | Handling |
| --- | --- | --- |
| Three durations entered in hours instead of minutes | **consistency**: all durations must be in minutes, so at least 10 | corrected: duration × 60 |
| One week without sessions for athlete A03 | **completeness**: eight weeks expected per athlete | flagged: the week is missing from the table, no load is made up |
| One session entered twice | **uniqueness**: one session per athlete per day | excluded: only one copy is kept |
| A perceived effort of 14 | **accuracy**: effort must be between 0 and 10 | excluded: the real value is unknown |

The **timeliness** check verifies that the last session is less than seven days before the end date. It passes: a check that finds nothing is information too.

The report repeats this table, lists each anomaly found, then gives the weekly table. A test, in [`tests/test_example.py`](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/tests/test_example.py), fails if any of the four defects is no longer detected.

## Running it yourself

With Python 3.11 or later and [uv](https://docs.astral.sh/uv/), from the root of the cloned repository:

```bash
uv run python examples/training-load/run.py
uv run pytest -q
```

The report is written to `examples/training-load/output/report.md`. The [example's README](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/README.md) also gives the equivalent with pip and venv.

On every pull request (a proposed change reviewed before being merged), the [`example.yml`](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/example.yml) workflow reruns the command and the tests on Linux, Windows and macOS.

## The documents that come with it

- [Product sheet](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/product-sheet.md): for whom, for which decision, what is guaranteed and what is not.
- [Data dictionary](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/data-dictionary.md): every column of every table.
- [Method log](https://github.com/simIDe/quality-approach-guide/blob/main/examples/training-load/method-log.md) (excerpt): the decisions, the use of AI, what we would do differently.
