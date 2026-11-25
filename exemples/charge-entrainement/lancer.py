"""Point d'entrée unique : données, pipeline, contrôles, rapport.

Depuis la racine du dépôt : uv run python exemples/charge-entrainement/lancer.py
"""
import sqlite3
from contextlib import closing
from pathlib import Path

from controles import controler
from generer import DATE_FIN, ecrire_csv, generer_seances, premier_lundi
from pipeline import charger, transformer

DOSSIER = Path(__file__).resolve().parent  # les chemins ne dépendent pas du dossier courant


def ecrire_rapport(controles, connexion, chemin):
    lignes = ["# Charge d'entraînement hebdomadaire", "",
              f"Séances du {premier_lundi()} au {DATE_FIN}. Données synthétiques, athlètes fictifs.",
              "Charge = effort perçu (0 à 10) × durée en minutes, en unités arbitraires (UA).",
              "", "## Contrôles qualité", "",
              "| Dimension | Règle | Résultat | Traitement |", "| --- | --- | --- | --- |"]
    for c in controles:
        resultat = "conforme" if c.ok else f"{len(c.anomalies)} anomalie(s)"
        traitement = "rien à traiter" if c.ok else c.traitement
        lignes.append(f"| {c.dimension} | {c.regle} | {resultat} | {traitement} |")
    lignes += ["", "## Anomalies détectées", ""]
    lignes += [f"- {c.dimension} : {a}" for c in controles for a in c.anomalies]
    lignes += ["", "## Charge par athlète et par semaine", "",
               "| Athlète | Semaine du | Séances | Minutes | Charge (UA) |",
               "| --- | --- | --- | --- | --- |"]
    for athlete, semaine, nb, minutes, charge in connexion.execute("SELECT * FROM charge_hebdo"):
        lignes.append(f"| {athlete} | {semaine} | {nb} | {minutes:.0f} | {charge:.0f} |")
    chemin.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return chemin


def executer(dossier=DOSSIER):
    """Enchaîne les quatre étapes et renvoie le chemin du rapport."""
    chemin_csv = ecrire_csv(generer_seances(), dossier / "data" / "seances.csv")
    base = dossier / "sortie" / "charge.sqlite"  # à ouvrir pour explorer les tables
    base.parent.mkdir(parents=True, exist_ok=True)
    base.unlink(missing_ok=True)
    with closing(sqlite3.connect(base)) as connexion:
        charger(chemin_csv, connexion)
        controles = controler(connexion, DATE_FIN)
        transformer(connexion)
        return ecrire_rapport(controles, connexion, dossier / "sortie" / "rapport.md")


if __name__ == "__main__":
    rapport = executer()
    print(f"Rapport écrit : {rapport}")
