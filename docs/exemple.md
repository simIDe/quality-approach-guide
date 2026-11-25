---
title: L'exemple
---

# L'exemple : charge d'entraînement hebdomadaire

Le dossier [`exemples/charge-entrainement/`](https://github.com/simIDe/quality-approach-guide/tree/main/exemples/charge-entrainement) contient un *data product* (produit de données : des données préparées pour un utilisateur et une décision précis) minimal, qui tourne de bout en bout avec une seule commande. Il se lit en vingt minutes : moins de 300 lignes de Python, tests compris.

Il montre une façon de faire, pas la seule. Votre projet peut utiliser d'autres outils et une autre organisation.

## Ce que fait l'exemple

L'utilisateur est l'entraîneur d'un club de course à pied. Il reçoit un rapport avec une ligne par athlète et par semaine sur huit semaines, et la charge de chaque semaine : effort perçu (0 à 10) × durée en minutes.

1. [`generer.py`](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/generer.py) crée un CSV de séances synthétiques, avec une graine fixe et une date de fin fixe : le fichier est le même à chaque lancement. Les athlètes (A01 à A06) sont fictifs.
2. [`pipeline.py`](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/pipeline.py) charge le CSV dans SQLite, nettoie les séances et calcule la table hebdomadaire en SQL.
3. [`controles.py`](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/controles.py) contrôle les séances brutes selon les cinq dimensions : exactitude, complétude, fraîcheur, cohérence, unicité.
4. [`lancer.py`](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/lancer.py) enchaîne les étapes et écrit le rapport Markdown.

## Les quatre défauts et leur traitement

Le générateur introduit volontairement quatre défauts. Chacun est détecté par un contrôle, puis traité d'une des trois façons possibles : corrigé, exclu ou signalé.

| Défaut | Contrôle qui le détecte | Traitement |
| --- | --- | --- |
| Trois durées saisies en heures au lieu de minutes | **cohérence** : toutes les durées doivent être en minutes, donc au moins 10 | corrigé : durée × 60 |
| Une semaine sans séance pour l'athlète A03 | **complétude** : huit semaines attendues par athlète | signalé : la semaine manque au tableau, aucune charge n'est inventée |
| Une séance saisie deux fois | **unicité** : une séance par athlète et par jour | exclu : un seul exemplaire est gardé |
| Un effort perçu de 14 | **exactitude** : l'effort doit être entre 0 et 10 | exclu : la vraie valeur est inconnue |

Le contrôle de **fraîcheur** vérifie que la dernière séance date de moins de sept jours avant la date de fin. Il passe : un contrôle qui ne trouve rien est aussi une information.

Le rapport reprend ce tableau, liste chaque anomalie trouvée, puis donne la table hebdomadaire. Un test, dans [`tests/test_exemple.py`](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/tests/test_exemple.py), échoue si l'un des quatre défauts n'est plus détecté.

## Le lancer chez vous

Avec Python 3.11 ou plus récent et [uv](https://docs.astral.sh/uv/), depuis la racine du dépôt cloné :

```bash
uv run python exemples/charge-entrainement/lancer.py
uv run pytest -q
```

Le rapport est écrit dans `exemples/charge-entrainement/sortie/rapport.md`. Le [README de l'exemple](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/README.md) donne aussi l'équivalent avec pip et venv.

À chaque pull request (proposition de modification relue avant d'être fusionnée), le workflow [`exemple.yml`](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/exemple.yml) relance la commande et les tests sur Linux, Windows et macOS.

## Les documents qui l'accompagnent

- [Fiche produit](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/fiche-produit.md) : pour qui, pour quelle décision, ce qui est garanti et ce qui ne l'est pas.
- [Dictionnaire de données](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/dictionnaire-de-donnees.md) : chaque colonne de chaque table.
- [Journal de méthode](https://github.com/simIDe/quality-approach-guide/blob/main/exemples/charge-entrainement/journal-de-methode.md) (extrait) : les décisions, l'usage de l'IA, ce qu'on referait autrement.
