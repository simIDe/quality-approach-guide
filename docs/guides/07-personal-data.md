---
title: "07 · Personal data"
sidebar_position: 7
---

*Am I allowed to use this data?*

This guide is not legal advice: it helps you ask the right questions and points to the CNIL (Commission nationale de l'informatique et des libertés), the French data protection authority. Its pages linked below are in French.

## The problem

Your club offers you the smartwatch exports of its runners: heart rate, GPS positions, injuries recorded by the physiotherapist. The project would be more realistic, but this data describes real people, and their health.

## The bare minimum

**Recognising personal data.** It is any information relating to an identified or identifiable person, directly (name, photo) or indirectly (licence number, a GPS track that leaves the same home every morning, the combination of age + club + sport) ([CNIL definition](https://www.cnil.fr/fr/definition/donnee-personnelle)).

**Recognising health data.** Heart rate, injuries, weight, sleep or menstrual cycle can be health data, depending on how they are used. They are sensitive data, protected more strictly ([what is health data, CNIL](https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante)).

**Six questions to ask before using them**, with the answers written in the product sheet:

1. **Purpose**: what exactly will they be used for?
2. **Legal basis**: what gives you the right to process them (for example the people's consent)?
3. **Minimisation**: which columns do you really need for the intended decision?
4. **Access**: who can see them? Is the repository public? Does an AI model receive them?
5. **Retention**: how long are they kept, and who deletes them afterwards?
6. **Hosting**: where are they stored, in which country?

**Pseudonymising is not anonymising.** Replacing "Léa Martin" with "A07" is pseudonymisation: with the lookup table, or by cross-referencing date, club and performance, the person can be found again; the data remains personal. Anonymisation makes re-identification impossible in practice, and it is hard to guarantee ([anonymisation, CNIL](https://www.cnil.fr/fr/technologies/lanonymisation-de-donnees-personnelles); [anonymisation and pseudonymisation in research, CNIL](https://www.cnil.fr/fr/recherche-scientifique-hors-sante-enjeux-et-avantages-de-lanonymisation-et-de-la-pseudonymisation)).

Often the simplest is to do without: synthetic or open data are enough to demonstrate a method.

## Going further

- The [GDPR developer guide](https://www.cnil.fr/fr/technologies/guide-rgpd-du-developpeur) (CNIL): security, minimisation, source code management.
- An overview: [GDPR, what is it about?](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on) (CNIL).
- When in doubt, the data protection officer (DPO) of the organisation providing the data.

## How to know it's done

- The product sheet says whether the project uses personal data and, if so, answers the six questions.
- No personal data is in the repository or its history, or sent to an AI model.
- The group can explain why its data is pseudonymised, anonymised or synthetic.
