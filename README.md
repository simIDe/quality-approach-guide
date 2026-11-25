# Quality Approach : guide du mini-projet

Guide de référence pour le mini-projet du cours Quality Approach (Master 2 STAPS, UFR STAPS Montpellier) : le brief, une liste de contrôle qualité, des fiches pratiques, des modèles de documents et un exemple qui fonctionne.

**Le site : <https://simide.github.io/quality-approach-guide/>**

Ce dépôt se consulte, il ne se copie pas. Votre projet peut être organisé tout autrement.

## Lancer le site en local

Il faut [Node.js](https://nodejs.org/) 20 ou plus récent.

```bash
npm ci
npm start
```

Le site s'ouvre sur <http://localhost:3000/quality-approach-guide/>. Pour vérifier comme la CI : `node scripts/verifier-navigation.mjs` puis `npm run build`.

## Lancer l'exemple en local

Il faut Python 3.11 ou plus récent et [uv](https://docs.astral.sh/uv/). Depuis la racine du dépôt :

```bash
uv run python exemples/charge-entrainement/lancer.py   # données, pipeline, contrôles, rapport
uv run pytest -q                                       # tests
```

Le rapport est écrit dans `exemples/charge-entrainement/sortie/rapport.md`. Voir le [README de l'exemple](exemples/charge-entrainement/README.md).

## Licence

Code sous licence MIT, textes sous licence CC BY 4.0. Voir [LICENSE](LICENSE).
