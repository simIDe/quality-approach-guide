---
title: "02 · Check your data"
sidebar_position: 2
---

*How do I know if my data is good?*

## The problem

Your training load table says an athlete ran for 90 hours this week: one session was entered in hours instead of minutes. The coach will stop trusting you if he is the one who spots it.

## The bare minimum

"Good" means good *for the promised use*. For each of the five quality dimensions, pick at least one check that makes sense for your user.

| Dimension | The question | Example check |
| --- | --- | --- |
| Accuracy | Are the values plausible? | Perceived effort between 0 and 10, duration between 5 and 300 minutes |
| Completeness | Are rows or values missing? | Each athlete has at least one session every week |
| Timeliness | Is the data recent enough? | The most recent session is less than 7 days old |
| Consistency | Does the data contradict itself? | No session dated in the future |
| Uniqueness | Is the same thing counted twice? | No two identical sessions (athlete, date, duration) |

In SQL (here SQLite), each check is a query that returns the faulty rows; zero rows means the check passed.

```sql
-- Accuracy: effort off the scale or implausible duration
SELECT * FROM sessions WHERE effort NOT BETWEEN 0 AND 10 OR duration_min NOT BETWEEN 5 AND 300;
-- Uniqueness: duplicate sessions
SELECT athlete, date, duration_min, COUNT(*) AS n
FROM sessions GROUP BY athlete, date, duration_min HAVING COUNT(*) > 1;
-- Timeliness: one row if the most recent session is more than 7 days old
SELECT MAX(date) AS latest FROM sessions HAVING MAX(date) < date('now', '-7 days');
```

The same checks in Python, with the standard library's `sqlite3` module:

```python
import sqlite3

con = sqlite3.connect("data/sessions.db")
off_scale = con.execute("SELECT * FROM sessions WHERE effort NOT BETWEEN 0 AND 10").fetchall()
assert not off_scale, f"{len(off_scale)} session(s) with effort off the scale"
```

**What to do with a defect you find.** Three possible answers, to choose case by case:

- **correct** when the right value is certain (a duration of 1.5, obviously in hours, becomes 90 minutes);
- **exclude** when it is not (an effort of 14 out of 10);
- **flag** when you keep the row but the user needs to know (a missing week).

In all three cases, write it down: how many rows, which rule, why. The delivered report and the method log are the right places. The repository's example does exactly that: [examples/training-load](https://github.com/simIDe/quality-approach-guide/tree/main/examples/training-load).

## Going further

- Turn each check into a pytest test, so it runs on its own (see [guide 04](./04-automate-a-check.md)).
- Describe each column (type, unit, possible values) in a data dictionary: the accuracy checks follow from it.
- Use DuckDB to check a large CSV or Parquet file directly, without loading it into a database ([DuckDB documentation](https://duckdb.org/docs/)).

## How to know it's done

- Each dimension has at least one written check that can be rerun.
- Each defect found has a decision (corrected, excluded, flagged) written down somewhere.
- The delivered product states its known limits.
