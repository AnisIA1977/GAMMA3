# Script de démarrage pour GAMMA3.0 sur Windows 11

Write-Host "Initialisation de GAMMA3.0..." -ForegroundColor Cyan

# 1. Vérification de Python
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Error "Python n'est pas trouvé. Veuillez installer Python depuis python.org et cocher 'Add to PATH'."
    exit 1
}

# 2. Création de l'environnement virtuel si nécessaire
if (-not (Test-Path "venv")) {
    Write-Host "Création de l'environnement virtuel..."
    python -m venv venv
}

# 3. Activation de l'environnement
Write-Host "Activation de l'environnement..."
.\venv\Scripts\Activate.ps1

# 4. Installation des dépendances
Write-Host "Installation des dépendances..."
pip install -r requirements.txt

# 5. Lancement du serveur
Write-Host "Lancement du serveur..." -ForegroundColor Green
Write-Host "Ouvrez votre navigateur sur http://127.0.0.1:8000" -ForegroundColor Yellow
uvicorn gamma3_system.main:app --reload
