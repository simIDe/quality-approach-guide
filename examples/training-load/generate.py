"""Génère un CSV synthétique de séances de course à pied, avec quatre défauts volontaires.

Athlètes fictifs (A01 à A06). Graine et date de fin fixes : même fichier à chaque lancement.
"""
import csv
import random
from datetime import date, timedelta

GRAINE = 2026
DATE_FIN = date(2026, 11, 22)  # un dimanche : dernier jour couvert par les données
NB_SEMAINES = 8
ATHLETES = [f"A{i:02d}" for i in range(1, 7)]
SEANCES_PAR_SEMAINE = 3
COLONNES = ["athlete", "date", "duree", "rpe"]


def premier_lundi(date_fin=DATE_FIN):
    return date_fin - timedelta(weeks=NB_SEMAINES, days=-1)


def seances_propres():
    """Les séances sans défaut : 3 par semaine et par athlète, durée en minutes."""
    alea = random.Random(GRAINE)
    lignes = []
    for athlete in ATHLETES:
        for semaine in range(NB_SEMAINES):
            lundi = premier_lundi() + timedelta(weeks=semaine)
            for jour in sorted(alea.sample(range(7), SEANCES_PAR_SEMAINE)):
                jour_iso = (lundi + timedelta(days=jour)).isoformat()
                # durée en minutes, effort perçu (RPE) sur l'échelle 0 à 10
                lignes.append({"athlete": athlete, "date": jour_iso,
                               "duree": alea.randint(30, 100), "rpe": alea.randint(3, 8)})
    return lignes


def ajouter_defauts(lignes):
    """Introduit les quatre défauts volontaires, sur des lignes toutes différentes."""
    alea = random.Random(GRAINE + 1)
    # 1. Semaine manquante : aucune séance de A03 pendant la 5e semaine.
    lundi = premier_lundi() + timedelta(weeks=4)
    semaine = {(lundi + timedelta(days=j)).isoformat() for j in range(7)}
    lignes = [l for l in lignes if not (l["athlete"] == "A03" and l["date"] in semaine)]
    heures1, heures2, heures3, hors_echelle, double = alea.sample(range(len(lignes)), 5)
    # 2. Trois durées saisies en heures au lieu de minutes.
    for i in (heures1, heures2, heures3):
        lignes[i]["duree"] = round(lignes[i]["duree"] / 60, 2)
    # 3. Un effort perçu hors de l'échelle 0 à 10.
    lignes[hors_echelle]["rpe"] = 14
    # 4. Une séance saisie deux fois.
    lignes.append(dict(lignes[double]))
    return sorted(lignes, key=lambda l: (l["date"], l["athlete"]))


def generer_seances():
    return ajouter_defauts(seances_propres())


def ecrire_csv(lignes, chemin):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.DictWriter(fichier, fieldnames=COLONNES)
        ecrivain.writeheader()
        ecrivain.writerows(lignes)
    return chemin
