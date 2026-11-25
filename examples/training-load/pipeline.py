"""Charge le CSV dans SQLite, nettoie les séances et calcule la charge hebdomadaire."""
import csv

# Une durée sous 10 « minutes » n'est pas une séance : elle a été saisie en heures.
SEUIL_HEURES = 10

NETTOYAGE = f"""
DROP TABLE IF EXISTS seances;
CREATE TABLE seances AS
SELECT DISTINCT                          -- unicité : un doublon exact est exclu
    athlete,
    date,
    CASE WHEN duree < {SEUIL_HEURES} THEN duree * 60 ELSE duree END
        AS duree_min,                    -- cohérence : heures converties en minutes
    rpe
FROM seances_brutes
WHERE rpe BETWEEN 0 AND 10;              -- exactitude : effort hors échelle exclu
"""

HEBDOMADAIRE = """
DROP TABLE IF EXISTS charge_hebdo;
CREATE TABLE charge_hebdo AS
SELECT
    athlete,
    date(date, 'weekday 0', '-6 days') AS semaine,  -- lundi de la semaine
    COUNT(*) AS nb_seances,
    SUM(duree_min) AS minutes,
    SUM(rpe * duree_min) AS charge                  -- effort perçu × minutes
FROM seances
GROUP BY athlete, semaine
ORDER BY athlete, semaine;
"""


def charger(chemin_csv, connexion):
    """Copie le CSV tel quel dans la table seances_brutes."""
    with open(chemin_csv, newline="", encoding="utf-8") as fichier:
        lignes = [(l["athlete"], l["date"], float(l["duree"]), int(l["rpe"]))
                  for l in csv.DictReader(fichier)]
    connexion.executescript("""
        DROP TABLE IF EXISTS seances_brutes;
        CREATE TABLE seances_brutes (athlete TEXT, date TEXT, duree REAL, rpe INTEGER);
    """)
    connexion.executemany("INSERT INTO seances_brutes VALUES (?, ?, ?, ?)", lignes)
    connexion.commit()


def transformer(connexion):
    """Construit la table seances (nettoyée) puis la table charge_hebdo."""
    connexion.executescript(NETTOYAGE + HEBDOMADAIRE)
