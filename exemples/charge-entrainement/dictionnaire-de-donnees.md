# Dictionnaire de données

Les trois tables de la base SQLite `sortie/charge.sqlite`, recréée à chaque lancement de `lancer.py`.

## seances_brutes

Copie du fichier `data/seances.csv`, sans aucune modification. Les contrôles qualité portent sur cette table.

| Colonne | Type | Unité | Définition | Valeurs possibles | Source |
| --- | --- | --- | --- | --- | --- |
| athlete | TEXT | — | Identifiant fictif de l'athlète | A01 à A06 | `data/seances.csv` |
| date | TEXT | jour (AAAA-MM-JJ) | Date de la séance | du 2026-09-28 au 2026-11-22 | `data/seances.csv` |
| duree | REAL | minutes, parfois heures par erreur | Durée de la séance telle que saisie | 30 à 100 attendu ; sous 10, la valeur est en heures | `data/seances.csv` |
| rpe | INTEGER | point d'échelle | Effort perçu déclaré par l'athlète (RPE, *rating of perceived exertion*) | 0 à 10 attendu ; toute autre valeur est une erreur | `data/seances.csv` |

## seances

Séances nettoyées : doublons exacts exclus, durées en heures converties, efforts hors échelle exclus.

| Colonne | Type | Unité | Définition | Valeurs possibles | Source |
| --- | --- | --- | --- | --- | --- |
| athlete | TEXT | — | Identifiant fictif de l'athlète | A01 à A06 | `seances_brutes.athlete` |
| date | TEXT | jour (AAAA-MM-JJ) | Date de la séance | du 2026-09-28 au 2026-11-22 | `seances_brutes.date` |
| duree_min | REAL | minutes | Durée de la séance, convertie en minutes si elle était saisie en heures | 10 et plus | `seances_brutes.duree` |
| rpe | INTEGER | point d'échelle | Effort perçu | 0 à 10 | `seances_brutes.rpe` |

## charge_hebdo

Le produit livré : une ligne par athlète et par semaine où au moins une séance est enregistrée.

| Colonne | Type | Unité | Définition | Valeurs possibles | Source |
| --- | --- | --- | --- | --- | --- |
| athlete | TEXT | — | Identifiant fictif de l'athlète | A01 à A06 | `seances.athlete` |
| semaine | TEXT | jour (AAAA-MM-JJ) | Lundi de la semaine | huit lundis, du 2026-09-28 au 2026-11-16 | calculée depuis `seances.date` |
| nb_seances | INTEGER | séances | Nombre de séances retenues dans la semaine | 1 à 7 (3 dans les données générées, moins si une séance a été exclue) | `COUNT(*)` sur `seances` |
| minutes | REAL | minutes | Durée totale courue dans la semaine | 0 et plus | somme de `seances.duree_min` |
| charge | REAL | unité arbitraire (UA) | Somme sur la semaine de l'effort perçu × durée en minutes | 0 et plus | somme de `seances.rpe × seances.duree_min` |
