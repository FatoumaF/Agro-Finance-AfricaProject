import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import nest_asyncio
import asyncio
import streamlit as st

# Charger les variables d'environnement à partir d'un fichier .env
load_dotenv()

# Configurer la clé API OpenAI
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Appliquer nest_asyncio pour exécuter des boucles d'événements imbriquées
nest_asyncio.apply()

# Configurer le modèle de langage OpenAI
llm = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo-0613")

# Titre de l'application
st.title("Extraction de contenu avec Streamlit")

# Saisie de la question par l'utilisateur
question = st.text_input("Posez votre question sur les critères de financement : ")

# Fonction pour charger et transformer les documents
async def load_and_transform_documents():
    loader = AsyncChromiumLoader(["https://www.enabel.be/"])
    docs =  loader.load()  

    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        docs, tags_to_extract=["div", "span", "h2", "a"]
    )

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, chunk_overlap=0)
    splits = splitter.split_documents(docs_transformed)

    return splits

# Fonction pour extraire le contenu en texte
async def extract_content(splits, question):
    extracted_texts = []
    for split in splits:
        content = split.page_content
        prompt = f"La réponse à votre question {question}\n\nContent:\n{content}"
        response = await llm.apredict(prompt)
        extracted_texts.append(response)
    return extracted_texts

# Exécuter le processus de chargement, transformation et extraction
async def main():
    if question:
        st.write("Recherche en cours...")
        splits = await load_and_transform_documents()
        extracted_texts = await extract_content(splits, question)
        for text in extracted_texts:
            st.text(text)  # Afficher chaque texte extrait

# Bouton pour déclencher la recherche lorsque l'utilisateur clique dessus
if st.button('Lancer la recherche'):
    asyncio.run(main())
