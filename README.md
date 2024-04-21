# Medical-Chatbot-using-Llama-2-LLM

## Running steps:

Clone the repository

```
Project repo: https://github.com/canerkaraoglu/Medical-Chatbot-using-Llama-2-LLM
```

### Step 01 - Create a conda environment after opening the repository

```
conda create -n mchatbot python=3.8 -y
```

```
conda activate mchatbot
```

### Step 02 - Install the requirements using `requirements.txt`

```
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials:

```
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Download the Llama 2 Model:
```
llama-2-7b-chat.ggmlv3.q4_0.bin
```

## From the following link:

```
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
