# pyrefly: ignore [missing-import]
import streamlit as st
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

# Résoudre le chemin de l'image relativement au script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

prompt_template="""
Answer the following question based only on the provided context:
<context>
{context}
</context>
<question>
{input}
</question>
"""

llm=ChatOpenAI(model="gpt-4o", temperature=0)

def main():
    st.set_page_config(page_title="RAG", layout="wide")
    st.subheader("Retrieval Augmented generation", divider="blue")
    
    with st.sidebar:
        st.title("Data loader")
        st.image(os.path.join(SCRIPT_DIR, "upm_rag.png"))
        pdf_docs = st.file_uploader(label="Load your pdfs", accept_multiple_files=True)
        if st.button("Submit"):
            if not pdf_docs:
                st.error("⚠️ Veuillez d'abord sélectionner au moins un fichier PDF !")
            else:
                with st.spinner("Chargement et indexation des documents..."):
                    content = ""
                    for pdf in pdf_docs:
                        reader = PdfReader(pdf)
                        for page in reader.pages:
                            text = page.extract_text()
                            if text:
                                content += text

                    if not content.strip():
                        st.error("Aucun texte n'a pu être extrait des PDF fournis.")
                    else:
                        splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                            chunk_size=512, chunk_overlap=16
                        )
                        chunks = splitter.split_text(content)

                        embedding_model = OpenAIEmbeddings()
                        vector_store = Chroma.from_texts(
                            chunks,
                            embedding_model,
                            collection_name="data_collection",
                        )
                        retriever = vector_store.as_retriever(
                            search_kwargs={"k": 5},
                        )

                        st.session_state.retriever = retriever
                        st.success(f"✅ {len(chunks)} chunks indexés avec succès !")
    st.subheader("Chatbot 💬")
    user_question = st.text_input("Posez votre question sur les documents chargés / Ask Your Question")
    if user_question:
        if "retriever" not in st.session_state:
            st.warning("⚠️ Veuillez d'abord charger un ou plusieurs fichiers PDF dans la barre latérale et cliquer sur 'Submit' !")
        else:
            with st.spinner("Recherche et génération de la réponse..."):
                context_docs = st.session_state.retriever.invoke(user_question)
                context_list = [d.page_content for d in context_docs]
                context_text = ". ".join(context_list)
                prompt = prompt_template.replace("{context}", context_text).replace("{input}", user_question)

                resp = llm.invoke(prompt)
                st.markdown("### Réponse :")
                st.write(resp.content)

if __name__ == "__main__":
    main()