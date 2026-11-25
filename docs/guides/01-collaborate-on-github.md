---
title: "01 · Collaborate on GitHub"
sidebar_position: 1
---

*How can three people work on the same code without stepping on each other's toes?*

## The problem

Léa fixes the training load calculation while Hugo renames the columns in the same file, and each pushes straight to the main branch. By evening the script no longer runs and nobody knows which change broke it.

## The bare minimum

Four habits are enough to start.

1. **Split the work with issues.** An *issue* is a GitHub ticket: a task, a defect or a question, with a title, a description and an assignee. One issue per task of a few hours, no more.
2. **Work on a short-lived branch.** A *branch* is a line of work parallel to the main branch (`main`). It only lives for the length of one task: one or two days.
3. **Propose the change through a pull request.** A *pull request* (PR) asks to merge a branch into `main`; GitHub shows the *diff* there, that is, the lines added and removed.
4. **Have another member review it.** Someone other than the author reads the diff, asks questions, then approves and merges.

```bash
git switch main
git pull                               # start from the latest version
git switch -c 12-load-calculation      # one branch per issue (here issue #12)
# ... edit, test ...
git add src/load.py
git commit -m "Compute load in minutes instead of hours"
git push -u origin 12-load-calculation
gh pr create --fill                    # or the "Compare & pull request" button on GitHub
```

A *commit* is a dated record of a set of changes, with a message. A good message says what the change does, in one sentence. Writing `Closes #12` in the PR description closes the issue automatically when it is merged.

## Going further

- Protect `main` in the repository settings to prevent merging without review ([GitHub documentation on pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests)).
- Track issues on a GitHub Projects board (to do, in progress, done) rather than in a list.
- Work in pairs on the same screen (*pair programming*) for the tricky parts; the review then happens live.

## How to know it's done

- The history of `main` contains only pull request merges, and each PR was reviewed by someone other than its author.
- Every member of the group has opened at least one PR and reviewed at least one.
- Reading the list of closed issues, an outsider understands who did what.
