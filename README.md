# GAMMA3.0 - Système de Gestion du Matériel Naval

## 📘 Vue d'ensemble
Le système GAMMA3.0 est conçu pour automatiser la gestion du matériel technique de la Marine Nationale Tunisienne. Il implémente les règles de gestion strictes définies dans le cahier des charges "GAMMA3.0", notamment la codification hiérarchique des articles.

### Structure de Codification
Un article est identifié par une nomenclature unique de 11 caractères générée automatiquement :
`100MT010001`
- **1** : Classe (ex: Mécanique)
- **00** : Sous-Classe (ex: Moteurs Diesels)
- **MT** : Constructeur (ex: MTU)
- **01** : Série (ex: 20 V 538)
- **0001** : Code Item (ex: Joint)

## 🛠 Architecture Technique
Ce projet utilise une architecture moderne et portable :
- **Backend** : Python 3.12 + FastAPI (Performance et Documentation API auto-générée).
- **Base de Données** : SQLite (Stockage local fichier unique, idéal pour le déploiement autonome).
- **ORM** : SQLAlchemy (Abstraction de la base de données).
- **Frontend** : Vue.js 3 (Interface réactive, sans étape de build complexe).

## 🚀 Guide de Déploiement (Windows 11)

### Pré-requis
1.  Installer **Python 3.10+** (Cochez "Add Python to PATH" à l'installation).
2.  Avoir **PowerShell** ou un terminal standard.

### Installation
1.  Téléchargez le dossier du projet.
2.  Ouvrez un terminal dans le dossier.
3.  Exécutez le script d'installation et lancement :
    ```powershell
    ./start.ps1
    ```

### Lancement Manuel
Si vous ne souhaitez pas utiliser le script :
1.  Créez un environnement virtuel :
    ```bash
    python -m venv venv
    ```
2.  Activez-le :
    ```bash
    .\venv\Scripts\activate
    ```
3.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
4.  Lancez le serveur :
    ```bash
    uvicorn gamma3_system.main:app --reload
    ```
5.  Ouvrez votre navigateur sur : `http://127.0.0.1:8000`

## 🧪 Tests
Pour vérifier que tout fonctionne et que les règles métier sont respectées :
```bash
pytest tests/
```

## 📂 Structure du Projet
- `gamma3_system/` : Code source.
    - `models.py` : Définition des tables (Classe, Article...).
    - `crud.py` : Logique métier (Création, Lecture...).
    - `main.py` : Point d'entrée de l'API.
    - `static/` : Interface utilisateur (HTML/JS).
- `tests/` : Tests automatisés.
- `requirements.txt` : Liste des librairies nécessaires.
