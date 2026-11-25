---
title: "05 · Publier une version"
sidebar_position: 5
---

*Comment dire « ceci est la version livrée » ?*

## Le problème

Le 18 janvier, vous livrez le projet, mais le groupe continue à corriger des détails dans les jours qui suivent. Le 20 janvier, l'entraîneur, l'enseignant et le groupe qui relance votre projet ne regardent plus la même chose.

## Le minimum utile

Marquer la version livrée par un tag, puis en faire une release.

- Un *tag* est une étiquette posée sur un commit précis (un *commit* est un enregistrement daté de modifications). Il ne bouge plus, même si la branche avance.
- Une *release* GitHub est une page attachée à un tag : un titre, des notes de version et une archive du code téléchargeable ([documentation GitHub sur les releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)).

```bash
git switch main
git pull                                         # la version fusionnée et relue
git tag -a v1.0.0 -m "Version livrée le 18 janvier 2027"
git push origin v1.0.0
gh release create v1.0.0 --title "v1.0.0" --notes-file NOTES.md
```

La release peut aussi se créer depuis l'interface : *Releases*, puis *Draft a new release*.

Les notes de version tiennent en trois lignes : ce que fait le produit, ce qui a changé depuis la version précédente, les limites connues.

```markdown
Tableau hebdomadaire de charge d'entraînement, 12 athlètes, 8 dernières semaines.
Nouveau : les séances saisies en heures sont converties en minutes.
Limite connue : une semaine manquante pour un athlète, signalée dans le rapport.
```

Une convention courante pour le numéro : `v1.0.0` pour la première version livrée, `v1.0.1` pour une correction, `v1.1.0` pour un ajout. Rien n'oblige à la suivre ; l'important est qu'un numéro désigne toujours le même état du code.

## Pour aller plus loin

- Publier une documentation ou un rapport sur GitHub Pages, comme le fait ce dépôt : son site est construit avec Docusaurus par GitHub Actions et publié à chaque fusion ([workflows personnalisés pour GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)).
- Joindre à la release le fichier produit (rapport, CSV nettoyé) avec `gh release upload v1.0.0 rapport.md`, pour que l'utilisateur n'ait rien à relancer.
- Tenir un fichier `CHANGELOG.md` qui accumule les notes de chaque version.

## Comment savoir si c'est fait

- La page *Releases* du dépôt montre une version datée avec ses notes.
- `git switch --detach v1.0.0` sur une autre machine, puis les commandes du README, redonnent exactement le produit livré.
- La fiche produit et le journal de méthode citent le numéro de version livrée.
