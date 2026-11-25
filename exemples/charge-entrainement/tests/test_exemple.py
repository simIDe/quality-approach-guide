"""Tests de l'exemple : génération, transformation, contrôles et rapport."""
import sqlite3

import pytest

from controles import controler
from generer import DATE_FIN, ecrire_csv, generer_seances, seances_propres
from lancer import executer
from pipeline import charger, transformer


@pytest.fixture
def connexion():
    cx = sqlite3.connect(":memory:")
    yield cx
    cx.close()


def charger_lignes(lignes, connexion, tmp_path):
    charger(ecrire_csv(lignes, tmp_path / "seances.csv"), connexion)


def test_generation_reproductible():
    assert generer_seances() == generer_seances()


def test_les_quatre_defauts_sont_detectes(connexion, tmp_path):
    charger_lignes(generer_seances(), connexion, tmp_path)
    resultats = {c.dimension: c for c in controler(connexion, DATE_FIN)}
    echecs = {dimension for dimension, c in resultats.items() if not c.ok}
    assert echecs == {"exactitude", "cohérence", "complétude", "unicité"}
    assert len(resultats["cohérence"].anomalies) == 3  # durées en heures
    assert len(resultats["exactitude"].anomalies) == 1  # effort perçu hors échelle
    assert len(resultats["unicité"].anomalies) == 1  # séance en double
    assert "A03" in resultats["complétude"].anomalies[0]  # semaine manquante
    assert resultats["fraîcheur"].ok


def test_donnees_propres_sans_anomalie(connexion, tmp_path):
    charger_lignes(seances_propres(), connexion, tmp_path)
    assert all(c.ok for c in controler(connexion, DATE_FIN))


def test_transformation_corrige_exclut_et_calcule_la_charge(connexion, tmp_path):
    lignes = [
        {"athlete": "A01", "date": "2026-11-16", "duree": 60, "rpe": 5},
        {"athlete": "A01", "date": "2026-11-16", "duree": 60, "rpe": 5},  # doublon
        {"athlete": "A01", "date": "2026-11-18", "duree": 0.5, "rpe": 4},  # en heures
        {"athlete": "A01", "date": "2026-11-20", "duree": 40, "rpe": 12},  # hors échelle
        {"athlete": "A01", "date": "2026-11-22", "duree": 30, "rpe": 2},  # dimanche
    ]
    charger_lignes(lignes, connexion, tmp_path)
    transformer(connexion)
    semaines = connexion.execute("SELECT * FROM charge_hebdo").fetchall()
    # 5×60 + 4×30 + 2×30 = 480 ; le dimanche appartient à la semaine du lundi 16.
    assert semaines == [("A01", "2026-11-16", 3, 120.0, 480.0)]


def test_le_rapport_dit_comment_chaque_defaut_est_traite(tmp_path):
    texte = executer(tmp_path).read_text(encoding="utf-8")
    assert all(mot in texte for mot in ["corrigé", "exclu", "signalé"])
    assert "| A01 | 2026-09-28 |" in texte
