---
title: Checklist
sidebar_position: 1
---

# Quality checklist

Two lists of questions, to go through again before each delivery. A "no" is not a mistake: it is a limit to fix or to state.

## The data

- [ ] **Accuracy:** have the values been compared against plausible bounds (scales, units, dates)?
- [ ] **Completeness:** do we know how many values or rows are missing, and what we do about them?
- [ ] **Timeliness:** is the date of the data known, and is it recent enough for the user's decision?
- [ ] **Consistency:** does the same piece of information have the same name, format and unit everywhere?
- [ ] **Uniqueness:** have we checked that no row appears twice?
- [ ] **Origin:** is each source written down, with its address, its licence and the date it was retrieved?
- [ ] **Defects:** is each defect found corrected, excluded or flagged, and is that choice written down?
- [ ] **Limits:** are the known limits written where the user will read them?

## The project

The first six questions follow the characteristics of a *data product* (data designed for a user, with a promise) described by Zhamak Dehghani in 2019: [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html).

- [ ] **Discoverable:** does the user know where to find the product?
- [ ] **Addressable:** does the product have a stable address (path, URL, table name)?
- [ ] **Trustworthy:** are the promise and the checks that verify it visible?
- [ ] **Self-describing:** is each column or field explained, for example in a data dictionary?
- [ ] **Interoperable:** is the output in an open, common format?
- [ ] **Secure:** are secrets and personal data kept out of the repository and out of exchanges with a model?
- [ ] **Rerunnable by someone else:** can someone outside the group rerun the project using only the README?
- [ ] **Readable history:** do the commits and pull requests tell what was done and why?
- [ ] **Automated checks:** do the checks and tests run without intervention on every change?
