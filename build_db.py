import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

documents = []

for file in os.listdir("documents"):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(f"documents/{file}")
        documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="mdr_db"
)

print("Base documental creada.")
