---
title: "02 · Contrôler des données"
sidebar_position: 2
---

*Comment savoir si mes données sont bonnes ?*

## Le problème

Votre tableau de charge d'entraînement annonce qu'un athlète a couru 90 heures cette semaine : une séance a été saisie en heures au lieu de minutes. L'entraîneur ne vous fera plus confiance si c'est lui qui le découvre.

## Le minimum utile

« Bonnes » veut dire bonnes *pour l'usage promis*. Choisissez, pour chacune des cinq dimensions de la qualité, au moins un contrôle qui a du sens pour votre utilisateur.

| Dimension | La question | Exemple de contrôle |
| --- | --- | --- |
| Exactitude | Les valeurs sont-elles plausibles ? | Effort perçu entre 0 et 10, durée entre 5 et 300 minutes |
| Complétude | Manque-t-il des lignes ou des valeurs ? | Chaque athlète a au moins une séance chaque semaine |
| Fraîcheur | Les données sont-elles assez récentes ? | La séance la plus récente date de moins de 7 jours |
| Cohérence | Les données se contredisent-elles ? | Pas de séance datée dans le futur |
| Unicité | Une même chose est-elle comptée deux fois ? | Pas deux séances identiques (athlète, date, durée) |

En SQL (ici SQLite), chaque contrôle est une requête qui renvoie les lignes en défaut ; zéro ligne veut dire contrôle réussi.

```sql
-- Exactitude : effort hors de l'échelle ou durée improbable
SELECT * FROM seances WHERE effort NOT BETWEEN 0 AND 10 OR duree_min NOT BETWEEN 5 AND 300;
-- Unicité : séances en double
SELECT athlete, date, duree_min, COUNT(*) AS n
FROM seances GROUP BY athlete, date, duree_min HAVING COUNT(*) > 1;
-- Fraîcheur : une ligne si la séance la plus récente a plus de 7 jours
SELECT MAX(date) AS derniere FROM seances HAVING MAX(date) < date('now', '-7 days');
```

Les mêmes contrôles en Python, avec le module `sqlite3` de la bibliothèque standard :

```python
import sqlite3

con = sqlite3.connect("donnees/seances.db")
hors_echelle = con.execute("SELECT * FROM seances WHERE effort NOT BETWEEN 0 AND 10").fetchall()
assert not hors_echelle, f"{len(hors_echelle)} séance(s) avec un effort hors échelle"
```

**Quoi faire d'un défaut trouvé.** Trois réponses possibles, à choisir au cas par cas :

- **corriger** quand la bonne valeur est certaine (une durée de 1,5 manifestement en heures devient 90 minutes) ;
- **exclure** quand elle ne l'est pas (un effort de 14 sur 10) ;
- **signaler** quand on garde la ligne mais que l'utilisateur doit le savoir (une semaine manquante).

Dans les trois cas, écrivez-le : combien de lignes, quelle règle, pourquoi. Le rapport livré et le journal de méthode sont les bons endroits. L'exemple du dépôt fait exactement cela : [exemples/charge-entrainement](https://github.com/simIDe/quality-approach-guide/tree/main/exemples/charge-entrainement).

## Pour aller plus loin

- Transformer chaque contrôle en test pytest, pour qu'il tourne tout seul (voir [la fiche 04](./04-automatiser-une-verification.md)).
- Décrire chaque colonne (type, unité, valeurs possibles) dans un dictionnaire de données : les contrôles d'exactitude en découlent.
- Utiliser DuckDB pour contrôler directement un gros fichier CSV ou Parquet, sans le charger dans une base ([documentation DuckDB](https://duckdb.org/docs/)).

## Comment savoir si c'est fait

- Chaque dimension a au moins un contrôle écrit, que l'on peut relancer.
- Chaque défaut trouvé a une décision (corrigé, exclu, signalé) notée quelque part.
- Le produit livré annonce ses limites connues.
