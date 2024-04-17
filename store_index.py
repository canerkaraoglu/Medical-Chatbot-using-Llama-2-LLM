"""Converting the text into vectors and storing into Pinecone"""

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

import os
from src.helper import load_pdf, text_split, download_huggingface_embeddings


# Load the virtual environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

# print("PINECONE_API_KEY: ", PINECONE_API_KEY)
# print("PINECONE_API_ENV: ", PINECONE_API_ENV)

# Extract the raw data, split the text into chunks, and download the embedding model

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_huggingface_embeddings()

# Create the Pinecone instance
Pinecone(api_key=os.environ.get("PINECONE_API_KEY"), 
         environment=os.environ.get("PINECONE_API_ENV"))

index_name="med-chatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)