# Consignes pour les agents de code

## Le dépôt

Ce dépôt est le guide du mini-projet du cours Quality Approach (Master 2 STAPS). Il contient un site de documentation (Docusaurus, dans `docs/`) et un exemple minimal de *data product* (dans `exemples/charge-entrainement/`). Toute la documentation est en français ; les termes techniques anglais usuels sont conservés et définis à leur première apparition.

## Commandes

```bash
# Installer l'environnement Python
uv sync

# Lancer l'exemple de bout en bout
uv run python exemples/charge-entrainement/lancer.py

# Lancer les tests
uv run pytest -q

# Lancer le site en local
npm ci
npm start

# Vérifier le site comme la CI
node scripts/verifier-navigation.mjs
npm run build
```

## Règles

- Ne pas inventer de données ni de sources.
- Écrire les tests avant le code.
- Ne jamais modifier un test pour le faire passer.
- Ne jamais manipuler de données personnelles.
- Proposer un plan avant une modification de plus d'un fichier.
