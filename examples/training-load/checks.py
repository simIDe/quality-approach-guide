"""Quality checks on the raw sessions: one per dimension, each says how it is handled."""
from dataclasses import dataclass
from datetime import timedelta

from generate import N_WEEKS, first_monday
from pipeline import HOURS_THRESHOLD


@dataclass
class Check:
    dimension: str
    rule: str
    handling: str
    anomalies: list

    @property
    def ok(self):
        return not self.anomalies


def list_rows(connection, query, *parameters):
    return [" ".join(str(v) for v in row) for row in connection.execute(query, parameters)]


def accuracy(connection, end_date):
    anomalies = list_rows(connection, "SELECT athlete_id, date, 'rpe', rpe FROM raw_sessions "
                                      "WHERE rpe NOT BETWEEN 0 AND 10")
    return Check("accuracy", "perceived exertion between 0 and 10",
                 "excluded: the true value cannot be guessed", anomalies)


def consistency(connection, end_date):
    anomalies = list_rows(connection, "SELECT athlete_id, date, 'duration', duration "
                                      "FROM raw_sessions WHERE duration < ?", HOURS_THRESHOLD)
    return Check("consistency", f"all durations in minutes (≥ {HOURS_THRESHOLD})",
                 "corrected: duration × 60", anomalies)


def completeness(connection, end_date):
    expected = {(first_monday(end_date) + timedelta(weeks=w)).isoformat()
                for w in range(N_WEEKS)}
    present = connection.execute("SELECT DISTINCT athlete_id, date(date, 'weekday 0', '-6 days') "
                                 "FROM raw_sessions").fetchall()
    anomalies = [f"{athlete} no session in the week of {week}"
                 for athlete in sorted({a for a, _ in present})
                 for week in sorted(expected - {w for a, w in present if a == athlete})]
    return Check("completeness", f"{N_WEEKS} weeks per athlete",
                 "flagged: week missing from the table, nothing is made up", anomalies)


def timeliness(connection, end_date):
    latest = connection.execute("SELECT MAX(date) FROM raw_sessions").fetchone()[0]
    limit = (end_date - timedelta(days=7)).isoformat()
    anomalies = [] if latest and latest > limit else [f"latest session on {latest}"]
    return Check("timeliness", f"a session in the 7 days before {end_date}",
                 "flagged: do not use the report as is", anomalies)


def uniqueness(connection, end_date):
    anomalies = list_rows(connection, "SELECT athlete_id, date, COUNT(*) || ' times' "
                                      "FROM raw_sessions GROUP BY athlete_id, date "
                                      "HAVING COUNT(*) > 1")
    return Check("uniqueness", "one session per athlete per day",
                 "excluded: a single copy kept", anomalies)


def run_checks(connection, end_date):
    """Run the five checks on the raw_sessions table."""
    return [check(connection, end_date)
            for check in (accuracy, completeness, timeliness, consistency, uniqueness)]
