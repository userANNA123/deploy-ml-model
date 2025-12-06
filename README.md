Déploiement d’un Modèle de Machine Learning avec CI/CD et Hugging Face
 À propos du projet

Ce projet consiste à déployer un modèle de Machine Learning dans un environnement cloud en utilisant :

FastAPI / Gradio pour exposer une interface simple

Hugging Face Spaces pour héberger l’application

GitHub Actions (CI/CD) pour automatiser les tests, la construction et le déploiement

Ce pipeline garantit que chaque modification poussée dans la branche main est automatiquement :

testée

validée

déployée en production

 Objectifs principaux

Mettre en place un pipeline CI/CD complet

Déployer automatiquement un modèle ML sur Hugging Face

Automatiser les tests unitaires

Gérer différents environnements : développement → production

Assurer une qualité continue du code

 Architecture du projet
deploy-ml-model/
│
├── app.py              # Application Gradio exposée
├── requirements.txt    # Dépendances
├── tests/              # Tests unitaires (pytest)
│   └── test_sanity.py
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml   # Pipeline CI/CD complet
│
└── README.md           # Documentation

🔧 Technologies utilisées
Technologie	Rôle
Python 3.11	Langage principal
Gradio	Interface Web
Hugging Face Hub	Hébergement de l'application
GitHub Actions	Automatisation CI/CD
Pytest	Exécution des tests unitaires
⚙️ Pipeline CI/CD – Explication

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

📄 Exemple de code (app.py)
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
