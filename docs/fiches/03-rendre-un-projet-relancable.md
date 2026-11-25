---
title: "03 · Rendre un projet relançable"
sidebar_position: 3
---

*Quelqu'un d'autre peut-il relancer mon projet ?*

## Le problème

Le 20 janvier, un autre groupe aura dix minutes pour relancer votre projet avec votre seul README. Si le script cherche `C:\Users\lea\Bureau\seances.csv`, demande une bibliothèque installée « à la main » ou donne des chiffres différents à chaque exécution, c'est perdu.

## Le minimum utile

Cinq points, du plus important au moins important.

**1. Des dépendances figées.** Une façon simple est [uv](https://docs.astral.sh/uv/), un gestionnaire de projets Python : il note les dépendances dans `pyproject.toml` et leurs versions exactes dans `uv.lock`. Les deux fichiers sont versionnés avec le code.

```bash
uv init                 # crée pyproject.toml (une fois, au début du projet)
uv add pandas pytest    # ajoute des dépendances et met à jour uv.lock
uv sync                 # sur une autre machine : installe exactement les mêmes versions
```

**2. Une seule commande pour tout lancer.** Un script d'entrée qui enchaîne les étapes (données, transformation, sortie) :

```bash
uv run python pipeline.py
```

`uv run` lance la commande dans l'environnement du projet, sans avoir à l'activer.

**3. Des chemins relatifs au projet**, jamais à votre machine :

```python
from pathlib import Path

RACINE = Path(__file__).resolve().parent
SEANCES = RACINE / "donnees" / "seances.csv"   # fonctionne sous Windows, macOS et Linux
```

**4. Une graine aléatoire fixe** dès qu'il y a du hasard (données simulées, échantillonnage, modèle) :

```python
import random

random.seed(42)   # numpy : rng = numpy.random.default_rng(42)
```

**5. Un README d'installation** qui tient en quelques lignes : prérequis (version de Python, uv), commandes à taper dans l'ordre, ce qu'on doit obtenir à la fin.

## Pour aller plus loin

- Sans uv, l'équivalent avec pip et venv : `python -m venv .venv`, activer l'environnement, puis `pip install -r requirements.txt`, avec des versions figées dans le fichier (`pandas==2.2.3`, produit par `pip freeze > requirements.txt`).
- Un fichier `Makefile` ou un script `lancer.sh` / `lancer.ps1` quand il y a plusieurs commandes à enchaîner.
- Un conteneur Docker fige aussi le système, au prix d'un outil de plus à installer et à expliquer.

## Comment savoir si c'est fait

- Un membre du groupe clone le dépôt dans un dossier neuf et relance tout avec le seul README, sans rien demander aux autres.
- Deux exécutions successives donnent exactement les mêmes résultats.
- Aucun chemin absolu dans le code : une recherche de `C:\` ou `/home/` ne trouve rien.
