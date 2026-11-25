---
title: "06 · Work with an agent"
sidebar_position: 6
---

*How do I use a coding agent without losing control?*

## The problem

You ask a coding agent (an AI assistant that reads, writes and runs code in your project) to "clean the session data". It changes six files, the tests pass, but nobody in the group can explain what it deleted, and on 20 January everyone will need to be able to.

## The bare minimum

**1. Write the request before the code.** A few lines: the goal, the files involved, what must not change, how you will know it worked. If you can't write it, the agent won't guess it.

```text
Goal: convert to minutes the durations entered in hours in sessions.csv.
Rule: a duration below 5 is treated as hours.
Do not touch: the load calculation, the other columns.
Done when: the new test passes and the old ones do too.
Propose a plan before changing anything.
```

**2. Have the tests written first.** Ask for the test, read it, check that it fails, and only then ask for the code that makes it pass. Refuse any change to an existing test made just to make it pass.

**3. Review the diff.** The *diff* is the list of lines added and removed. Read it in full before each commit (record of changes), with `git diff` or in the pull request, and ask the agent to explain every line you don't understand.

**4. Never send it** secrets (password, API key, `.env` file) or personal data: athletes' names, health data, raw files from smartwatches. Work on a synthetic or pseudonymised sample (see [guide 07](./07-personal-data.md)).

**5. Keep the log.** In the method log, for each notable use: what was asked, what was kept, what was rejected or corrected, and why. It is expected evidence, not a formality.

## Going further

- Write an `AGENTS.md` file at the root of the project: commands to install and test, the group's rules. Many agents read this file when they start; this repository has one ([AGENTS.md](https://github.com/simIDe/quality-approach-guide/blob/main/AGENTS.md)).
- Have the agent work on a separate branch, merged through a pull request after human review (see [guide 01](./01-collaborate-on-github.md)).
- Use a local model when the data must not leave the machine, often at the cost of lower quality.

## How to know it's done

- Every member can explain any file in the project, including those written by the agent.
- The method log contains at least one example of an agent proposal that was rejected or corrected.
- No secret or personal data appears in the conversations with the agent or in the git history.
