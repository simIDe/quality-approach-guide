---
title: "07 · Données personnelles"
sidebar_position: 7
---

*Ai-je le droit d'utiliser ces données ?*

Cette fiche ne donne pas de conseil juridique : elle aide à se poser les questions et renvoie à la CNIL, l'autorité française de protection des données.

## Le problème

Votre club vous propose les exports de montres connectées de ses coureurs : fréquence cardiaque, positions GPS, blessures notées par le kiné. Le projet serait plus réaliste, mais ces données décrivent des personnes réelles, et leur santé.

## Le minimum utile

**Reconnaître une donnée personnelle.** C'est toute information qui se rapporte à une personne identifiée ou identifiable, directement (nom, photo) ou indirectement (numéro de licence, trace GPS qui part chaque matin du même domicile, combinaison âge + club + discipline) ([définition CNIL](https://www.cnil.fr/fr/definition/donnee-personnelle)).

**Reconnaître une donnée de santé.** Fréquence cardiaque, blessures, poids, sommeil ou cycle menstruel peuvent en être, selon l'usage qui en est fait. Ce sont des données sensibles, protégées plus strictement ([qu'est-ce qu'une donnée de santé, CNIL](https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante)).

**Six questions à se poser avant de les utiliser**, réponses à noter dans la fiche produit :

1. **Finalité** : à quoi serviront-elles, précisément ?
2. **Base légale** : sur quoi repose le droit de les traiter (par exemple le consentement des personnes) ?
3. **Minimisation** : de quelles colonnes a-t-on vraiment besoin pour la décision visée ?
4. **Accès** : qui peut les voir ? Le dépôt est-il public ? Un modèle d'IA les reçoit-il ?
5. **Durée** : combien de temps sont-elles gardées, qui les supprime ensuite ?
6. **Hébergement** : où sont-elles stockées, dans quel pays ?

**Pseudonymiser n'est pas anonymiser.** Remplacer « Léa Martin » par « A07 » est une pseudonymisation : avec la table de correspondance, ou en croisant date, club et performance, on retrouve la personne ; les données restent personnelles. L'anonymisation rend la réidentification impossible en pratique, et elle est difficile à garantir ([l'anonymisation, CNIL](https://www.cnil.fr/fr/technologies/lanonymisation-de-donnees-personnelles) ; [anonymisation et pseudonymisation en recherche, CNIL](https://www.cnil.fr/fr/recherche-scientifique-hors-sante-enjeux-et-avantages-de-lanonymisation-et-de-la-pseudonymisation)).

Souvent, le plus simple est de s'en passer : des données synthétiques ou ouvertes suffisent pour démontrer une méthode.

## Pour aller plus loin

- Le [guide RGPD du développeur](https://www.cnil.fr/fr/technologies/guide-rgpd-du-developpeur) (CNIL) : sécurité, minimisation, gestion du code source.
- Une vue d'ensemble : [RGPD, de quoi parle-t-on ?](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on) (CNIL).
- En cas de doute, le délégué à la protection des données (DPO) de la structure qui fournit les données.

## Comment savoir si c'est fait

- La fiche produit dit si le projet utilise des données personnelles et, si oui, répond aux six questions.
- Aucune donnée personnelle n'est dans le dépôt ni dans son historique, ni envoyée à un modèle d'IA.
- Le groupe sait expliquer pourquoi ses données sont pseudonymisées, anonymisées ou synthétiques.
