---
title: Liste de contrôle
sidebar_position: 1
---

# Liste de contrôle qualité

Deux listes de questions, à reprendre avant chaque livraison. Une réponse « non » n'est pas une faute : c'est une limite à corriger ou à annoncer.

## Les données

- [ ] **Exactitude :** les valeurs ont-elles été confrontées à des bornes plausibles (échelles, unités, dates) ?
- [ ] **Complétude :** sait-on combien de valeurs ou de lignes manquent, et ce qu'on en fait ?
- [ ] **Fraîcheur :** la date des données est-elle connue, et suffit-elle pour la décision de l'utilisateur ?
- [ ] **Cohérence :** une même information a-t-elle le même nom, le même format et la même unité partout ?
- [ ] **Unicité :** a-t-on vérifié qu'aucune ligne n'apparaît en double ?
- [ ] **Origine :** chaque source est-elle notée, avec son adresse, sa licence et sa date de récupération ?
- [ ] **Défauts :** chaque défaut trouvé est-il corrigé, exclu ou signalé, et ce choix est-il écrit ?
- [ ] **Limites :** les limites connues sont-elles écrites là où l'utilisateur les lira ?

## Le projet

Les six premières questions reprennent les caractéristiques d'un *data product* (produit de données conçu pour un utilisateur, avec une promesse) décrites par Zhamak Dehghani en 2019 : [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html).

- [ ] **Trouvable** (*discoverable*) : l'utilisateur sait-il où trouver le produit ?
- [ ] **Adressable** (*addressable*) : le produit a-t-il une adresse stable (chemin, URL, nom de table) ?
- [ ] **Digne de confiance** (*trustworthy*) : la promesse et les contrôles qui la vérifient sont-ils visibles ?
- [ ] **Auto-décrit** (*self-describing*) : chaque colonne ou champ est-il expliqué, par exemple dans un dictionnaire de données ?
- [ ] **Interopérable** (*interoperable*) : la sortie est-elle dans un format ouvert et courant ?
- [ ] **Sécurisé** (*secure*) : les secrets et les données personnelles sont-ils hors du dépôt et hors des échanges avec un modèle ?
- [ ] **Relançable par un tiers :** quelqu'un hors du groupe peut-il relancer le projet avec le seul README ?
- [ ] **Historique lisible :** les commits et les pull requests racontent-ils ce qui a été fait et pourquoi ?
- [ ] **Vérifications automatiques :** les contrôles et les tests tournent-ils sans intervention à chaque modification ?
