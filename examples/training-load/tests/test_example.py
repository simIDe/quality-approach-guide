"""Tests of the example: generation, transformation, checks and report."""
import sqlite3

import pytest

from checks import run_checks
from generate import END_DATE, clean_sessions, generate_sessions, write_csv
from pipeline import load, transform
from run import run


@pytest.fixture
def connection():
    cx = sqlite3.connect(":memory:")
    yield cx
    cx.close()


def load_rows(rows, connection, tmp_path):
    load(write_csv(rows, tmp_path / "sessions.csv"), connection)


def test_generation_is_reproducible():
    assert generate_sessions() == generate_sessions()


def test_the_four_defects_are_detected(connection, tmp_path):
    load_rows(generate_sessions(), connection, tmp_path)
    results = {c.dimension: c for c in run_checks(connection, END_DATE)}
    failures = {dimension for dimension, c in results.items() if not c.ok}
    assert failures == {"accuracy", "consistency", "completeness", "uniqueness"}
    assert len(results["consistency"].anomalies) == 3  # durations in hours
    assert len(results["accuracy"].anomalies) == 1  # perceived exertion out of scale
    assert len(results["uniqueness"].anomalies) == 1  # duplicated session
    assert "A03" in results["completeness"].anomalies[0]  # missing week
    assert results["timeliness"].ok


def test_clean_data_has_no_anomaly(connection, tmp_path):
    load_rows(clean_sessions(), connection, tmp_path)
    assert all(c.ok for c in run_checks(connection, END_DATE))


def test_transform_corrects_excludes_and_computes_the_load(connection, tmp_path):
    rows = [
        {"athlete_id": "A01", "date": "2026-11-16", "duration": 60, "rpe": 5},
        {"athlete_id": "A01", "date": "2026-11-16", "duration": 60, "rpe": 5},  # duplicate
        {"athlete_id": "A01", "date": "2026-11-18", "duration": 0.5, "rpe": 4},  # in hours
        {"athlete_id": "A01", "date": "2026-11-20", "duration": 40, "rpe": 12},  # out of scale
        {"athlete_id": "A01", "date": "2026-11-22", "duration": 30, "rpe": 2},  # Sunday
    ]
    load_rows(rows, connection, tmp_path)
    transform(connection)
    weeks = connection.execute("SELECT * FROM weekly_load").fetchall()
    # 5×60 + 4×30 + 2×30 = 480; the Sunday belongs to the week of Monday the 16th.
    assert weeks == [("A01", "2026-11-16", 3, 120.0, 480.0)]


def test_the_report_says_how_each_defect_is_handled(tmp_path):
    text = run(tmp_path).read_text(encoding="utf-8")
    assert all(word in text for word in ["corrected", "excluded", "flagged"])
    assert "| A01 | 2026-09-28 |" in text
