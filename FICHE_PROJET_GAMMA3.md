# 📋 FICHE PROJET — GAMMA 3

> Document de cadrage à compléter avant le démarrage du développement.
> Toute information manquante doit être marquée `[À DÉFINIR]` ou `[INCONNU]`.

---

## 🎯 1. IDENTIFICATION DU PROJET

| Champ | Valeur |
|---|---|
| **Nom du projet** | Gamma 3 |
| **Nature** | Modernisation / Refonte de Gamma 2 |
| **Date de cadrage** | `[À REMPLIR]` |
| **Sponsor / Décideur** | `[À REMPLIR]` |
| **Chef de projet** | `[À REMPLIR]` |
| **Tech Lead** | `[À REMPLIR]` |
| **Date de démarrage souhaitée** | `[À REMPLIR]` |
| **Date de mise en production cible** | `[À REMPLIR]` |

---

## 🏛️ 2. CONTEXTE LEGACY (Gamma 2)

### 2.1 Application existante

| Champ | Valeur |
|---|---|
| **Année de mise en production de Gamma 2** | `[À REMPLIR]` |
| **Technologie frontend** | Silverlight |
| **Version .NET / Silverlight** | `[À REMPLIR]` |
| **Technologie backend** | `[À REMPLIR — WCF ? ASP.NET ?]` |
| **SGBD** | Microsoft SQL Server |
| **Version SQL Server** | `[À REMPLIR — ex: 2012, 2016, 2019]` |
| **Hébergement actuel** | `[À REMPLIR — on-premise / cloud / hybride]` |
| **Nombre d'utilisateurs actifs** | `[À REMPLIR]` |
| **Pic d'utilisateurs simultanés** | `[À REMPLIR]` |
| **Disponibilité de la documentation Gamma 2** | `[Oui/Non/Partielle]` |

### 2.2 Volumétrie de la base de données ⚠️ CRITIQUE

| Champ | Valeur |
|---|---|
| **Backup BDD disponible ?** | ✅ Oui (confirmé) |
| **Format de la backup** | `[À REMPLIR — .bak / .bacpac / dump SQL]` |
| **Taille totale de la BDD (Go)** | `[À REMPLIR]` |
| **Nombre approximatif de tables** | `[À REMPLIR]` |
| **Nombre approximatif de procédures stockées** | `[À REMPLIR]` |
| **Nombre approximatif de vues** | `[À REMPLIR]` |
| **Présence de triggers ?** | `[Oui/Non — si oui, combien]` |
| **Présence de jobs SQL Agent ?** | `[Oui/Non]` |
| **Données binaires (BLOB/images)** | `[Oui/Non — taille estimée]` |
| **Année de la donnée la plus ancienne** | `[À REMPLIR]` |
| **Données sensibles RGPD (à chiffrer)** | `[À LISTER]` |

### 2.3 Modules fonctionnels existants

> Lister les modules de Gamma 2 à reprendre (cocher ce qui s'applique)

- [ ] Gestion des produits / articles
- [ ] Gestion des catégories
- [ ] Gestion des stocks (entrées/sorties)
- [ ] Gestion des fournisseurs
- [ ] Gestion des clients
- [ ] Gestion des commandes / bons de commande
- [ ] Gestion des livraisons / bons de livraison
- [ ] Gestion des inventaires
- [ ] Gestion multi-sites / multi-entrepôts
- [ ] Gestion des utilisateurs et droits
- [ ] Reporting / tableaux de bord
- [ ] Exports (Excel, PDF, CSV)
- [ ] Codes-barres / QR codes
- [ ] Notifications (mail, in-app)
- [ ] Audit / traçabilité
- [ ] Autres : `[À LISTER]`

### 2.4 Lacunes connues / Points d'amélioration souhaités

> Lister les bugs récurrents, frustrations utilisateurs, fonctionnalités manquantes

1. `[À REMPLIR]`
2. `[À REMPLIR]`
3. `[À REMPLIR]`

### 2.5 Intégrations externes existantes

| Système intégré | Type d'intégration | À conserver ? |
|---|---|---|
| `[Ex: ERP, Comptabilité]` | `[API/Fichier/BDD]` | `[Oui/Non]` |
| | | |

---

## 🚀 3. PROJET CIBLE (Gamma 3)

### 3.1 Vision et objectifs

**Vision en 1 phrase :**
`[À REMPLIR — ex: "Une plateforme de gestion de stock moderne, collaborative et sécurisée, accessible partout."]`

**Top 3 objectifs business :**
1. `[À REMPLIR]`
2. `[À REMPLIR]`
3. `[À REMPLIR]`

**Top 3 objectifs techniques :**
1. `[À REMPLIR — ex: Sortir de la dette Silverlight]`
2. `[À REMPLIR — ex: Améliorer la performance]`
3. `[À REMPLIR — ex: Permettre le mobile]`

### 3.2 Utilisateurs cibles

| Type d'utilisateur | Nombre estimé | Usage principal |
|---|---|---|
| Administrateurs | `[X]` | `[À REMPLIR]` |
| Gestionnaires de stock | `[X]` | `[À REMPLIR]` |
| Opérateurs entrepôt | `[X]` | `[À REMPLIR]` |
| Comptables | `[X]` | `[À REMPLIR]` |
| `[Autres]` | `[X]` | `[À REMPLIR]` |
| **TOTAL utilisateurs** | `[X]` | |

### 3.3 Contraintes techniques

| Contrainte | Valeur |
|---|---|
| **Stack imposée frontend** | Angular 17+ |
| **Stack imposée backend** | Spring Boot 3.x / Java 21 |
| **SGBD cible** | `[À ARBITRER : PostgreSQL / SQL Server / autre]` |
| **Hébergement cible** | `[À REMPLIR : Cloud (AWS/Azure/GCP) / On-premise / Hybride]` |
| **Conteneurisation requise ?** | `[Oui/Non]` |
| **Kubernetes requis ?** | `[Oui/Non]` |
| **Navigateurs supportés** | `[À REMPLIR — ex: Chrome, Edge, Firefox dernières versions]` |
| **Support mobile (responsive) ?** | `[Oui/Non — natif ou PWA ?]` |
| **Support hors-ligne ?** | `[Oui/Non]` |
| **Multi-langues ?** | `[Oui/Non — quelles langues ?]` |
| **Multi-tenant ?** | `[Oui/Non]` |

### 3.4 Exigences non-fonctionnelles

| Exigence | Cible |
|---|---|
| **Temps de réponse API (médian)** | `[À DÉFINIR — ex: < 200ms]` |
| **Temps de chargement pages** | `[À DÉFINIR — ex: < 2s]` |
| **Disponibilité (SLA)** | `[À DÉFINIR — ex: 99.5%]` |
| **RPO (Recovery Point Objective)** | `[À DÉFINIR — ex: 1h]` |
| **RTO (Recovery Time Objective)** | `[À DÉFINIR — ex: 4h]` |
| **Conformité RGPD** | `[Oui/Non]` |
| **Autres conformités** | `[À LISTER — ISO 27001, etc.]` |
| **Audit trail requis ?** | `[Oui/Non — sur quelles entités ?]` |
| **2FA obligatoire ?** | `[Oui/Non — pour qui ?]` |

### 3.5 Sécurité

| Champ | Valeur |
|---|---|
| **Type d'authentification** | `[À DÉFINIR : JWT local / SSO / OAuth2 / LDAP]` |
| **SSO existant à intégrer ?** | `[Oui/Non — quel fournisseur ?]` |
| **Politique de mots de passe** | `[À DÉFINIR]` |
| **Données chiffrées au repos ?** | `[Oui/Non]` |
| **Données chiffrées en transit ?** | HTTPS obligatoire |
| **Niveau de risque sécurité** | `[Faible / Moyen / Élevé]` |

---

## 🔴 4. STRATÉGIE DE MIGRATION

### 4.1 Approche de bascule

| Champ | Valeur |
|---|---|
| **Approche envisagée** | `[À ARBITRER : Big Bang / Strangler / Dual-Run]` |
| **Coexistence Gamma 2 + Gamma 3 possible ?** | `[Oui/Non]` |
| **Durée de coexistence acceptable** | `[À DÉFINIR — ex: 3 mois]` |
| **Bascule par module ou globale ?** | `[À DÉFINIR]` |
| **Période de gel des données legacy** | `[À DÉFINIR]` |

### 4.2 Tolérance à la perte de données

| Champ | Valeur |
|---|---|
| **Tolérance à la perte** | **0% (strict)** |
| **Données critiques absolues** | `[À LISTER : transactions financières, mouvements de stock, etc.]` |
| **Données pouvant être archivées** | `[À LISTER : logs anciens, etc.]` |
| **Données à anonymiser** | `[À LISTER]` |
| **Données à supprimer (RGPD)** | `[À LISTER]` |

### 4.3 Validation post-migration

> Comment garantir que la migration a réussi ?

- [ ] Comparaison des counts par table
- [ ] Checksums sur données critiques
- [ ] Échantillonnage manuel
- [ ] Tests de réconciliation comptable
- [ ] Validation par utilisateurs métier
- [ ] Autres : `[À DÉFINIR]`

---

## 👥 5. ÉQUIPE PROJET

| Rôle | Nombre | Compétences | Disponibilité |
|---|---|---|---|
| Tech Lead | `[X]` | `[À REMPLIR]` | `[X]%` |
| Dev backend Java/Spring | `[X]` | `[Junior/Confirmé/Senior]` | `[X]%` |
| Dev frontend Angular | `[X]` | `[Junior/Confirmé/Senior]` | `[X]%` |
| DBA / Expert SQL | `[X]` | `[À REMPLIR]` | `[X]%` |
| DevOps | `[X]` | `[À REMPLIR]` | `[X]%` |
| QA / Testeur | `[X]` | `[À REMPLIR]` | `[X]%` |
| UX/UI Designer | `[X]` | `[À REMPLIR]` | `[X]%` |
| Product Owner | `[X]` | `[À REMPLIR]` | `[X]%` |

---

## 📅 6. PLANNING & BUDGET

| Champ | Valeur |
|---|---|
| **Méthodologie** | `[À DÉFINIR : Scrum / Kanban / SAFe]` |
| **Durée du sprint** | `[À DÉFINIR : 1 / 2 / 3 semaines]` |
| **Date de démarrage** | `[À REMPLIR]` |
| **Date MVP cible** | `[À REMPLIR]` |
| **Date go-live cible** | `[À REMPLIR]` |
| **Budget global (optionnel)** | `[À REMPLIR]` |
| **Phase pilote prévue ?** | `[Oui/Non — combien d'utilisateurs ?]` |

---

## 🛠️ 7. INFRASTRUCTURE & OUTILLAGE

### 7.1 Environnements

| Environnement | Disponible ? | Hébergement |
|---|---|---|
| Développement | `[Oui/Non]` | `[À REMPLIR]` |
| Test / Recette | `[Oui/Non]` | `[À REMPLIR]` |
| Pré-production | `[Oui/Non]` | `[À REMPLIR]` |
| Production | `[Oui/Non]` | `[À REMPLIR]` |

### 7.2 Outils

| Catégorie | Outil utilisé / souhaité |
|---|---|
| **Gestion de code source** | `[Git — GitHub / GitLab / Bitbucket / Azure DevOps]` |
| **Gestion de projet / tickets** | `[Jira / Trello / Azure Boards / autre]` |
| **CI/CD** | `[À DÉFINIR]` |
| **Container registry** | `[À DÉFINIR]` |
| **Monitoring** | `[À DÉFINIR]` |
| **Logs centralisés** | `[À DÉFINIR]` |
| **Communication équipe** | `[Slack / Teams / autre]` |
| **Documentation** | `[Confluence / Notion / Wiki Git / autre]` |

---

## ⚠️ 8. RISQUES IDENTIFIÉS

| # | Risque | Probabilité | Impact | Mitigation envisagée |
|---|---|---|---|---|
| 1 | Perte de données pendant la migration | Faible | **Critique** | Stratégie ETL validée + plan de rollback |
| 2 | `[À COMPLÉTER]` | | | |
| 3 | `[À COMPLÉTER]` | | | |
| 4 | `[À COMPLÉTER]` | | | |
| 5 | `[À COMPLÉTER]` | | | |

---

## 📌 9. POINTS BLOQUANTS / À CLARIFIER

> Liste des questions à résoudre AVANT de démarrer le sprint 1

1. `[À COMPLÉTER]`
2. `[À COMPLÉTER]`
3. `[À COMPLÉTER]`

---

## 📎 10. DOCUMENTS COMPLÉMENTAIRES À FOURNIR

- [ ] Cahier des charges fonctionnel — ✅ Fourni
- [ ] Cahier des charges technique — ✅ Fourni
- [ ] Backup BDD Gamma 2 (anonymisée si possible) — `[À FOURNIR]`
- [ ] Schéma de la BDD (DDL ou diagramme) — `[À FOURNIR]`
- [ ] Captures d'écran des interfaces Gamma 2 critiques — `[À FOURNIR]`
- [ ] Documentation utilisateur Gamma 2 (si existante) — `[À FOURNIR]`
- [ ] Liste des bugs / tickets connus de Gamma 2 — `[À FOURNIR]`
- [ ] Mockups / maquettes Gamma 3 (si existantes) — `[À FOURNIR]`
- [ ] Charte graphique / branding — `[À FOURNIR]`

---

## ✅ 11. VALIDATION

| Rôle | Nom | Date | Signature |
|---|---|---|---|
| Sponsor | | | |
| Chef de projet | | | |
| Tech Lead | | | |

---

> 💡 **Conseil** : ne bloque pas le démarrage en attendant que TOUS les champs soient remplis.
> Identifie les **3-5 informations critiques** (volumétrie BDD, équipe, dates clés, hébergement)
> et démarre l'analyse avec Claude. Les autres infos peuvent venir au fil de l'eau.
