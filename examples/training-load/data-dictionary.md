# Data dictionary

The three tables of the SQLite database `output/training_load.sqlite`, recreated on every run of `run.py`.

## raw_sessions

Copy of the file `data/sessions.csv`, without any change. The quality checks run on this table.

| Column | Type | Unit | Definition | Possible values | Source |
| --- | --- | --- | --- | --- | --- |
| athlete_id | TEXT | — | Fictional identifier of the athlete | A01 to A06 | `data/sessions.csv` |
| date | TEXT | day (YYYY-MM-DD) | Date of the session | from 2026-09-28 to 2026-11-22 | `data/sessions.csv` |
| duration | REAL | minutes, sometimes hours by mistake | Duration of the session as entered | 30 to 100 expected; under 10, the value is in hours | `data/sessions.csv` |
| rpe | INTEGER | scale point | Perceived exertion reported by the athlete (RPE, *rating of perceived exertion*) | 0 to 10 expected; any other value is an error | `data/sessions.csv` |

## sessions

Cleaned sessions: exact duplicates excluded, durations in hours converted, out-of-scale exertions excluded.

| Column | Type | Unit | Definition | Possible values | Source |
| --- | --- | --- | --- | --- | --- |
| athlete_id | TEXT | — | Fictional identifier of the athlete | A01 to A06 | `raw_sessions.athlete_id` |
| date | TEXT | day (YYYY-MM-DD) | Date of the session | from 2026-09-28 to 2026-11-22 | `raw_sessions.date` |
| duration_min | REAL | minutes | Duration of the session, converted to minutes if it was entered in hours | 10 and above | `raw_sessions.duration` |
| rpe | INTEGER | scale point | Perceived exertion | 0 to 10 | `raw_sessions.rpe` |

## weekly_load

The delivered product: one row per athlete and per week with at least one recorded session.

| Column | Type | Unit | Definition | Possible values | Source |
| --- | --- | --- | --- | --- | --- |
| athlete_id | TEXT | — | Fictional identifier of the athlete | A01 to A06 | `sessions.athlete_id` |
| week | TEXT | day (YYYY-MM-DD) | Monday of the week | eight Mondays, from 2026-09-28 to 2026-11-16 | computed from `sessions.date` |
| n_sessions | INTEGER | sessions | Number of sessions kept in the week | 1 to 7 (3 in the generated data, fewer if a session was excluded) | `COUNT(*)` over `sessions` |
| minutes | REAL | minutes | Total duration run in the week | 0 and above | sum of `sessions.duration_min` |
| load | REAL | arbitrary unit (AU) | Sum over the week of perceived exertion × duration in minutes | 0 and above | sum of `sessions.rpe × sessions.duration_min` |
