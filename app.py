"""Creates the app component of the Flask application."""
import sys
sys.path.append(r"C:\Users\caner\Desktop\Medical-Chatbot-using-Llama-2-LLM\src")

from flask import Flask, render_template, jsonify, request
from src import helper
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from pathlib import Path




# Create the Flask app
app = Flask(__name__)

# Load the environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

# Load the embeddings
embeddings = helper.download_huggingface_embeddings()

# Initializing the Pinecone
Pinecone(api_key=os.environ.get("PINECONE_API_KEY"), 
         environment=os.environ.get("PINECONE_API_ENV"))

index_name="med-chatbot"

# Loading the index, because we have created the index in the store_index.py
docsearch=PineconeVectorStore.from_existing_index(index_name, embeddings)

# Load the Llama model using the CTransformers class. LLM is only for use for better response, 
# for enhancing the quality for the response.
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={'max_new_tokens': 512,
                            'temperature': 0.8}
                )

# Create the question-answering object
chain_kwargs = {"prompt": prompt}
qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_kwargs)

# Flask part

# Default route for the Flask
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)