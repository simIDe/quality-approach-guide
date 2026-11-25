# Journal de méthode (extrait)

Un extrait, pour montrer la forme. Le journal d'un groupe est plus long et écrit au fil de l'eau, pas à la fin.

| Date | Décision ou événement | Pourquoi | Qui |
| --- | --- | --- | --- |
| 2026-11-09 | Sujet : la charge d'entraînement hebdomadaire pour l'entraîneur d'un club de course à pied | C'est l'exemple vu en cours ; un utilisateur et une décision faciles à nommer | enseignant |
| 2026-11-09 | Données synthétiques générées par script, athlètes fictifs | Des vraies séances seraient des données personnelles, et même des données de santé | enseignant |
| 2026-11-10 | Quatre défauts fixés à l'avance : durées en heures, semaine manquante, doublon, effort hors échelle | Un défaut par grande famille de problème, pour que chaque contrôle ait quelque chose à trouver | enseignant |
| 2026-11-10 | SQLite et bibliothèque standard de Python, pytest pour les tests | Rien à installer à part uv ; le code doit se lire en vingt minutes | enseignant |
| 2026-11-25 | Tests écrits avant le code, dont un qui exige la détection des quatre défauts | Le test fixe ce qu'on attend avant que le code existe ; impossible de « réussir » sans détecter | agent de code, relu par l'enseignant |
| 2026-11-25 | Date de fin des données fixée au 22 novembre 2026 au lieu de la date du jour | Le même fichier et le même rapport à chaque lancement, donc des tests stables | agent de code, relu par l'enseignant |
| 2026-11-25 | Semaine manquante signalée, pas remplie par une charge nulle | Une semaine sans enregistrement n'est pas forcément une semaine de repos ; inventer un zéro tromperait l'entraîneur | enseignant |
| 2026-11-25 | Une durée sous 10 « minutes » est considérée comme saisie en heures | Une séance de moins de dix minutes est invraisemblable pour ce club ; la règle reste une hypothèse, est écrite dans la fiche produit comme limite | enseignant |
| 2026-11-25 | CI sur Linux, Windows et macOS | Vérifier que la commande unique marche sur les trois systèmes des étudiants | agent de code |

## Usage de l'IA

- **Ce qui a été demandé :** à un agent de code, d'écrire l'exemple à partir de la spécification du dépôt : tests d'abord, une seule commande, moins de 300 lignes de Python, noms en français.
- **Ce qui a été gardé :** le découpage en quatre fichiers (générer, charger et transformer, contrôler, lancer), le SQL de la table hebdomadaire, les tests.
- **Ce qui a été rejeté ou corrigé, et pourquoi :**
  - la première version dépassait 300 lignes (313) : elle a été resserrée, sans retirer de contrôle ni de test ;
  - la première version gardait la base SQLite en mémoire : elle est maintenant écrite dans `sortie/charge.sqlite`, pour qu'un étudiant puisse ouvrir les tables et refaire les requêtes.
- **Ce qui n'a jamais été envoyé à l'agent :** aucune donnée réelle, aucun secret. Il n'y en a pas dans ce projet.

## Ce qu'on referait autrement

- Repérer les doublons sur la clé (athlète, date) dans le nettoyage aussi, et pas seulement les lignes strictement identiques : deux saisies différentes du même jour passeraient aujourd'hui le nettoyage, même si le contrôle d'unicité les signale.
- Montrer la semaine manquante comme une ligne vide du tableau plutôt que par son absence, pour que l'entraîneur la voie sans lire la section des anomalies.
- Demander à la source de saisir la durée dans une seule unité, plutôt que de corriger après coup avec un seuil.
