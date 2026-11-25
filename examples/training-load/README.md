# Exemple : charge d'entraînement hebdomadaire

Un *data product* (produit de données : des données préparées pour un utilisateur précis et une décision précise) minimal, de bout en bout.

- **Pour qui :** l'entraîneur d'un club de course à pied.
- **Ce qu'il obtient :** un rapport Markdown avec une ligne par athlète et par semaine sur huit semaines, et la charge de chaque semaine (effort perçu de 0 à 10 × durée en minutes).
- **Les données :** synthétiques, générées par un script avec une graine fixe. Les athlètes (A01 à A06) sont fictifs. Aucune donnée personnelle.

Le générateur introduit volontairement quatre défauts. Les contrôles les détectent et le rapport dit comment chacun est traité.

| Défaut introduit | Dimension qui le détecte | Traitement |
| --- | --- | --- |
| Trois durées saisies en heures au lieu de minutes | cohérence | corrigé (durée × 60) |
| Une semaine sans séance pour l'athlète A03 | complétude | signalé (rien n'est inventé) |
| Une séance saisie deux fois | unicité | exclu (un seul exemplaire gardé) |
| Un effort perçu de 14 sur une échelle de 0 à 10 | exactitude | exclu (la vraie valeur est inconnue) |

Le cinquième contrôle, la fraîcheur, vérifie que la dernière séance date de moins de sept jours avant la date de fin des données. Il passe.

## Lancer l'exemple

Il faut Python 3.11 ou plus récent et [uv](https://docs.astral.sh/uv/). Depuis la racine du dépôt :

```bash
uv run python exemples/charge-entrainement/lancer.py
```

Cette commande installe l'environnement si besoin, génère `data/seances.csv`, le charge dans SQLite, lance les contrôles, calcule la table hebdomadaire et écrit `sortie/rapport.md`. La base `sortie/charge.sqlite` reste disponible pour explorer les tables. Les dossiers `data/` et `sortie/` sont recréés à chaque lancement et ne sont pas versionnés.

## Lancer les tests

```bash
uv run pytest -q
```

## Sans uv : pip et venv

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install pytest
python exemples/charge-entrainement/lancer.py
python -m pytest -q
```

L'exemple n'utilise que la bibliothèque standard de Python ; pytest sert seulement aux tests. Avec pip, la version de pytest n'est pas figée comme elle l'est par `uv.lock`.

## Ce qu'il y a dans ce dossier

| Fichier | Rôle |
| --- | --- |
| `lancer.py` | point d'entrée unique : enchaîne les étapes et écrit le rapport |
| `generer.py` | génère le CSV synthétique et ses quatre défauts |
| `pipeline.py` | charge le CSV dans SQLite, nettoie, calcule la charge en SQL |
| `controles.py` | un contrôle qualité par dimension |
| `tests/test_exemple.py` | tests de la transformation et des contrôles |
| `fiche-produit.md` | pour qui, pour quelle décision, ce qui est garanti ou non |
| `dictionnaire-de-donnees.md` | chaque colonne de chaque table |
| `journal-de-methode.md` | extrait du journal : décisions, usage de l'IA |

Ceci est un exemple, pas un modèle à recopier.
