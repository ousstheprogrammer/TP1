# TP2 — Prompt Engineering & Sentiment Analysis

## Description
TP sur l'utilisation des LLMs pour des tâches de classification, notamment l'analyse de sentiment via le prompt engineering.

## Technologies utilisées
- Python 3.11+
- Anaconda / Jupyter Notebook
- tiktoken (tokenisation)
- LangChain + OpenAI GPT-4o
- Ollama (LLM local)

## Structure du projet
```
SMA_TokPr/
├── sma.ipynb         ← Notebook principal
├── reponses.md       ← Réponses aux questions du TP
├── screenshots/      ← Captures d'écran
├── .env              ← Clé API (NON versionnée)
├── .gitignore
└── README.md
```

## Installation avec Anaconda

```bash
# Ouvrir Anaconda Prompt et lancer Jupyter
jupyter notebook
```

Les dépendances s'installent directement dans la première cellule du notebook.

## Précautions
- Ne jamais committer le fichier `.env` (clé API secrète)
- Vérifier que `.env` est bien dans `.gitignore`
