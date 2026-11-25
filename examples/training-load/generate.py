"""Generate a synthetic CSV of running sessions, with four deliberate defects.

Fictional athletes (A01 to A06). Fixed seed and end date: the same file on every run.
"""
import csv
import random
from datetime import date, timedelta

SEED = 2026
END_DATE = date(2026, 11, 22)  # a Sunday: last day covered by the data
N_WEEKS = 8
ATHLETES = [f"A{i:02d}" for i in range(1, 7)]
SESSIONS_PER_WEEK = 3
COLUMNS = ["athlete_id", "date", "duration", "rpe"]


def first_monday(end_date=END_DATE):
    return end_date - timedelta(weeks=N_WEEKS, days=-1)


def clean_sessions():
    """Sessions without defects: 3 per week per athlete, duration in minutes."""
    rng = random.Random(SEED)
    rows = []
    for athlete in ATHLETES:
        for week in range(N_WEEKS):
            monday = first_monday() + timedelta(weeks=week)
            for day in sorted(rng.sample(range(7), SESSIONS_PER_WEEK)):
                day_iso = (monday + timedelta(days=day)).isoformat()
                # duration in minutes, rating of perceived exertion (RPE) on the 0 to 10 scale
                rows.append({"athlete_id": athlete, "date": day_iso,
                             "duration": rng.randint(30, 100), "rpe": rng.randint(3, 8)})
    return rows


def add_defects(rows):
    """Introduce the four deliberate defects, each on a different row."""
    rng = random.Random(SEED + 1)
    # 1. Missing week: no session for A03 during the 5th week.
    monday = first_monday() + timedelta(weeks=4)
    week = {(monday + timedelta(days=d)).isoformat() for d in range(7)}
    rows = [r for r in rows if not (r["athlete_id"] == "A03" and r["date"] in week)]
    hours1, hours2, hours3, out_of_scale, double = rng.sample(range(len(rows)), 5)
    # 2. Three durations entered in hours instead of minutes.
    for i in (hours1, hours2, hours3):
        rows[i]["duration"] = round(rows[i]["duration"] / 60, 2)
    # 3. A perceived exertion outside the 0 to 10 scale.
    rows[out_of_scale]["rpe"] = 14
    # 4. A session entered twice.
    rows.append(dict(rows[double]))
    return sorted(rows, key=lambda r: (r["date"], r["athlete_id"]))


def generate_sessions():
    return add_defects(clean_sessions())


def write_csv(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return path
