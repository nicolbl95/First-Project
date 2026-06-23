# 📊 Assistant IA Multi-Agents — Analyse Financière

![Python 3.14](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge\&logo=visualstudiocode\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-121212?style=for-the-badge\&logo=langchain\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge\&logo=langchain\&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-7B3FE4?style=for-the-badge\&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0073EC?style=for-the-badge\&logo=databricks\&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge\&logo=ollama\&logoColor=white)
![Groq API](https://img.shields.io/badge/Groq_API-00D4AA?style=for-the-badge\&logo=groq\&logoColor=white)

[![🚀 Démo Live](https://img.shields.io/badge/%F0%9F%9A%80_D%C3%A9mo_Live-Streamlit_Cloud-FF4B4B?style=for-the-badge)](https://multiagent-financial-analyzer.streamlit.app/)

---

## 📖 Description

**Assistant IA Multi-Agents — Analyse Financière** est une application web développée avec **Streamlit** qui analyse automatiquement des rapports financiers PDF grâce à une architecture multi-agents basée sur **LangGraph**, **LangChain**, **RAG** et **ChromaDB**.

L'application permet à un utilisateur de téléverser un rapport financier PDF ou de sélectionner l’un des rapports d’exemple intégrés pour obtenir une analyse structurée des risques et une synthèse managériale.

L’objectif du projet est de démontrer une architecture IA modulaire proche d’un cas d’usage professionnel : extraction documentaire, recherche sémantique, analyse par LLM, génération de synthèse et interface web utilisable.

ℹ️ **Démo en ligne :**
Vous pouvez tester directement l'application sans installation ici :
https://multiagent-financial-analyzer.streamlit.app/

---

## 📸 Aperçu de l'interface

![Interface de l'application](assets/1dashboard.png)

*Interface Streamlit avec sélection de langue, rapports préchargés, import PDF et compteur en temps réel pendant l’analyse.*

---

## ✨ Fonctionnalités clés

* 🤖 **Architecture multi-agents avec LangGraph**
  Le traitement est séparé entre plusieurs agents spécialisés : extraction documentaire, analyse des risques et rédaction de synthèse.

* 📄 **Analyse de rapports financiers PDF**
  L’utilisateur peut importer son propre fichier PDF directement depuis l’interface.

* 📊 **Rapports préchargés**
  Trois exemples de rapports financiers sont intégrés : **BioSensus**, **TechNova** et **OmniDrive**. Cela permet de tester l’application immédiatement sans chercher de fichier externe.

* 🌍 **Interface bilingue français / anglais**
  L’utilisateur peut changer la langue de l’interface en un clic.

* ⏱️ **Compteur en temps réel**
  Un indicateur affiche le temps estimé et le temps écoulé pendant l’exécution des agents.

* 🧠 **Pipeline RAG avec ChromaDB**
  Le contenu du PDF est découpé en morceaux, indexé et réutilisé comme contexte pour améliorer la qualité de l’analyse.

* 🐳 **Support Docker**
  Le projet contient un `Dockerfile` permettant de lancer l’application dans un conteneur portable.

---

## 🧠 Architecture du système

L’application repose sur une architecture en trois agents :

### 1. Agent Extracteur

L’agent extracteur lit le rapport PDF, extrait le texte, le découpe en segments et prépare les données pour la recherche sémantique.

Technologies principales :

* `PyPDFLoader`
* `RecursiveCharacterTextSplitter`
* `ChromaDB`

### 2. Agent Analyste

L’agent analyste réalise une analyse des risques financiers, stratégiques, opérationnels et réglementaires à partir du contexte extrait via le pipeline RAG.

Il identifie notamment :

* les risques financiers ;
* les incohérences potentielles ;
* les dépendances économiques ;
* les risques opérationnels ;
* les signaux faibles utiles pour un décideur.

### 3. Agent Rédacteur

L’agent rédacteur transforme l’analyse brute en synthèse claire et structurée pour un lecteur non technique ou un dirigeant.

Il produit une restitution plus lisible, orientée décision, avec un langage simple et professionnel.

---

## 🔁 Flux de traitement

```text
PDF utilisateur ou rapport préchargé
        ↓
Agent Extracteur
        ↓
Extraction du texte + découpage en chunks
        ↓
Indexation dans ChromaDB
        ↓
Agent Analyste
        ↓
Analyse des risques financiers
        ↓
Agent Rédacteur
        ↓
Synthèse managériale
        ↓
Affichage dans l’interface Streamlit
```

---

## 🛠️ Technologies utilisées

| Technologie     | Rôle                                                      |
| --------------- | --------------------------------------------------------- |
| **Python 3.14** | Langage principal du projet                               |
| **Streamlit**   | Interface web interactive                                 |
| **LangGraph**   | Orchestration des agents IA                               |
| **LangChain**   | Intégration des LLM et composants RAG                     |
| **ChromaDB**    | Base vectorielle pour la recherche sémantique             |
| **RAG**         | Recherche augmentée pour améliorer les réponses du modèle |
| **Ollama**      | Exécution locale possible d’un modèle LLM                 |
| **Groq API**    | Exécution cloud rapide du modèle LLM                      |
| **Docker**      | Conteneurisation de l’application                         |
| **VS Code**     | Environnement de développement                            |

---

## 📂 Structure du projet

```text
├── agents/                         # Agents IA spécialisés orchestrés par LangGraph
│   ├── __init__.py
│   ├── analyzer.py                 # Agent d'analyse des risques financiers
│   ├── extractor.py                # Agent d'extraction, chunking PDF et RAG
│   └── writer.py                   # Agent de rédaction de la synthèse managériale
│
├── assets/                         # Images et ressources visuelles du projet
│   └── 1dashboard.png              # Capture d'écran de l'interface
│
├── sample_reports/                 # Rapports PDF financiers d'exemple
│   ├── Rapport_Financier_Avance_OmniDrive.pdf
│   ├── Rapport_Financier_TechNova.pdf
│   └── Rapport_Performance_BioSensus_2025.pdf
│
├── utils/                          # Fonctions utilitaires partagées
│
├── .gitignore                      # Fichiers exclus du suivi Git
├── Dockerfile                      # Configuration Docker du projet
├── app.py                          # Interface utilisateur Streamlit
├── graph_builder.py                # Construction et compilation du graphe LangGraph
├── README.md                       # Documentation principale du projet
└── requirements.txt                # Dépendances Python du projet
```

> Les dossiers et fichiers locaux comme `venv/`, `.env`, `.vscode/` et `__pycache__/` ne doivent pas être envoyés sur GitHub.

---

## 🚀 Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/nicolbl95/MultiAgent-Financial-Analyzer.git
cd MultiAgent-Financial-Analyzer
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l’environnement virtuel

Sur Windows avec Git Bash :

```bash
source venv/Scripts/activate
```

Sur Windows avec PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

Sur macOS ou Linux :

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Lancer l’application

```bash
streamlit run app.py
```

L’application sera disponible localement à l’adresse :

```text
http://localhost:8501
```

---

## 🔐 Configuration des variables d’environnement

Si vous utilisez **Groq API**, créez un fichier `.env` à la racine du projet :

```env
GROQ_API_KEY=votre_cle_api_ici
```

⚠️ Le fichier `.env` ne doit jamais être envoyé sur GitHub.

Il doit être présent dans `.gitignore` :

```text
.env
venv/
__pycache__/
*.pyc
.vscode/
```

---

## 🐳 Utilisation avec Docker

Le projet contient un `Dockerfile` permettant de lancer l’application dans un conteneur.

### 1. Construire l’image Docker

```bash
docker build -t financial-analyzer .
```

### 2. Lancer le conteneur

```bash
docker run -p 8501:8501 financial-analyzer
```

L’application sera disponible à l’adresse :

```text
http://localhost:8501
```

### Dockerfile utilisé

```dockerfile
# Image Python légère
FROM python:3.14-slim

# Empêche Python de créer des fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Affiche immédiatement les logs dans Docker
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier le projet
COPY . .

# Port Streamlit
EXPOSE 8501

# Lancer l'application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 📦 Fichier `.dockerignore` recommandé

Pour éviter de copier des fichiers inutiles ou sensibles dans l’image Docker, il est recommandé de créer un fichier `.dockerignore` :

```text
venv/
__pycache__/
.git/
.gitignore
.env
.vscode/
*.pyc
```

Cela permet de garder l’image Docker plus légère et plus sécurisée.

---

## 🌐 Démo en ligne

L’application est déployée avec Streamlit Community Cloud :

https://multiagent-financial-analyzer.streamlit.app/

Cette démo permet de tester le projet sans installation locale.

---

## 🧪 Exemples inclus

Le dossier `sample_reports/` contient trois rapports financiers de démonstration :

| Rapport            | Description                                              |
| ------------------ | -------------------------------------------------------- |
| **BioSensus 2025** | Rapport de performance financière                        |
| **TechNova**       | Rapport financier d’une entreprise technologique fictive |
| **OmniDrive**      | Rapport financier avancé d’une entreprise fictive        |

Ces fichiers permettent de tester rapidement le fonctionnement de l’application.

---

## ⚠️ Limites actuelles

* L’application fonctionne mieux avec des PDF contenant du texte sélectionnable.
* Les PDF scannés ou sous forme d’image peuvent nécessiter un OCR.
* Les analyses générées par IA peuvent contenir des erreurs.
* Les résultats doivent être considérés comme une aide à l’analyse, et non comme un conseil financier professionnel.
* La qualité des réponses dépend de la qualité du rapport PDF fourni.

---

## 🔮 Améliorations possibles

* Ajouter un OCR pour les PDF scannés.
* Ajouter une extraction automatique des tableaux financiers.
* Générer des graphiques financiers à partir des données extraites.
* Ajouter un export PDF ou Word de la synthèse.
* Ajouter des tests unitaires.
* Ajouter GitHub Actions pour automatiser les vérifications.
* Améliorer la mémoire entre agents.
* Ajouter une comparaison automatique entre plusieurs rapports financiers.
* Ajouter un mode d’analyse plus détaillé pour les investisseurs.

---

## 👨‍💻 Auteur

Projet développé par **nicolbl95**.

GitHub : https://github.com/nicolbl95

---

## 📄 Licence

Ce projet est publié à des fins d’apprentissage, de démonstration et de portfolio.

---

## ✅ Résumé

Ce projet démontre la mise en place d’une application IA complète combinant :

* interface web ;
* traitement de documents PDF ;
* architecture multi-agents ;
* RAG ;
* base vectorielle ;
* LLM local ou cloud ;
* conteneurisation Docker ;
* déploiement en ligne.

Il illustre une approche pratique de l’ingénierie LLM appliquée à l’analyse documentaire financière.
