---
title: "05 · Publish a release"
sidebar_position: 5
---

*How do I say "this is the delivered version"?*

## The problem

On 18 January you deliver the project, but the group keeps fixing details in the days that follow. On 20 January, the coach, the teacher and the group rerunning your project are no longer looking at the same thing.

## The bare minimum

Mark the delivered version with a tag, then turn it into a release.

- A *tag* is a label placed on a specific commit (a *commit* is a dated record of changes). It no longer moves, even if the branch moves on.
- A GitHub *release* is a page attached to a tag: a title, release notes and a downloadable archive of the code ([GitHub documentation on releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)).

```bash
git switch main
git pull                                         # the merged, reviewed version
git tag -a v1.0.0 -m "Version delivered on 18 January 2027"
git push origin v1.0.0
gh release create v1.0.0 --title "v1.0.0" --notes-file NOTES.md
```

The release can also be created from the web interface: *Releases*, then *Draft a new release*.

The release notes fit in three lines: what the product does, what changed since the previous version, the known limits.

```markdown
Weekly training load table, 12 athletes, last 8 weeks.
New: sessions entered in hours are converted to minutes.
Known limit: one missing week for one athlete, flagged in the report.
```

A common convention for the number: `v1.0.0` for the first delivered version, `v1.0.1` for a fix, `v1.1.0` for an addition. Nothing forces you to follow it; what matters is that a number always refers to the same state of the code.

## Going further

- Publish documentation or a report on GitHub Pages, as this repository does: its site is built with Docusaurus by GitHub Actions and published on every merge ([custom workflows for GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)).
- Attach the produced file (report, cleaned CSV) to the release with `gh release upload v1.0.0 report.md`, so the user has nothing to rerun.
- Keep a `CHANGELOG.md` file that accumulates the notes of each version.

## How to know it's done

- The repository's *Releases* page shows a dated version with its notes.
- `git switch --detach v1.0.0` on another machine, followed by the README commands, gives back exactly the delivered product.
- The product sheet and the method log cite the delivered version number.
