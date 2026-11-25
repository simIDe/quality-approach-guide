---
title: Fiche produit
sidebar_position: 1
---

# Modèle : fiche produit

Une page qui dit pour qui est le produit, à quelle décision il sert et ce qu'il garantit. Vous pouvez copier ce modèle tel quel ou l'adapter : [fichier Markdown brut](https://raw.githubusercontent.com/simIDe/quality-approach-guide/main/i18n/fr/docusaurus-plugin-content-docs/current/templates/product-sheet.md).

## Le modèle

**Nom du produit :**

**Utilisateur :** qui, précisément, va s'en servir.

**Décision :** ce que l'utilisateur décide grâce au produit.

**Promesse :**

- *Contenu :* ce que contient le produit (lignes, colonnes, indicateurs).
- *Fraîcheur :* à quelle fréquence il est mis à jour, et jusqu'à quelle date il porte.
- *Périmètre :* ce qu'il couvre (population, territoire, période).

**Ce qui n'est pas garanti :**

**Responsable :** qui répond du produit.

**Données utilisées et leur origine :**

| Source | Adresse | Licence | Date de récupération |
| --- | --- | --- | --- |
| | | | |

**Données personnelles :** oui ou non. Si oui, lesquelles et comment elles sont protégées.

## Un exemple rempli

**Nom du produit :** Charge d'entraînement hebdomadaire, club de course à pied.

**Utilisateur :** l'entraîneur d'un club de course à pied.

**Décision :** ajuster la charge de la semaine suivante pour chaque athlète.

**Promesse :**

- *Contenu :* une ligne par athlète et par semaine ; charge = effort perçu de la séance (RPE, *rating of perceived exertion*, de 0 à 10) × durée en minutes, additionnée sur la semaine.
- *Fraîcheur :* recalculée à chaque lancement du pipeline, à partir des séances disponibles.
- *Périmètre :* les huit dernières semaines, tous les athlètes présents dans le fichier de séances.

**Ce qui n'est pas garanti :** l'exactitude de l'effort perçu, qui reste une déclaration de l'athlète ; la présence de toutes les séances (une semaine sans séance peut être un oubli de saisie) ; toute interprétation médicale ou de risque de blessure.

**Responsable :** le mainteneur du dépôt guide.

**Données utilisées et leur origine :**

| Source | Adresse | Licence | Date de récupération |
| --- | --- | --- | --- |
| Séances synthétiques (identifiant d'athlète fictif, date, durée, effort perçu) | Générées par un script de l'exemple, avec une graine aléatoire fixe | Celle du dépôt | Régénérées à chaque lancement |

**Données personnelles :** non. Les athlètes sont fictifs et les données sont générées par un script. Avec de vraies séances, l'effort perçu et la durée d'entraînement d'une personne identifiable seraient des données personnelles, et la fiche le signalerait.
