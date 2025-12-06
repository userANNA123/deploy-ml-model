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

✅ Une API REST avec FastAPI pour exposer le modèle

✅ Un schéma d’entrée clairement défini avec Pydantic

✅ Un modèle Random Forest pré-entraîné et chargé depuis un fichier

✅ Une documentation interactive automatique de l’API (Swagger / OpenAPI)

✅ Une base pour les tests unitaires et fonctionnels avec Pytest

Client : Futurisys
Contexte : Projet professionnel – Déploiement d’un modèle ML en production
Auteur : ANNA <Ton nom complet>

🎯 Livrables

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

## 🏗️ Architecture du projet
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

🛠️ Installation
🔹 Prérequis

Python 3.9 ou supérieur

(Optionnel mais recommandé) PostgreSQL si tu enregistres les prédictions dans une base

Git

Un compte GitHub (pour versionner le projet)

🔹 Cloner le dépôt

git clone https://github.com/<ton-utilisateur>/<ton-repo>.git
cd <ton-repo>

🔹 Créer un environnement virtuel
bash
Copy code
python -m venv venv
source venv/bin/activate      # Sur Linux / macOS
venv\Scripts\activate         # Sur Windows
🔹 Installer les dépendances
bash
Copy code
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
⚙️ Configuration (optionnel : base de données)


env
Copy code
# Database (optionnel)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ml_db

# API
API_HOST=0.0.0.0
API_PORT=8000

# Environment
ENVIRONMENT=development
DEBUG=True


📖 Utilisation
🔹 Démarrer l’API
En développement (rechargement automatique) :

bash
Copy code
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
En production (sans --reload) :

bash
Copy code
uvicorn app.main:app --host 0.0.0.0 --port 8000
L’API sera accessible à l’adresse :
👉 http://localhost:8000

🔹 Documentation interactive
Une fois l’API démarrée, tu peux accéder à :

Swagger UI : http://localhost:8000/docs

ReDoc : http://localhost:8000/redoc

Schéma OpenAPI : http://localhost:8000/openapi.json

📡 Exemples de requêtes
✅ Endpoint de prédiction
URL : POST http://localhost:8000/predict

Body JSON d’exemple (adapté à ton PredictionRequest) :

json
Copy code
{
  "age": 34,
  "annee_experience_totale": 5,
  "revenu_mensuel": 2500.0,
  "distance_domicile_travail": 7.5,
  "nb_formations_suivies": 2,
  "nombre_heures_travaillees": 38.0,
  "frequence_deplacement": "Rarement"
}
Réponse JSON (exemple) :

json
Copy code
{
  "prediction": 0
}
où :

0 = reste

1 = churn / départ

💻 Exemple avec curl
bash
Copy code
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 34,
    "annee_experience_totale": 5,
    "revenu_mensuel": 2500.0,
    "distance_domicile_travail": 7.5,
    "nb_formations_suivies": 2,
    "nombre_heures_travaillees": 38.0,
    "frequence_deplacement": "Rarement"
  }'
🧪 Tests
Les tests sont écrits avec Pytest et couvrent :

la bonne réponse de l’API (/predict)

la validation des données par les schémas Pydantic

le fonctionnement du modèle ML (dimensions, types, etc.)

🔹 Lancer tous les tests
bash
Copy code
pytest
🔹 Avec affichage détaillé
bash
Copy code
pytest -v
🔹 Avec rapport de couverture
bash
Copy code
pytest --cov=app --cov-report=term-missing


🧠 Modèle de Machine Learning
🔹 Type de modèle
Le modèle utilisé est un :

RandomForestClassifier (scikit-learn)

Caractéristiques typiques (à adapter à ton code exact) :

n_estimators : 100 – 500

Gère bien les relations non linéaires

Robuste au bruit et aux variables corrélées

🔹 Données d’entrée
Le modèle utilise plusieurs variables comme :

age

annee_experience_totale

revenu_mensuel

distance_domicile_travail

nb_formations_suivies

nombre_heures_travaillees

frequence_deplacement (catégorielle : "Jamais", "Rarement", "Souvent")

Ces variables sont converties/encodées dans le même format que lors de l’entraînement du modèle.

🔹 Performances (à compléter)


Accuracy : …

F1-score : …

Recall : …

Precision : …

Et éventuellement :

Courbe ROC-AUC

Matrice de confusion

🔹 Limites du modèle
Performances dépendantes de la qualité des données d’entraînement

Risque de biais si le dataset est déséquilibré

Interprétabilité plus faible qu’un modèle linéaire

🗄️ Base de données (si utilisée)


Exemple de table :

model_inputs ou predictions :

id : identifiant unique

input_data : données d’entrée (JSON ou colonnes normalisées)

prediction : 0 ou 1

created_at : timestamp

(optionnel) model_version

Les scripts de création peuvent être :

via SQLAlchemy (code Python)

via script SQL (fichier .sql)

🔐 Sécurité (niveau de base)


Validation stricte des entrées avec Pydantic

Utilisation de variables d’environnement pour la configuration (.env)

Pas de secrets (mots de passe, clés) dans le code versionné

🔜 Améliorations possibles :

Authentification JWT

Gestion des rôles utilisateurs

Rate limiting

🔄 CI/CD (optionnel / améliorable)


Un pipeline GitHub Actions qui :

lance les tests

génère le rapport de couverture

vérifie l’installation du projet

déploie sur un serveur ou sur un service (Railway, Render, etc.)

Pour l’instant, tu peux simplement mentionner :

Le projet est prêt à être intégré dans un pipeline CI/CD (tests automatisés via Pytest, dépendances listées dans requirements.txt, configuration externe via .env).

📊 Monitoring et évolution
Endpoint /predict utilisé comme point central pour la prédiction

Possibilité de logger les requêtes pour analyser les usages

Possibilité d’améliorer le modèle en réentraînant régulièrement avec de nouvelles données

🤝 Contribution
Forker le projet

Créer une branche :

bash
Copy code
git checkout -b feature/nouvelle-fonctionnalite
Committer les changements :

bash
Copy code
git commit -m "Ajout d'une nouvelle fonctionnalité"
Pousser la branche :

bash
Copy code
git push origin feature/nouvelle-fonctionnalite
Ouvrir une Pull Request

📝 Versions


bash
Copy code
git tag -l
git tag v1.0.0
git push origin v1.0.0
📄 Licence
Ce projet peut être distribué sous licence MIT (ou une autre licence de ton choix).

👤 Auteur & Remerciements
Auteur : ANNA <Ton nom>

Remerciements :

OpenClassrooms pour le projet

La communauté FastAPI

La communauté Python / Machine Learning
