"""Load the CSV into SQLite, clean the sessions and compute the weekly load."""
import csv

# A duration under 10 "minutes" is not a session: it was entered in hours.
HOURS_THRESHOLD = 10

CLEANING = f"""
DROP TABLE IF EXISTS sessions;
CREATE TABLE sessions AS
SELECT DISTINCT                          -- uniqueness: an exact duplicate is excluded
    athlete_id,
    date,
    CASE WHEN duration < {HOURS_THRESHOLD} THEN duration * 60 ELSE duration END
        AS duration_min,                 -- consistency: hours converted to minutes
    rpe
FROM raw_sessions
WHERE rpe BETWEEN 0 AND 10;              -- accuracy: out-of-scale exertion excluded
"""

WEEKLY = """
DROP TABLE IF EXISTS weekly_load;
CREATE TABLE weekly_load AS
SELECT
    athlete_id,
    date(date, 'weekday 0', '-6 days') AS week,  -- Monday of the week
    COUNT(*) AS n_sessions,
    SUM(duration_min) AS minutes,
    SUM(rpe * duration_min) AS load              -- perceived exertion × minutes
FROM sessions
GROUP BY athlete_id, week
ORDER BY athlete_id, week;
"""


def load(csv_path, connection):
    """Copy the CSV as is into the raw_sessions table."""
    with open(csv_path, newline="", encoding="utf-8") as file:
        rows = [(r["athlete_id"], r["date"], float(r["duration"]), int(r["rpe"]))
                for r in csv.DictReader(file)]
    connection.executescript("""
        DROP TABLE IF EXISTS raw_sessions;
        CREATE TABLE raw_sessions (athlete_id TEXT, date TEXT, duration REAL, rpe INTEGER);
    """)
    connection.executemany("INSERT INTO raw_sessions VALUES (?, ?, ?, ?)", rows)
    connection.commit()


def transform(connection):
    """Build the (cleaned) sessions table, then the weekly_load table."""
    connection.executescript(CLEANING + WEEKLY)
