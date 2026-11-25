"""Contrôles qualité des séances brutes : un par dimension, chacun dit comment il est traité."""
from dataclasses import dataclass
from datetime import timedelta

from generer import NB_SEMAINES, premier_lundi
from pipeline import SEUIL_HEURES


@dataclass
class Controle:
    dimension: str
    regle: str
    traitement: str
    anomalies: list

    @property
    def ok(self):
        return not self.anomalies


def lister(connexion, requete, *parametres):
    return [" ".join(str(v) for v in ligne) for ligne in connexion.execute(requete, parametres)]


def exactitude(connexion, date_fin):
    anomalies = lister(connexion, "SELECT athlete, date, 'effort', rpe FROM seances_brutes "
                                  "WHERE rpe NOT BETWEEN 0 AND 10")
    return Controle("exactitude", "effort perçu entre 0 et 10",
                    "exclu : on ne peut pas deviner la vraie valeur", anomalies)


def coherence(connexion, date_fin):
    anomalies = lister(connexion, "SELECT athlete, date, 'durée', duree FROM seances_brutes "
                                  "WHERE duree < ?", SEUIL_HEURES)
    return Controle("cohérence", f"toutes les durées en minutes (≥ {SEUIL_HEURES})",
                    "corrigé : durée × 60", anomalies)


def completude(connexion, date_fin):
    attendues = {(premier_lundi(date_fin) + timedelta(weeks=s)).isoformat()
                 for s in range(NB_SEMAINES)}
    presentes = connexion.execute("SELECT DISTINCT athlete, date(date, 'weekday 0', '-6 days') "
                                  "FROM seances_brutes").fetchall()
    anomalies = [f"{athlete} aucune séance la semaine du {semaine}"
                 for athlete in sorted({a for a, _ in presentes})
                 for semaine in sorted(attendues - {s for a, s in presentes if a == athlete})]
    return Controle("complétude", f"{NB_SEMAINES} semaines par athlète",
                    "signalé : semaine absente du tableau, rien n'est inventé", anomalies)


def fraicheur(connexion, date_fin):
    derniere = connexion.execute("SELECT MAX(date) FROM seances_brutes").fetchone()[0]
    limite = (date_fin - timedelta(days=7)).isoformat()
    anomalies = [] if derniere and derniere > limite else [f"dernière séance le {derniere}"]
    return Controle("fraîcheur", f"une séance dans les 7 jours avant le {date_fin}",
                    "signalé : rapport à ne pas utiliser tel quel", anomalies)


def unicite(connexion, date_fin):
    anomalies = lister(connexion, "SELECT athlete, date, COUNT(*) || ' fois' FROM seances_brutes "
                                  "GROUP BY athlete, date HAVING COUNT(*) > 1")
    return Controle("unicité", "une séance par athlète et par jour",
                    "exclu : un seul exemplaire gardé", anomalies)


def controler(connexion, date_fin):
    """Lance les cinq contrôles sur la table seances_brutes."""
    return [controle(connexion, date_fin)
            for controle in (exactitude, completude, fraicheur, coherence, unicite)]
