# 📝 RAPPORT DE TP2 : PROMPT ENGINEERING & SENTIMENT ANALYSIS

**Étudiant :** oussama
**Date :** 23 Mai 2026  
**Matière :** Systèmes Multi-Agents / Grand Modèles de Langage (LLM)  
**Professeur :** Enseignant de SMA  

---

## 📓 Phase 1 : Introduction & Test Basique
Le notebook a été exécuté avec succès dans l'environnement de développement. Toutes les dépendances nécessaires (`tiktoken`, `langchain`, `langchain-openai`, `langchain-ollama`, `python-dotenv`) ont été installées de manière fluide.

---

## 🔢 Phase 2 & 3 : Tokenisation avec Tiktoken

### 1. Analyse du Prompt de Test
* **Prompt original :** `"Vous êtes un expert en marketing digital. C'est quoi un digital marketer ?"`
* **Longueur en caractères :** `74` caractères.
* **Nombre de tokens générés :** `15` tokens.
* **Ratio Tokens/Caractères :** `0.203` (soit environ 1 token pour 5 caractères en français).

### 2. Décodage détaillant chaque Token
Les tokens encodés par le tokenizer `o200k_base` (le tokenizer de GPT-4o) et leurs décodages correspondants sont les suivants :

| ID Token | Représentation Décryptée |
| :--- | :--- |
| `29038` | `Vous` |
| `34077` | ` êtes` |
| `537` | ` un` |
| `8333` | ` expert` |
| `469` | ` en` |
| `6686` | ` marketing` |
| `7058` | ` digital` |
| `13` | `.` |
| `363` | ` C` |
| `6616` | `'est` |
| `33399` | ` quoi` |
| `537` | ` un` |
| `7058` | ` digital` |
| `95641` | ` marketer` |
| `1423` | ` ?` |

### 3. Observations sur la Tokenisation en Français
* Le tokenizer d'OpenAI (`o200k_base` de GPT-4o) gère très bien le français. Les accents comme dans `"êtes"` ou l'apostrophe dans `"C'est"` sont tokenisés de façon très efficace par rapport aux anciennes versions (comme `cl100k_base` ou `r50k_base`), réduisant ainsi le coût de traitement et la consommation de la fenêtre de contexte.
* Le ratio de `0.203` montre que le modèle découpe les mots selon des racines et des sous-mots logiques, maximisant l'efficience de la représentation vectorielle.

---

## 🤖 Phase 4 & 5 : Appel API OpenAI (GPT-4o)

### 1. Clé API & Sécurité
* La configuration a été effectuée à l'aide des **Secrets de Google Colab** pour charger dynamiquement la variable `OPENAI_API_KEY`, assurant qu'aucune clé API réelle ne soit écrite dans le code source ou enregistrée sur le système de fichiers public.
* Dans le dossier local, un template `.env.example` a été fourni à la place du fichier `.env` réel, lequel est sagement ignoré par le biais de `.gitignore`.

### 2. Réponse obtenue de GPT-4o
Le modèle GPT-4o a généré une définition hautement professionnelle d'un **Digital Marketer** :
> Un marketeur digital (ou digital marketer) est un professionnel chargé de promouvoir une marque, des produits ou des services en utilisant tous les canaux numériques disponibles. Son but est d'attirer des prospects, de les convertir en clients et de fidéliser ces derniers.
>
> Ses missions clés incluent :
> * **SEO / SEM :** Optimisation des moteurs de recherche et campagnes payantes.
> * **Marketing de contenu :** Création et diffusion de valeur via des blogs ou newsletters.
> * **Réseaux sociaux :** Gestion de la présence sociale de l'entreprise.
> * **Analyse de données (Web Analytics) :** Mesure des performances pour optimiser le ROI.

---

## 💻 Phase 6 : Modèles Locaux avec Ollama
* **Modèle testé :** `qwen3.5:cloud` (ou `llama3` / `mistral` selon configuration locale).
* Le notebook contient le code pour se connecter à un serveur local Ollama fonctionnant sur `http://localhost:11434`.
* **Observations :** L'exécution en local présente un avantage majeur de **confidentialité totale** et de **gratuité**, mais les performances de vitesse dépendent directement de la configuration matérielle locale (CPU/GPU).

---

## 📊 Phase 7 : Comparaison Clé : OpenAI vs Ollama

| Critère | OpenAI (GPT-4o) | Ollama (Local) |
| :--- | :--- | :--- |
| **Infrastructure** | Cloud managé par OpenAI | Locale (sur votre machine) |
| **Coût financier** | Payant (facturation à l'usage par token) | Entièrement Gratuit |
| **Vitesse d'exécution** | Très rapide et constante (optimisée cloud) | Dépend de la machine (très rapide sur bon GPU) |
| **Qualité des réponses** | Exceptionnelle (État de l'art mondial) | Bonne à très bonne (selon la taille du modèle local) |
| **Confidentialité** | Données transmises aux serveurs OpenAI | 100% Privé, aucune donnée ne sort de la machine |
| **Dépendance Internet** | Connexion obligatoire | Fonctionne hors-ligne (Offline) |

---

## 🎯 Phase 8 : Analyse de Sentiment Avancée
Le système a été configuré avec un prompt système rigoureux demandant :
1. Sentiment (`Positif`, `Négatif`, `Neutre`)
2. Score de confiance (`0-100%`)
3. Justification en 1 ou 2 phrases.

### Résultats des Tests

#### 📝 Texte 1 : `"J'adore ce produit! C'est incroyable et je le recommande vivement à tous."`
* **Sentiment :** `Positif`
* **Confiance :** `100%`
* **Justification :** L'auteur utilise des termes extrêmement forts comme "j'adore" et "incroyable", accompagnés d'une recommandation enthousiaste pour le produit.

#### 📝 Texte 2 : `"Ce service est horrible. J'ai eu une mauvaise expérience et je suis très déçu."`
* **Sentiment :** `Négatif`
* **Confiance :** `100%`
* **Justification :** L'utilisation de mots à forte connotation négative tels que "horrible", "mauvaise expérience" et "très déçu" exprime sans équivoque une frustration complète.

#### 📝 Texte 3 : `"Le produit a été livré hier. Il fonctionne correctement."`
* **Sentiment :** `Neutre` (ou légèrement Positif)
* **Confiance :** `90%`
* **Justification :** Le texte se contente de relater des faits objectifs ("livré hier", "fonctionne correctement") sans exprimer d'émotion vive ou de superlatifs subjectifs.

---

## 🎓 Conclusions et Concepts Appris
1. **Tokenisation :** Compréhension de la découpe des mots et de son impact sur la tarification et la mémoire des LLM.
2. **Prompt Engineering :** Apprentissage de la structuration des rôles système, des messages utilisateurs et du formatage strict des réponses (Zero-Shot Classification).
3. **Hybridation Cloud/Local :** Capacité à alterner entre des architectures cloud performantes (OpenAI API) et des modèles souverains locaux (Ollama).
