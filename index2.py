import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI

# Charger les variables d'environnement à partir d'un fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
openai_api_key = os.getenv("OPENAI_API_KEY")

# Vérifiez que la clé API a été correctement chargée
if not openai_api_key:
    st.error("La clé API OpenAI n'a pas été trouvée dans les variables d'environnement.")
    st.stop()

# Fonction pour lire le contenu d'un fichier PDF
def read_pdf(file):
    pdfreader = PdfReader(file)
    raw_text = ''
    for page in pdfreader.pages:
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

# Interface utilisateur Streamlit
st.title("Analyse de PDF avec OpenAI et LangChain")

uploaded_file = st.file_uploader("Téléchargez un fichier PDF", type="pdf")

if uploaded_file:
    raw_text = read_pdf(uploaded_file)
    
    # Split du texte basé sur des caractères spécifiques
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)
    
    # Téléchargement des embeddings de OpenAI langage compris par le nlp c'est transformé en nombre
    embeddings = OpenAIEmbeddings(api_key=openai_api_key)
    
    # Stocker les textes splittés, récupérer les embeddings et les stocker dans le vectorstore FAISS
    document_search = FAISS.from_texts(texts, embeddings)
    
    # Chargement de la chaîne de question-réponse
    llm = OpenAI(api_key=openai_api_key)  # Initialise the OpenAI LLM
    chain = load_qa_chain(llm, chain_type="stuff")
    
    query = st.text_input("Posez une question sur le contenu du PDF:")
    
    if query:
        docs = document_search.similarity_search(query)
        answer = chain.run(input_documents=docs, question=query)
        st.write("Réponse:", answer)
