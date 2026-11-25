# Fiche produit : Charge d'entraînement hebdomadaire, club de course à pied

| Rubrique | Contenu |
| --- | --- |
| **Nom du produit** | Charge d'entraînement hebdomadaire |
| **Utilisateur** | L'entraîneur du club de course à pied |
| **Décision** | Chaque lundi, alléger, maintenir ou augmenter la charge de la semaine pour chaque athlète |
| **Responsable** | Le groupe qui maintient l'exemple (ici, l'enseignant) |

## Promesse

- **Contenu :** une ligne par athlète et par semaine, avec le nombre de séances, les minutes courues et la charge (effort perçu de 0 à 10 × durée en minutes, en unités arbitraires).
- **Fraîcheur :** les huit semaines qui se terminent à la date de fin des données (le dimanche 22 novembre 2026). Le contrôle de fraîcheur échoue si la dernière séance date de plus de sept jours avant cette date.
- **Périmètre :** les six athlètes du fichier de séances, sur huit semaines. Les séances sont contrôlées selon cinq dimensions (exactitude, complétude, fraîcheur, cohérence, unicité) et chaque défaut trouvé est écrit dans le rapport avec son traitement.

## Ce qui n'est pas garanti

- L'effort perçu est déclaré par l'athlète : il reste subjectif.
- Une semaine sans séance enregistrée est signalée, pas complétée : elle n'apparaît pas dans le tableau.
- Une séance dont l'effort est hors de l'échelle est exclue : la charge de cette semaine est sous-estimée.
- Une durée sous dix minutes est considérée comme saisie en heures et convertie. Une vraie séance de moins de dix minutes serait donc mal corrigée.
- Le produit ne dit pas quelle charge est bonne pour un athlète : la décision reste à l'entraîneur.

## Données utilisées et origine

| Source | Origine | Date |
| --- | --- | --- |
| `data/seances.csv` : une ligne par séance (athlète, date, durée, effort perçu) | Générée par `generer.py`, graine fixe, quatre défauts introduits volontairement | Séances du 28 septembre au 22 novembre 2026, recréées à chaque lancement |

## Données personnelles

Non. Les données sont synthétiques et les identifiants d'athlètes (A01 à A06) ne correspondent à personne. Un vrai club manipulerait des données de santé (effort, charge) : il faudrait alors se poser les questions de la fiche « Données personnelles » avant de commencer.
