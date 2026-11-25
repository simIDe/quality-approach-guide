---
title: "04 · Automatiser une vérification"
sidebar_position: 4
---

*Comment faire tourner mes contrôles tout seuls ?*

## Le problème

Vos tests et vos contrôles de données existent, mais chacun oublie de les lancer avant de pousser son travail. Hugo fusionne une modification qui casse le calcul de la charge, et l'erreur n'est découverte que la veille de la livraison.

## Le minimum utile

GitHub Actions lance des commandes sur une machine de GitHub à chaque modification du dépôt, gratuitement pour un dépôt public. Un *workflow* est un fichier YAML placé dans `.github/workflows/` qui dit quand et quoi lancer.

Ce workflow lance pytest à chaque *push* (envoi de commits vers GitHub) et à chaque pull request (demande de fusion d'une branche) :

```yaml
# .github/workflows/tests.yml
name: Tests

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7        # récupère le code du dépôt
      - uses: astral-sh/setup-uv@v10     # installe uv
      - run: uv sync                     # installe les dépendances figées (uv.lock)
      - run: uv run pytest -q            # lance les tests ; un échec fait échouer le workflow
```

Il suppose un projet géré avec uv et des tests pytest (voir [la fiche 03](./03-rendre-un-projet-relancable.md)). Vos contrôles de données peuvent tourner de la même façon, écrits comme des tests ou lancés par une ligne `run:` de plus (`uv run python controles.py`), pourvu que le script s'arrête en erreur quand un contrôle échoue.

**Lire un échec.** Une croix rouge apparaît à côté du commit et dans la pull request.

1. Cliquer sur la croix, puis sur *Details* : la liste des étapes s'affiche, celle qui a échoué est marquée.
2. Ouvrir cette étape et descendre jusqu'aux premières lignes en erreur : pytest y donne le nom du test et la valeur obtenue face à la valeur attendue.
3. Reproduire en local avec la même commande (`uv run pytest -q`), corriger, pousser : le workflow repart tout seul.

**Deux exemples réels dans ce dépôt :**

- [exemple.yml](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/exemple.yml) installe l'environnement de l'exemple, génère les données, lance le pipeline puis les tests ;
- [docs.yml](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/docs.yml) construit ce site à chaque pull request et le publie à chaque fusion.

## Pour aller plus loin

- Ajouter un linter comme Ruff dans une étape de plus, pour vérifier le style du code.
- Lancer les contrôles de données chaque nuit avec un déclencheur `schedule`, utile si la source change toute seule ([démarrage rapide GitHub Actions](https://docs.github.com/en/actions/get-started/quickstart)).
- Exiger que le workflow soit vert avant toute fusion, dans les réglages de protection de la branche principale.

## Comment savoir si c'est fait

- L'onglet *Actions* du dépôt montre une exécution pour chaque push et chaque pull request.
- Un test volontairement cassé sur une branche fait apparaître une croix rouge dans la pull request.
- Chaque membre du groupe sait retrouver, dans le journal d'exécution, le test qui a échoué.
