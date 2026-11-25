---
title: "06 · Travailler avec un agent"
sidebar_position: 6
---

*Comment utiliser un agent de code sans perdre la main ?*

## Le problème

Vous demandez à un agent de code (un assistant d'IA qui lit, écrit et lance du code dans votre projet) de « nettoyer les données de séances ». Il modifie six fichiers, les tests passent, mais personne dans le groupe ne sait expliquer ce qu'il a supprimé, et le 20 janvier chacun devra pouvoir le faire.

## Le minimum utile

**1. Écrire la demande avant le code.** Quelques lignes : le but, les fichiers concernés, ce qui ne doit pas changer, comment on saura que c'est réussi. Si vous ne savez pas l'écrire, l'agent ne le devinera pas.

```text
But : convertir en minutes les durées saisies en heures dans seances.csv.
Règle : une durée inférieure à 5 est considérée comme des heures.
Ne pas toucher : le calcul de la charge, les autres colonnes.
Réussi si : le nouveau test passe et les anciens aussi.
Propose un plan avant de modifier quoi que ce soit.
```

**2. Faire écrire les tests d'abord.** Demandez le test, lisez-le, vérifiez qu'il échoue, puis seulement demandez le code qui le fait passer. Refusez toute modification d'un test existant faite pour qu'il passe.

**3. Relire le diff.** Le *diff* est la liste des lignes ajoutées et supprimées. Lisez-le en entier avant chaque commit (enregistrement de modifications), avec `git diff` ou dans la pull request, et demandez à l'agent d'expliquer chaque ligne que vous ne comprenez pas.

**4. Ne jamais lui envoyer** de secret (mot de passe, clé d'API, fichier `.env`), ni de données personnelles : noms d'athlètes, données de santé, fichiers bruts de montres connectées. Travaillez sur un échantillon synthétique ou pseudonymisé (voir [la fiche 07](./07-donnees-personnelles.md)).

**5. Tenir le journal.** Dans le journal de méthode, à chaque usage notable : ce qui a été demandé, ce qui a été gardé, ce qui a été rejeté ou corrigé, et pourquoi. C'est une preuve attendue, pas une formalité.

## Pour aller plus loin

- Écrire un fichier `AGENTS.md` à la racine du projet : commandes pour installer et tester, règles du groupe. De nombreux agents lisent ce fichier au démarrage ; ce dépôt en a un ([AGENTS.md](https://github.com/simIDe/quality-approach-guide/blob/main/AGENTS.md)).
- Faire travailler l'agent sur une branche à part, fusionnée par pull request après relecture humaine (voir [la fiche 01](./01-collaborer-sur-github.md)).
- Utiliser un modèle local quand les données ne doivent pas quitter la machine, au prix d'une qualité souvent moindre.

## Comment savoir si c'est fait

- Chaque membre peut expliquer n'importe quel fichier du projet, y compris ceux écrits par l'agent.
- Le journal de méthode contient au moins un exemple de proposition de l'agent rejetée ou corrigée.
- Aucun secret ni donnée personnelle n'apparaît dans les conversations avec l'agent ni dans l'historique git.
