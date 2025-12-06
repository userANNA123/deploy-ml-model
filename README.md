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

<h2 align="center">Déploiement d’un Modèle de Machine Learning avec CI/CD & Hugging Face 🚀</h2>

<p align="center">
  Un pipeline complet pour tester, valider et déployer automatiquement un modèle de Machine Learning.  
  <br/>
  <a href="#"> Explorer la documentation</a> ·
  <a href="#"> Reporter un bug</a> ·
  <a href="#"> Demander une fonctionnalité</a>
</p>

---

## 🎓 Qu’allez-vous apprendre dans ce projet ?

Dans ce projet, vous allez consolider vos compétences en déployant un modèle de Machine Learning dans un environnement prêt pour la production.

Vous allez découvrir :

- 🚀 **Le développement d’API avec FastAPI**
- 🧪 **Les tests unitaires avec Pytest**
- 🔄 **La gestion des versions avec Git**
- ⚙️ **La création d’un pipeline CI/CD avec GitHub Actions**
- ☁️ **Le déploiement sur Hugging Face Spaces (Gradio)**
- 🗄️ **L’organisation d’un projet ML conforme aux standards professionnels**

Ces notions sont indispensables pour industrialiser un modèle ML et garantir sa fiabilité.

---

## 🧭 Étapes du projet (selon OpenClassrooms)

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


deploy-ml-model/
│
├── app.py
├── requirements.txt
├── README.md
├── src/
│ ├── app/
│ │ ├── api.py
│ │ ├── model.py
│ │ └── schemas.py
│ └── db/
│ └── config.py
│
├── tests/
│ ├── test_api.py
│ └── test_sanity.py
│
└── .github/
└── workflows/
└── ci-cd.yml

yaml
Copy code

└── README.md           # Documentation

---

## Installation

```bash
git clone https://github.com/userANNA123/deploy-ml-model.git
cd deploy-ml-model
pip install -r requirements.txt

Technologies utilisées
Technologie	Rôle
Python 3.11	Langage principal
Gradio	Interface Web
Hugging Face Hub	Hébergement de l'application
GitHub Actions	Automatisation CI/CD
Pytest	Exécution des tests unitaires
 Pipeline CI/CD – Explication

Le fichier .github/workflows/ci-cd.yml comporte 3 jobs :

✔️ 1. Tests

Installe Python + dépendances

Exécute :

pytest


Valide que le code fonctionne avant de continuer

✔️ 2. Build

Vérifie que les dépendances sont installables

S’assure que le projet peut être construit sans erreur

✔️ 3. Déploiement automatique

Si les étapes précédentes réussissent, la mise en production est déclenchée :

Création / mise à jour automatique du Space Hugging Face

Upload du projet via HfApi

Déploiement instantané 

 Exemple de code (app.py)
import gradio as gr

def greet(name):
    return f"Hello {name}! 

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Hello Space",
    description="Application ML déployée automatiquement avec CI/CD "
)

if __name__ == "__main__":
    demo.launch()

Tests

Un test minimal a été créé pour valider la structure :

def test_ok():
    assert 1 + 1 == 2

Déploiement

Le déploiement est automatique :

Tu fais un git push origin main

GitHub Actions lance le pipeline

Le Space Hugging Face est mis à jour

L'application est reconstruite et mise en ligne

 Lien vers l’application

 (Ajoute ton lien Hugging Face ici une fois le déploiement final terminé)

 Auteur

Projet réalisé par Anna HARBA, dans le cadre du projet OpenClassrooms – Data Analyst.
pip install -r requirements.txt
