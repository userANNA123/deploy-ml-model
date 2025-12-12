<<<<<<< HEAD
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/logo.png" alt="Logo" width="120">
  </a>

  <h3 align="center">Déploiement d’un Modèle Machine Learning avec CI/CD & Hugging Face</h3>

  <p align="center">
    Un pipeline complet pour tester, valider et déployer automatiquement un modèle de Machine Learning.
    <br />
    <a href="#">📘 Explorer la documentation</a>
    ·
    <a href="#">🐞 Reporter un bug</a>
    ·
    <a href="#">✨ Demander une fonctionnalité</a>
  </p>
</p>

---

<!-- TABLE OF CONTENTS -->
### 📚 Table des Matières
<details>
  <summary>Cliquer pour dérouler</summary>
  <ol>
    <li><a href="#-à-propos-du-projet">À propos du Projet</a></li>
    <li><a href="#-pipeline-cicd--architecture">Pipeline CI/CD & Architecture</a></li>
    <li><a href="#-technologies-utilisées">Technologies Utilisées</a></li>
    <li><a href="#-installation">Installation</a></li>
    <li><a href="#-utilisation">Utilisation</a></li>
    <li><a href="#-structure-du-référentiel">Structure du Référentiel</a></li>
    <li><a href="#-contributrice">Contributrice</a></li>
  </ol>
</details>

---

## 📌 À propos du Projet

Ce projet met en place un pipeline complet d’automatisation CI/CD pour déployer un modèle de Machine Learning dans le cloud.

Le système assure que chaque mise à jour de code soit :

- automatiquement **testée**
- validée via GitHub Actions
- puis **déployée** sur Hugging Face Spaces

Le but :  
➡️ garantir une livraison continue, stable et 100% automatisée.

---

## ⚙️ Pipeline CI/CD — Architecture

Voici l’architecture complète du workflow :

```mermaid
flowchart LR
    A[Push Git ➜ main] --> B[GitHub Actions CI]
    B --> C[Tests PyTest]
    C --> D[Build & Validation]
    D --> E[Déploiement Automatique sur Hugging Face]
    E --> F[Application ML Disponible en Ligne]
=======
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

 🚀 Déploiement d’un Modèle de Machine Learning avec FastAPI & CI/CD
📌 Présentation du projet

Ce projet consiste à déployer un modèle de Machine Learning (Random Forest) en production via une API REST FastAPI.
L’API permet de prédire le churn (attrition) à partir de caractéristiques professionnelles.

Le projet intègre :

une API FastAPI

une validation stricte des données avec Pydantic

un modèle ML pré-entraîné

une base de données PostgreSQL pour la traçabilité

des tests unitaires et fonctionnels

un workflow CI/CD GitHub Actions

🧱 Architecture du projet
project/
│── src/
│   └── app/
│       ├── main.py          # Point d’entrée FastAPI
│       ├── schemas.py       # Schémas Pydantic
│       ├── services.py      # Logique ML / prédiction
│       ├── database.py      # Connexion PostgreSQL (SQLAlchemy)
│       └── models.py        # Modèles ORM
│── model/
│   └── churn_model.joblib   # Modèle ML sauvegardé
│── tests/
│   ├── test_api.py          # Tests API
│   └── test_model.py        # Tests ML
│── requirements.txt
│── .env.example
│── README.md

⚙️ Installation
1️⃣ Cloner le projet
git clone https://github.com/userANNA123/deploy-ml-model.git
cd deploy-ml-model

2️⃣ Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate    # Linux / Mac
.\.venv\Scripts\activate    # Windows

3️⃣ Installer les dépendances
pip install -r requirements.txt

🗄️ Base de données PostgreSQL
Création de la base
CREATE DATABASE churn_db;
CREATE USER churn_user WITH PASSWORD '<PASSWORD>';
GRANT ALL PRIVILEGES ON DATABASE churn_db TO churn_user;

Configuration (variables d’environnement)

Créer un fichier .env (non versionné) :

DATABASE_URL=postgresql+psycopg://<USER>:<PASSWORD>@localhost:5432/churn_db


Dans le code (database.py) :

import os
DATABASE_URL = os.getenv("DATABASE_URL")


🔐 Bonne pratique : les identifiants ne sont jamais stockés en clair dans le code ou le README.

▶️ Lancer l’API
uvicorn src.app.main:app --reload


API disponible sur :
👉 http://127.0.0.1:8000

Documentation interactive :

Swagger : http://127.0.0.1:8000/docs

Redoc : http://127.0.0.1:8000/redoc

🔮 Endpoint /predict
Requête POST
POST /predict

Exemple d’entrée (JSON)
{
  "age": 30,
  "annee_experience_totale": 5,
  "revenu_mensuel": 3000,
  "distance_domicile_travail": 10,
  "nb_formations_suivies": 2,
  "nombre_heures_travaillees": 160,
  "frequence_deplacement": "Rarement"
}

Réponse
{
  "prediction": 1
}

🧪 Tests

Lancer tous les tests :

pytest -v


Les tests couvrent :

le chargement du modèle

la fonction de prédiction

l’endpoint API /predict

👩‍💻 Auteure

Anna Harba
Projet réalisé dans le cadre du parcours Machine Learning Engineer / Data – OpenClassrooms.

⭐ Points clés du projet

API performante et documentée automatiquement

Validation stricte des données (Pydantic v2)

Traçabilité des prédictions en base de données

Tests unitaires et fonctionnels

Architecture prête pour la production 