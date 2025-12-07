<!-- PROJECT SHIELDS -->
![Contributors](https://img.shields.io/github/contributors/userANNA123/deploy-ml-model?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/userANNA123/deploy-ml-model?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/userANNA123/deploy-ml-model?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/userANNA123/deploy-ml-model?style=for-the-badge)
![MIT License](https://img.shields.io/github/license/userANNA123/deploy-ml-model?style=for-the-badge)
![CI/CD](https://img.shields.io/github/actions/workflow/status/userANNA123/deploy-ml-model/ci-cd.yml?label=CI%2FCD&style=for-the-badge)

<br/>

<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/logo.png" alt="Logo" width="120">
</p>

<h2 align="center">Déploiement d’un Modèle de Machine Learning avec CI/CD & Hugging Face le développement d'API avec FastAPI, 

les tests unitaires avec Pytest, 

et la gestion des versions avec Git.  </h2>

<p align="center">
  Un pipeline complet pour tester, valider et déployer automatiquement un modèle de Machine Learning.  
  <br/>
  <a href="#"> Explorer la documentation</a> ·
  <a href="#"> Reporter un bug</a> ·
  <a href="#"> Demander une fonctionnalité</a>
</p>

---

 Description du Projet

Ce projet consiste à déployer un modèle de Machine Learning en production à l’aide de FastAPI.
Le modèle est un Random Forest qui prédit si une personne (employé / client) risque de quitter l’entreprise (churn / attrition) à partir de caractéristiques professionnelles.

Ce projet met en place :

 Une API REST avec FastAPI pour exposer le modèle

Un schéma d’entrée clairement défini avec Pydantic

 Un modèle Random Forest pré-entraîné et chargé depuis un fichier

 Une documentation interactive automatique de l’API (Swagger / OpenAPI)

Une base pour les tests unitaires et fonctionnels avec Pytest

Client : Futurisys
Contexte : Projet professionnel – Déploiement d’un modèle ML en production
Auteur : ANNA <Ton nom complet>

 Livrables

✅ Dépôt Git structuré (code, modèle, tests, documentation)

✅ API FastAPI fonctionnelle exposant un endpoint de prédiction

✅ Modèle Random Forest sérialisé (par ex. model/random_forest.pkl)

✅ Schémas Pydantic pour la validation des données d’entrée/sortie

✅ Documentation Swagger / OpenAPI (via FastAPI)

✅ README détaillé expliquant installation, utilisation et architecture

✅ (Optionnel) Tests Pytest pour vérifier le bon fonctionnement du modèle et de l’API

## Étapes du projet (selon OpenClassrooms)

### ✅ **Étape 1 — Mettre en place un système de gestion de version et collaboration**
- Création du repository GitHub  
- Structure du projet  
- Branches main / develop  
- Commits clairs & conventions  

### ✅ **Étape 2 — Configurer la CI/CD**
- Mise en place du workflow GitHub Actions  
- Installation des dépendances  
- Pipeline complet :  
  - Tests  
  - Build  
  - Déploiement automatique  
- Déploiement vers Hugging Face Spaces via API

### ✅ **Étape 3 — Développement de l’API**
- Implémentation de FastAPI / or Gradio  
- Endpoints pour les prédictions  
- Validation des données (Pydantic)

### ✅ **Étape 4 — Gestion des données via PostgreSQL**
- Importation du dataset  
- Création des tables  
- Requêtes SQL (si applicable)

### ✅ **Étape 5 — Développer des tests unitaires & fonctionnels**
- Tests Pytest  
- Test du modèle  
- Test de l’API  
- Test du pipeline

### ✅ **Étape 6 — Documentation du modèle**
- README complet  
- Documentation API  
- Choix techniques & architecture  
- Instructions d’installation et exécution

---

##  Architecture du projet
project/
│── app/
│   ├── main.py              # Point d'entrée FastAPI
│   ├── api.py               # Routes de l'API (si séparé)
│   ├── models.py            # Modèles SQLAlchemy (si BD utilisée)
│   ├── schemas.py           # Schémas Pydantic (PredictionRequest, PredictionResponse)
│   ├── services.py          # Logique de prédiction / chargement du modèle
│   ├── database.py          # Connexion à la base PostgreSQL (optionnel)
│── model/
│   ├── random_forest.pkl    # Modèle ML sauvegardé
│   ├── preprocessor.pkl     # Prétraitement (si utilisé)
│── tests/
│   ├── test_api.py          # Tests de l'API
│   ├── test_model.py        # Tests du modèle
│── requirements.txt         # Dépendances Python
│── README.md                # Documentation principale
│── .env.example             # Exemple de configuration d'environnement
Installation
1️⃣ Cloner le projet
git clone https://github.com/userANNA123/deploy-ml-model.git
cd deploy-ml-model

2️⃣ Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.\.venv\Scripts\activate   # Windows

3️⃣ Installer les dépendances
pip install -r requirements.txt

 Base de données PostgreSQL

Créer la base :

CREATE DATABASE churn_db;
CREATE USER churn_user WITH PASSWORD '2025';
GRANT ALL PRIVILEGES ON DATABASE churn_db TO churn_user;


Configuration dans src/app/db.py :

DATABASE_URL = "postgresql+psycopg://churn_user:Anna2025@localhost:5432/churn_db"


Créer les tables :

python -m src.app.db

 Lancer l’API
uvicorn src.app.main:app --reload


API accessible sur :

http://127.0.0.1:8000

📘 Documentation interactive (Swagger)

 http://127.0.0.1:8000/docs

 http://127.0.0.1:8000/redoc

🔮 Endpoint /predict
 URL
POST http://127.0.0.1:8000/predict

 Input (Pydantic : PredictionRequest)
{
  "age": 30,
  "annee_experience_totale": 5,
  "revenu_mensuel": 3000,
  "distance_domicile_travail": 10,
  "nb_formations_suivies": 2,
  "nombre_heures_travaillees": 160,
  "frequence_deplacement": "Rarement"
}

 Output
{
  "prediction": 1
}

 Modèle Machine Learning

Dans ml_model.py, le modèle est chargé UNE SEULE FOIS :

MODEL_PATH = Path(__file__).resolve().parents[2] / "model" / "churn_model.joblib"
model = joblib.load(MODEL_PATH)

Feature Engineering

✔️ One-hot encoding
✔️ Variables dérivées :

experience_to_age

salary_category

long_commute

training_hours_per_year

work_life_balance

🧪 Tests unitaires
Lancer tous les tests :
pytest -v

Exemple :
def test_predict_from_dict_returns_0_or_1():
    y = predict_from_dict(VALID_DATA)
    assert y in [0, 1]

 Requirements.txt

Version professionnelle recommandée :

# Core Framework
fastapi==0.110.0
uvicorn[standard]==0.29.0

# Data Validation
pydantic==2.7.1

# Database
sqlalchemy==2.0.44
psycopg[binary]==3.2.1

# Machine Learning
scikit-learn==1.4.2
pandas==2.1.4
numpy>=1.26.0
joblib==1.3.2

# Testing
pytest==7.4.3
httpx==0.27.2

# API Docs & uploads
python-multipart==0.0.20

# Env
python-dotenv==1.2.1

📊 Exemple complet de requête (via cURL)
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "annee_experience_totale": 5,
    "revenu_mensuel": 3000,
    "distance_domicile_travail": 10,
    "nb_formations_suivies": 2,
    "nombre_heures_travaillees": 160,
    "frequence_deplacement": "Rarement"
  }'
 Auteur & Remerciements
Auteur : ANNA harba

Remerciements :

OpenClassrooms pour le projet

La communauté FastAPI

La communauté Python / Machine Learning

Fonctionnalités Clés
Fonctionnalité,Description,Technologies
 
Prédiction en temps réel,Endpoint /predict à faible latence.,"FastAPI, Random Forest"
Validation des données,Entrées et sorties strictement validées.,Pydantic
Traçabilité,Enregistrement de chaque requête (input/output) en base de données.,"SQLAlchemy, PostgreSQL"
Maintenance facilitée,Documentation automatique et tests unitaires complets.,"Swagger/Redoc, Pytest"
