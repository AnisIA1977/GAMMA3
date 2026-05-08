# 📘 GAMMA 3 — Journal de bord du projet

> **Version** : 1.0
> **Date de création** : 03 mai 2026
> **Dernière mise à jour** : 03 mai 2026 — Session 1 (Démarrage)
> **Statut** : Phase 0 — Analyse préalable
> **Objectif de ce document** : permettre la reprise exacte de la collaboration entre Claude et l'utilisateur en cas de perte de la conversation. À uploader au début de chaque nouvelle session.

---

## 🎯 1. CONTEXTE DU PROJET

### 1.1 Identité du projet

**GAMMA 3.0** = refonte complète d'un système de gestion automatisée du matériel technique de la **Marine tunisienne**.

- **Maître d'ouvrage (MOA)** : Division Approvisionnement (DA) — Base Navale Principale de Bizerte
- **Maître d'œuvre (MOE)** : DITAM
- **Document de référence** : Cahier des charges techniques v1.0 du 12/08/2025
- **Auteurs CCT** : CF Mnasri, CF Rouissi, LV Nouri, LV Elhammi, LV Fersi
- **Diffusion** : Limitée (نشرة محدودة)

### 1.2 Existant — GAMMA 2

- Stack legacy : **Microsoft Silverlight + Microsoft SQL Server**
- Une **backup de la BDD** existe et sera fournie pour la migration
- Doit être complètement remplacé

### 1.3 Cible — GAMMA 3

Stack imposée par le CCT :

| Couche | Techno imposée |
|---|---|
| Frontend | Angular |
| API Gateway | Spring Cloud Gateway |
| Backend | Microservices Spring Boot |
| Auth | Serveur dédié + JWT |
| Messaging | Apache Kafka + WebSocket |
| Reporting | JasperReports |
| BDD relationnelle | PostgreSQL |
| BDD NoSQL | MongoDB (notifications) |
| Conteneurisation | Docker |

### 1.4 Stack imposée par l'utilisateur (en complément)

- **Java 21 LTS** + Spring Boot 3.2+
- Spring (Web, Data JPA, Security, Validation, WebSocket, Actuator, Batch)
- Hibernate + JPA, MapStruct, SpringDoc OpenAPI
- Tests : JUnit 5, Mockito, Testcontainers, RestAssured
- Build : Maven (par défaut, à confirmer)
- Angular 17+ (standalone, signals, new control flow), TypeScript strict
- UI : Angular Material **OU** PrimeNG (à arbitrer) + TailwindCSS
- Tests front : Jasmine/Karma + Cypress
- Cache : Redis | Migrations : Flyway

### 1.5 Caractéristiques cibles

- Performance : < 200ms sur APIs critiques
- Sécurité : OWASP Top 10, RGPD, JWT + 2FA, audit trail
- Collaboration multi-utilisateurs temps réel (WebSocket/STOMP)
- UX moderne : responsive, PWA, WCAG 2.1 AA
- Maintenabilité : code lisible, testé, documenté

### 1.6 Enjeu critique

🔴 **Migration de la BDD avec 0% de perte tolérée**.

Stratégies à considérer : Big Bang, Strangler Fig, Dual-Write, CDC, Spring Batch ETL.

### 1.7 Planning macro imposé par le CCT

| Phase | Durée | Mois |
|---|---|---|
| 1. Préparation et analyse | 8 sem | 2 mois |
| 2. Migration BDD | 32 sem | 8 mois |
| 3. Développement (Charte + Front + Back) | 76 sem | 19 mois |
| 4. Déploiement | 12 sem | 3 mois |
| 5. Formation | 8 sem | 2 mois |
| 6. Tests et maintenance | 12 sem | 3 mois |
| **TOTAL** | | **~29-37 mois** |

---

## 🎓 2. MODE DE COLLABORATION CONVENU

### 2.1 Posture de Claude

- À la fois **Tech Lead Senior**, **Mentor/Enseignant**, et **Collègue de pair-programming**
- Pas un simple générateur de code, mais un **partenaire intellectuel**

### 2.2 Style pédagogique obligatoire (xAI)

Pour chaque réponse importante :
1. **Expliquer le POURQUOI avant le COMMENT** (intention, alternatives, trade-offs, conséquences)
2. **Documenter le COMMENT** (JavaDoc/JSDoc en anglais, commentaires inline, bloc d'explication en français)
3. **Contextualiser** (rapport au projet, aux principes SOLID/patterns)
4. **Anticiper les questions** (proposer 2-4 questions de réflexion à la fin)
5. **Encourager le dialogue** (poser des questions, proposer des alternatives à débattre)

### 2.3 Langues

- **Français** : documentation, explications, dialogues
- **Anglais** : code, JavaDoc, commits, commentaires de code

### 2.4 Format de réponse type

- Pour une décision d'architecture : Contexte → Options → Comparaison → Recommandation → Conséquences → Validation
- Pour du code : Objectif → Concepts → Approche → Code commenté → Tests → Pièges → Intégration → Questions
- Pour un concept : Problème → Théorie → Application au projet → Exemple → Erreurs courantes → Vérification

---

## 📋 3. PLAN DE LIVRABLES — PHASE D'ANALYSE

| # | Livrable | Statut | Sessions estimées |
|---|---|---|---|
| 1 | Synthèse exécutive | ⏳ À démarrer | 1 |
| 2 | Analyse du legacy Gamma 2 | 📅 À venir | 1 |
| 3 | 🔴 Stratégie de migration des données (CRITIQUE) | 📅 À venir | 2-3 |
| 4 | Analyse du cahier des charges | 📅 À venir | 1-2 |
| 5 | Architecture cible Gamma 3 | 📅 À venir | 2 |
| 6 | Modèle de données + mapping legacy | 📅 À venir | 2 |
| 7 | Roadmap & MVP | 📅 À venir | 1 |
| 8 | Structure des projets | 📅 À venir | 1 |
| 9 | Prochaines étapes immédiates | 📅 À venir | 1 |

**Total estimé** : ~12-14 sessions sur ~4-6 semaines (cohérent avec les 8 semaines de Phase 1 du CCT).

---

## ⚖️ 4. DÉCISIONS À TRANCHER ENSEMBLE (en cours)

| # | Décision | Options | Statut |
|---|---|---|---|
| D-001 | BDD cible | PostgreSQL vs SQL Server | ⏳ À débattre (livrable 5) |
| D-002 | UI Angular | Angular Material vs PrimeNG | ⏳ À débattre (livrable 5) |
| D-003 | Build backend | Maven vs Gradle | ⏳ À débattre (livrable 8) |
| D-004 | Stratégie migration | Big Bang / Strangler Fig / Dual-Write / CDC | ⏳ À débattre (livrable 3) |
| D-005 | State management Angular | NgRx vs Signals natifs | ⏳ À débattre (livrable 5) |
| D-006 | Architecture | Microservices d'emblée vs Modular Monolith d'abord | ⏳ Claude challenge le CCT — à débattre (livrable 5) |

> 📌 **Convention** : chaque décision validée sera consignée comme un **ADR** (Architecture Decision Record).

---

## 🧠 5. COMPRÉHENSION MÉTIER À DATE

### 5.1 Acteurs identifiés

- **EMAM** (État-Major Armée de Mer) — niveau stratégique
- **BL** (Bureau Logistique), **BQAI** (Qualité/Audit/Inspection)
- **DA** (Division Approvisionnement) — cœur métier de Gamma — sous-services :
  - SGS (gestion stock), SEP (étude/prévision), SM (magasins)
  - DAT (achat/transit), SC (comptabilité), SRR (réforme/remise)
  - SSC (saisie/contrôle), SRE (réception)
- **Unités utilisatrices** : DMEN, DRC, DEN, DGM, EP, RPS, 51/52 RCM, CFISM, 21 DAS

### 5.2 Modules fonctionnels (CCT — Article 9)

**Front-office** :
- Recherche multicritère, Authentification, Espace client, Panier, Commande en ligne, Journalisation

**Back-office** :
- Gestion paramètres (items, articles, classes, unités, corps, utilisateurs, droits)
- Prévisions (PARAM — Plan Annuel de Réapprovisionnement)
- Commande et suivi (fiches de commande, nomenclatures)
- Réception (bon provisoire, PV, bon d'entrée)
- Stockage (mise à jour stock)
- Distribution (demandes, ordres et bons de mouvement)
- Réforme (matériel complet/non complet, plans d'armement)
- Comptabilité (registre d'inventaire)
- Mise à jour des plans (armement, configuration, allocation)
- Réapprovisionnement services régionaux DA
- Remise du matériel
- Statistiques

### 5.3 Modèle "Article" — extrêmement riche

Un article a 6 blocs de données :

1. **Données de base** (nomenclature, désignation, unité, conditionnement, ISO, échelon de maintenance)
2. **Données de classification** (classe, catégorie, statut Cr/NCr, série, code type)
3. **Données de planification** (stocks min/max/sécu/alerte, mode approv, code ABC, code admin, délais, blocage, code origine, CMA, état)
4. **Données de stockage** (durée conservation, code nature/danger ADR)
5. **Données comptables** (prix, consommabilité, quantité)
6. **Références constructeurs** (NSN, OEM, etc.)

**Nomenclature intelligente à 12 caractères** :
```
100 MT 01 0001
│   │  │  └─ Item (4 chiffres)
│   │  └──── Série / Sous-famille (2 chiffres)
│   └─────── Constructeur / Catégorie (2 lettres)
└─────────── Groupe = Classe(1) + Sous-classe(2)
```

Exemple : `100MT010001` = Joint (item 0001) du moteur 20V538 (série 01) MTU (MT) sous-classe Moteurs Diesels (00), classe Matériel Mécanique (1).

### 5.4 Tables de référence à reprendre

- **Unités de gestion** (EA, HD, AY, BK, BO, BR, BT, BX, DZ, FT, GL, IN, KT, LB, LI, MR, PR, RO, SH, TU)
- **Codes type matériel** (MC, EQ, BE, DT, PS, PR, PC, AC, OD, OS, MP, MS)
- **Codes de gestion** (Clf, Clu, Ciu, Cei, Csm, Clm)
- **Codes nature/danger** (Classes 1 à 9 ADR — matières dangereuses)
- **Codes soutien** (S10, S20, S30, S40, S50)
- **Position administrative** (An, Dc, Da, Sb, Va, Ps, Px)
- **Mode approvisionnement** (GRC, ADO, BDC, ADR, MAX, LCE)
- **Origine matériel** (AFn, AFe, FMs, DOc, CL1, CL2, CL3, CL4, PR1, AD1, AD2, AX1)

### 5.5 Workflow de création d'article (multi-acteurs)

```
Responsable produit / Service utilisateur
  ↓ (estimations consommation, données planification + base)
Service comptable
  ↓ (ajoute données comptables)
Gestionnaire des stocks
  ↓ (complète données stockage + classification, valide)
Saisie dans le logiciel
```

### 5.6 Spécificités sensibles

- 🔐 **Contexte militaire** : confidentialité, audit trail, gestion matières dangereuses (ADR)
- 🌐 **Bilingue français / arabe** (RTL à prévoir)
- 🔒 **JWT + 2FA + OWASP + RGPD** imposés
- 📋 Workflow potentiellement avec **circuit de signature électronique** (à confirmer)

---

## ❓ 6. QUESTIONS BLOQUANTES POSÉES (en attente de réponse)

### 🔴 CRITIQUE — Migration BDD

1. **Volumétrie Gamma 2** : nb tables, nb lignes des grosses tables, taille du backup en Go ?
2. **Version SQL Server** source ? (NB : l'utilisateur a mentionné MySQL — à clarifier, divergence avec le CCT qui parle de SQL Server)
3. **Qualité données legacy** : doublons, orphelins, incohérences connus ?
4. **Historique** : migrer tout ou tronquer à N années ?
5. **Procédures stockées / triggers / vues** dans Gamma 2 ?

### 🟠 IMPORTANT — Contexte opérationnel

6. **Taille de l'équipe de dev** ? Niveaux Spring Boot / Angular ?
7. **Bascule** : Big Bang ou cohabitation ?
8. **Disponibilité key users côté DA** ?
9. **Réseau** : intranet militaire isolé ou accès internet ?

### 🟡 UTILE

10. **Nb utilisateurs simultanés cibles** ?
11. **2FA** : SMS, TOTP, carte à puce militaire (PKI) ?
12. Volume rapports JasperReports à reprendre ?
13. Mobile : PWA réellement utilisée smartphone ou juste responsive desktop/tablette ?

### 🟢 Pour plus tard

14. Circuit de signature électronique avec hiérarchie militaire ?
15. Intégrations avec autres SI militaires (RH MDN, finance) ?

---

## 💬 7. DERNIERS ÉCHANGES (résumé)

### Session 1 — 03 mai 2026

**Action utilisateur** :
- Lancement du projet, fourniture des documents (page de garde, définitions, instructions création/modification fiche article, historique CCF, CCT v1.0 PDF)
- Demande à Claude de proposer hypothèses + questions + plan avant d'attaquer le livrable 1

**Action Claude** :
- A confirmé sa compréhension métier (système militaire de gestion stock, pas e-commerce)
- A posé 15 questions classées par criticité
- A proposé un plan en 9 livrables / ~14 sessions
- A signalé son intention de **challenger le choix microservices** dans le livrable 5 (préférence pour modular monolith d'abord)
- A introduit le concept d'**ADR** (Architecture Decision Records)

**Réponse utilisateur** :
- A validé l'approche et les hypothèses ("presque toutes correctes")
- Va récupérer une copie de la BDD Gamma 2 et la version "MySQL" (probablement un lapsus pour SQL Server — à clarifier)
- A demandé une solution de sauvegarde de conversation → ce document

**Prochaine étape** : Reprendre à la **prochaine session** avec :
1. Réponses aux questions bloquantes (au moins volumétrie BDD et type de SGBD source)
2. Démarrage du **Livrable #1 : Synthèse exécutive**

---

## 🔄 8. COMMENT REPRENDRE LA COLLABORATION

À chaque nouvelle session, l'utilisateur :

1. Upload ce fichier (`GAMMA3_Journal_de_bord.md`) dans la conversation
2. Dit à Claude : *« On reprend le projet GAMMA 3. Voici le journal de bord. On en était au [livrable X]. »*
3. Claude lit le journal, confirme le contexte, et reprend exactement où on s'est arrêté

À la fin de chaque session importante (livrable terminé, décision actée), demander à Claude :
> *« Mets à jour le journal de bord avec ce qu'on a fait dans cette session. »*

Claude regénérera alors une version à jour du document à télécharger.

---

## 📚 9. ANNEXES — DOCUMENTS DE RÉFÉRENCE

Documents fournis dans le projet (dossier `/mnt/project/`) :
- `1_page_de_garde.docx` — Page de garde officielle (bilingue FR/AR)
- `2_Définition__Abréviation.docx` — Glossaire des sigles militaires
- `4_INSTRUCTIONS_DE_CREATION_MODIFICATION_FT.docx` — Instructions I01, I02, I03 (modèle FSA, attributs, nomenclature)
- `5_HISTORIQUE.docx` — Historique des révisions du CCF
- `Cahier_des_chages_V3_GAMMA.pdf` — **Cahier des charges techniques** (document de référence n°1)
- `consomabilite_du_materiel.xlsx` — Tableau de consommabilité (à analyser)

---

*Fin du journal de bord — version 1.0 — 03 mai 2026*
