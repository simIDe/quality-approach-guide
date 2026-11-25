"""Single entry point: data, pipeline, checks, report.

From the repository root: uv run python examples/training-load/run.py
"""
import sqlite3
from contextlib import closing
from pathlib import Path

from checks import run_checks
from generate import END_DATE, first_monday, generate_sessions, write_csv
from pipeline import load, transform

FOLDER = Path(__file__).resolve().parent  # paths do not depend on the current directory


def write_report(checks, connection, path):
    lines = ["# Weekly training load", "",
             f"Sessions from {first_monday()} to {END_DATE}. Synthetic data, fictional athletes.",
             "Load = perceived exertion (0 to 10) × duration in minutes, in arbitrary units (AU).",
             "", "## Quality checks", "",
             "| Dimension | Rule | Result | Handling |", "| --- | --- | --- | --- |"]
    for c in checks:
        result = "pass" if c.ok else f"{len(c.anomalies)} anomaly(ies)"
        handling = "nothing to handle" if c.ok else c.handling
        lines.append(f"| {c.dimension} | {c.rule} | {result} | {handling} |")
    lines += ["", "## Anomalies found", ""]
    lines += [f"- {c.dimension}: {a}" for c in checks for a in c.anomalies]
    lines += ["", "## Load per athlete per week", "",
              "| Athlete | Week of | Sessions | Minutes | Load (AU) |",
              "| --- | --- | --- | --- | --- |"]
    for athlete, week, n, minutes, load_au in connection.execute("SELECT * FROM weekly_load"):
        lines.append(f"| {athlete} | {week} | {n} | {minutes:.0f} | {load_au:.0f} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run(folder=FOLDER):
    """Chain the four steps and return the path of the report."""
    csv_path = write_csv(generate_sessions(), folder / "data" / "sessions.csv")
    database = folder / "output" / "training_load.sqlite"  # open it to explore the tables
    database.parent.mkdir(parents=True, exist_ok=True)
    database.unlink(missing_ok=True)
    with closing(sqlite3.connect(database)) as connection:
        load(csv_path, connection)
        checks = run_checks(connection, END_DATE)
        transform(connection)
        return write_report(checks, connection, folder / "output" / "report.md")


if __name__ == "__main__":
    report = run()
    print(f"Report written: {report}")
