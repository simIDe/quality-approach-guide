---
title: "01 · Collaborer sur GitHub"
sidebar_position: 1
---

*Comment travailler à trois sur le même code sans se marcher dessus ?*

## Le problème

Léa corrige le calcul de la charge d'entraînement pendant que Hugo renomme les colonnes du même fichier, et chacun pousse directement sur la branche principale. Le soir, le script ne tourne plus et personne ne sait quelle modification l'a cassé.

## Le minimum utile

Quatre habitudes suffisent pour commencer.

1. **Répartir le travail avec des issues.** Une *issue* est un ticket GitHub : une tâche, un défaut ou une question, avec un titre, une description et une personne assignée. Une issue par tâche de quelques heures, pas plus.
2. **Travailler sur une branche courte.** Une *branche* est une ligne de travail parallèle à la branche principale (`main`). Elle ne vit que le temps d'une tâche : un à deux jours.
3. **Proposer la modification par une pull request.** Une *pull request* (PR) demande à fusionner une branche dans `main` ; GitHub y affiche le *diff*, c'est-à-dire les lignes ajoutées et supprimées.
4. **Faire relire par un autre membre.** Quelqu'un d'autre que l'auteur lit le diff, pose ses questions, puis approuve et fusionne.

```bash
git switch main
git pull                               # partir de la dernière version
git switch -c 12-calcul-charge         # une branche par issue (ici l'issue n° 12)
# ... modifier, tester ...
git add src/charge.py
git commit -m "Calcule la charge en minutes et non en heures"
git push -u origin 12-calcul-charge
gh pr create --fill                    # ou le bouton « Compare & pull request » sur GitHub
```

Un *commit* est un enregistrement daté d'un ensemble de modifications, avec un message. Un bon message dit ce que fait le changement, en une phrase. Écrire `Closes #12` dans la description de la PR ferme l'issue automatiquement à la fusion.

## Pour aller plus loin

- Protéger `main` dans les réglages du dépôt pour interdire la fusion sans relecture ([documentation GitHub sur les pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests)).
- Suivre les issues dans un tableau GitHub Projects (à faire, en cours, fait) plutôt qu'en liste.
- Travailler à deux sur le même écran (*pair programming*) pour les parties délicates, la relecture se fait alors en direct.

## Comment savoir si c'est fait

- L'historique de `main` ne contient que des fusions de pull requests, et chaque PR a été relue par quelqu'un d'autre que son auteur.
- Chaque membre du groupe a ouvert au moins une PR et en a relu au moins une.
- En lisant la liste des issues fermées, un tiers comprend qui a fait quoi.
