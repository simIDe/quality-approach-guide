---
title: "03 · Make it rerunnable"
sidebar_position: 3
---

*Can someone else rerun my project?*

## The problem

On 20 January, another group will have ten minutes to rerun your project using only your README. If the script looks for `C:\Users\lea\Desktop\sessions.csv`, needs a library installed "by hand" or gives different numbers on every run, it's lost.

## The bare minimum

Five points, from most to least important.

**1. Pinned dependencies.** One simple way is [uv](https://docs.astral.sh/uv/), a Python project manager: it records the dependencies in `pyproject.toml` and their exact versions in `uv.lock`. Both files are versioned with the code.

```bash
uv init                 # creates pyproject.toml (once, at the start of the project)
uv add pandas pytest    # adds dependencies and updates uv.lock
uv sync                 # on another machine: installs exactly the same versions
```

**2. A single command to run everything.** An entry script that chains the steps (data, transformation, output):

```bash
uv run python pipeline.py
```

`uv run` runs the command in the project's environment, without having to activate it.

**3. Paths relative to the project**, never to your machine:

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SESSIONS = ROOT / "data" / "sessions.csv"   # works on Windows, macOS and Linux
```

**4. A fixed random seed** as soon as there is randomness (simulated data, sampling, model):

```python
import random

random.seed(42)   # numpy: rng = numpy.random.default_rng(42)
```

**5. An installation README** that fits in a few lines: prerequisites (Python version, uv), commands to type in order, what you should get at the end.

## Going further

- Without uv, the equivalent with pip and venv: `python -m venv .venv`, activate the environment, then `pip install -r requirements.txt`, with versions pinned in the file (`pandas==2.2.3`, produced by `pip freeze > requirements.txt`).
- A `Makefile` or a `run.sh` / `run.ps1` script when there are several commands to chain.
- A Docker container also pins the system, at the cost of one more tool to install and explain.

## How to know it's done

- A group member clones the repository into a fresh folder and reruns everything using only the README, without asking the others anything.
- Two successive runs give exactly the same results.
- No absolute path in the code: a search for `C:\` or `/home/` finds nothing.
