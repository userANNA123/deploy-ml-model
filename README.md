<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<br />
<p align="center">
  <a href="#">
    <img src="https://via.placeholder.com/120" alt="Logo" width="120">
  </a>

  <h3 align="center">Déploiement d’un Modèle de Machine Learning avec CI/CD & Hugging Face 🚀</h3>

  <p align="center">
   Un projet complet démontrant comment déployer un modèle ML en production avec une pipeline CI/CD.
   <br />
   <a href="#">Explorer la documentation »</a>
   <br />
   <br />
   <a href="#">Voir la Demo</a>
   ·
   <a href="#">Signaler un Bug</a>
   ·
   <a href="#">Demander une Fonctionnalité</a>
  </p>
</p>

---

## 🧭 Table of Contents

- [À propos du projet](#à-propos-du-projet)
- [Objectifs](#objectifs)
- [Architecture du projet](#architecture-du-projet)
- [Pipeline CI/CD](#pipeline-cicd)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Exécution locale](#exécution-locale)
- [Déploiement](#déploiement)
- [Auteur](#auteur)

---

## 📌 À propos du projet

Ce projet consiste à déployer un modèle Machine Learning dans un environnement cloud en utilisant :

- **FastAPI ou Gradio** pour exposer une interface simple  
- **Hugging Face Spaces** pour héberger l’application  
- **GitHub Actions (CI/CD)** pour automatiser :
  - les tests  
  - la construction  
  - et le déploiement automatique  

Cela garantit que chaque modification poussée dans la branche `main` est automatiquement :

✔ testée  
✔ validée  
✔ déployée  

---

## 🎯 Objectifs

- Mettre en place un pipeline complet CI/CD  
- Automatiser les tests unitaires  
- Générer une application web simple pour exposer le modèle  
- Déployer automatiquement sur **Hugging Face Spaces**  

---

## 🏗 Architecture du projet

deploy-ml-model/
├── app.py
├── requirements.txt
├── .github/
│ └── workflows/
│ └── ci-cd.yml
├── tests/
├── src/
└── README.md

---

## ⚙️ Pipeline CI/CD

Voici les étapes automatisées par GitHub Actions :

1️⃣ **Tests**  
Exécute pytest pour vérifier que le code fonctionne.

2️⃣ **Build**  
Installe les dépendances et vérifie que tout compile.

3️⃣ **Déploiement Automatique**  
Le pipeline :
- crée ou met à jour le Space Hugging Face  
- upload automatiquement les fichiers du repo  
- relance l’application en ligne  

---

## 🧰 Technologies utilisées

| Outil | Usage |
|-------|--------|
| **Python 3.11** | Développement |
| **Gradio** | Interface utilisateur simple |
| **HuggingFace Hub** | Déploiement cloud |
| **GitHub Actions** | Automatisation CI/CD |
| **Pytest** | Tests unitaires |

---

## 🛠 Installation

```bash
git clone https://github.com/userANNA123/deploy-ml-model.git
cd deploy-ml-model
pip install -r requirements.txt
