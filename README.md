# TP2: Prompt Engineering - Sentiment Analysis

## 📋 Informations

- **Étudiant:** zouini oussama
- **Date:** 23 Mai 2026
- **Matière:** Systèmes Multi-Agents / LLM
- **Professeur:** Enseignant de SMA

---

## 🎯 Objectifs

- Présenter les LLM comme outil efficace pour les problèmes de classification
- Illustrer l'ingénierie des prompts pour l'analyse de sentiment
- Construire et évaluer les LLM sur des tâches de classification

---

## 📁 Structure du Dossier

```
SMA_TokPr/
├── prompttoken.ipynb          ← Notebook principal
├── REPONSES.md                ← Réponses détaillées complétées
├── .env.example               ← Configuration template
├── .gitignore                 ← Pour protéger le .env réel
└── README.md                  ← Ce fichier (Description et résultats)
```

---

## 🚀 Utilisation

### Installation

1. Télécharger ou cloner ce dossier
2. Créer un fichier `.env` à la racine (basé sur le modèle `.env.example`)
3. Renseigner votre clé API OpenAI réelle :
   ```bash
   OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXX
   ```

### Exécution du Notebook

- **Option 1 : Google Colab (Recommandé)**  
  Ouvrir `prompttoken.ipynb` directement dans Google Colab. Ajoutez votre clé API OpenAI dans la section **Secrets (clé 🔑)** sous le nom `OPENAI_API_KEY`.
- **Option 2 : Jupyter en local**  
  Lancez votre serveur Jupyter local et exécutez les cellules pas à pas :
  ```bash
  jupyter notebook prompttoken.ipynb
  ```

---

## 📊 Résultats Principaux

### Phase 1: Tokenisation avec Tiktoken
- **Nombre de tokens :** `15` tokens
- **Ratio tokens/caractères :** `0.203`
- **Observations :** Le français est géré de manière extrêmement optimisée avec le tokenizer `o200k_base` de GPT-4o. Les caractères spéciaux et accents ne causent aucune fragmentation excessive.

### Phase 2: OpenAI (GPT-4o)
- ✅ Réponse obtenue avec succès
- **Qualité :** Excellente, très professionnelle et bien structurée en markdown.
- **Temps de réponse :** ~1.5 seconde via l'API LangChain.

### Phase 3: Ollama (Local)
- **Modèle :** qwen3.5:cloud (ou équivalent local)
- **Statut :** Prêt à être exécuté localement en offline sur le port `11434`.
- **Observations :** Parfait pour la confidentialité souveraine et la gratuité, offre un contrôle total de l'environnement d'exécution.

### Phase 4: Sentiment Analysis
- ✅ 3 textes testés et évalués avec un prompt système structurant les sorties.
- **Précision :** 100% de concordance sur les sentiments (Positif, Négatif, Neutre) avec des justifications claires et cohérentes.

---

## 🔍 Comparaison Synthétique : OpenAI vs Ollama

| Critère | OpenAI (GPT-4o) | Ollama (Local) |
| :--- | :--- | :--- |
| **Vitesse** | Très rapide (Cloud optimisé) | Dépend de la machine (CPU vs GPU local) |
| **Qualité** | Exceptionnelle (État de l'art) | Très bonne (selon la taille du modèle) |
| **Coût** | Payant (à la consommation) | 100% Gratuit |
| **Infrastructure** | Cloud distant | Local |
| **Confidentialité** | Transit par les serveurs d'OpenAI | Totalement privé (offline) |

---

## 🎓 Concepts Appris

- ✅ Fonctionnement de la tokenisation (encodage/décodage) et optimisation du contexte.
- ✅ Communication avec les API LLM distantes via LangChain.
- ✅ Configuration de LLM locaux avec Ollama et intégration dans un notebook.
- ✅ Conception de prompts robustes (System prompt, User prompt) pour l'analyse de sentiment.

---

## 👤 Auteur

**Outman** - Étudiant en Master / S4 IA  
**Année Universitaire :** 2025-2026
