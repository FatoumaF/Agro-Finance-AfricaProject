
---

# Analyse des Critères de Financement pour les Agriculteurs Africains

## Contexte

Ce projet a été développé pour une association facilitant la mise en relation entre les agriculteurs africains et les financeurs. L'objectif est de créer une IA capable de déterminer si un agriculteur est éligible à un financement, en fonction des critères définis par les financeurs. Le système analyse les données provenant de différentes sources : 

- Extraction des critères depuis des rapports PDF fournis par les financeurs.
- Extraction des critères directement depuis les sites web des financeurs, ce qui permet de s'adapter à de nouveaux financeurs en modifiant simplement le lien du site.

## Objectif

L'objectif est de créer un système d'analyse automatisée qui :
1. Extrait les critères de financement des rapports PDF et des sites web des financeurs.
2. Évalue l'éligibilité des agriculteurs à ces financements.
3. Facilite la mise en relation entre les agriculteurs et les financeurs si les critères sont remplis.

## Fonctionnalités

- Extraction de texte depuis des PDF pour analyser les critères de financement.
- Recherche de similarité pour trouver les parties pertinentes des rapports.
- Interface utilisateur avec Streamlit pour une interaction simple.
- Possibilité de changer la source d'extraction (PDF ou site web) pour s'adapter à différents financeurs.
- Utilisation d'OpenAI pour l'analyse et la génération de réponses sur les critères.

## Technologies Utilisées

- **Langage** : Python
- **Framework** : Streamlit pour l'interface utilisateur
- **IA/NLP** : OpenAI (LangChain pour la gestion des chaînes de traitement)
- **Gestion des Documents** : PyPDF2 pour l'extraction de texte depuis les PDF
- **Vector Store** : FAISS pour la recherche de similarité

## Prérequis

- Python 3.8+
- Une clé API OpenAI (à ajouter dans un fichier `.env`)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-repository/projet-clm.git
   cd projet-clm
   ```

2. Créez un environnement virtuel et activez-le :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Créez un fichier `.env` à la racine du projet pour y stocker votre clé API OpenAI :

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Utilisation

1. Lancez l'application Streamlit :

   ```bash
   streamlit run extract.py
   ```

2. Téléchargez un fichier PDF de critères de financement via l'interface Streamlit ou modifiez le lien du site web dans le code pour extraire les critères directement.

3. Posez une question sur les critères de financement à l'IA pour obtenir une réponse basée sur le contenu du PDF.



## Comment ça marche ?

1. **Lecture et Extraction** : Le contenu des PDF est lu et extrait avec PyPDF2, puis divisé en segments plus petits pour un traitement plus efficace.
2. **Création d'Embeddings** : Les segments de texte sont transformés en embeddings vectoriels avec OpenAI.
3. **Recherche de Similarité** : Les segments pertinents sont recherchés en fonction de la question posée par l'utilisateur.
4. **Génération de Réponses** : L'IA génère une réponse basée sur les documents les plus pertinents pour répondre à la question de l'utilisateur.

## Adaptation pour d'autres sources

Pour analyser les critères directement depuis un site web, modifiez le code pour utiliser un extracteur web. Par exemple, avec LangChain et un extracteur de contenu basé sur Chromium.

## Contribution

Toute contribution pour améliorer le projet est la bienvenue ! Veuillez créer une *issue* avant de soumettre une *pull request*.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
