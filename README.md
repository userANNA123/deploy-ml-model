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
