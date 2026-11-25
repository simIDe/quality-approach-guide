---
title: Comment ce site est fait
---

# Comment ce site est fait

Ce site applique à lui-même ce que le guide propose pour votre projet : chaque modification passe par une *pull request* (demande de fusion relue avant d'entrer dans la branche principale), une vérification automatique, puis une publication sans intervention manuelle.

## La chaîne en quatre étapes

1. **J'écris en Markdown.** Chaque page est un fichier du dossier [`docs/`](https://github.com/simIDe/quality-approach-guide/tree/main/docs). Le site est construit par [Docusaurus](https://docusaurus.io/), un générateur de site statique libre ; sa configuration tient dans [`docusaurus.config.mjs`](https://github.com/simIDe/quality-approach-guide/blob/main/docusaurus.config.mjs) et la navigation dans [`sidebars.mjs`](https://github.com/simIDe/quality-approach-guide/blob/main/sidebars.mjs). En local, `npm start` affiche le site pendant qu'on écrit.
2. **J'ouvre une pull request.** La modification est faite sur une branche, puis proposée. Exemple réel : la [pull request n° 3](https://github.com/simIDe/quality-approach-guide/pull/3), qui a ajouté les fiches pratiques, une fiche par commit. Voir la [fiche 01](./guides/01-collaborate-on-github.md).
3. **La vérification tourne.** Le workflow [`docs.yml`](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/docs.yml) vérifie que chaque page figure dans la navigation, puis construit le site : un lien interne ou une ancre cassés font échouer la construction. Un second workflow, [`example.yml`](https://github.com/simIDe/quality-approach-guide/blob/main/.github/workflows/example.yml), relance l'exemple et ses tests sous Linux, Windows et macOS. Tant qu'une vérification est rouge, on ne fusionne pas. Voir la [fiche 04](./guides/04-automate-a-check.md).
4. **La fusion publie.** Une fois la pull request fusionnée sur `main`, le même workflow publie le site sur GitHub Pages par le mécanisme officiel de GitHub Actions. Personne ne copie de fichiers à la main. Voir la [fiche 05](./guides/05-publish-a-release.md).

## Pourquoi ces choix

- **Docusaurus** est maintenu, libre (licence MIT) et lit des fichiers Markdown ordinaires : le contenu reste lisible sur GitHub et réutilisable avec un autre outil.
- **La recherche** est construite avec le site ([`docusaurus-search-local`](https://github.com/easyops-cn/docusaurus-search-local)) : aucun service tiers, aucun compte.
- **Les versions sont figées** dans `package-lock.json` (site) et `uv.lock` (exemple) : le site construit aujourd'hui sera le même dans six semaines.

Votre projet n'a besoin d'aucun de ces outils. L'idée à retenir est la chaîne : écrire, proposer, vérifier automatiquement, publier.
