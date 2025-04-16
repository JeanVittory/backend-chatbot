# Chat Bot 
A configurable chatbot server built with FastAPI and LangChain, designed to seamlessly integrate multiple LLM (Large Language Model) providers via environment variables. This API allows dynamic switching between AI models (e.g., Groq, Mistral, Anthropic Claude, DeepSeek, OpenAI, OLLAMA and Huggingface) making it ideal for testing, prototyping, and production deployments.

## Tech
- Python3.12.9 - Python is a high-level, general-purpose programming language.
- Fastapi - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints..
- Langchain - LangChain is a framework for developing applications powered by large language models (LLMs).
- Firestore - Cloud Firestore is a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud.
- Poetry - Python packaging and dependency management


## Installation

To run the application we encourage to use the 3.12.9 python version and then follow these steps:

```sh
git clone git@github.com:JeanVittory/backend-chatbot.git
cd backend-chatbot
poetry env use python3.12
poetry env info # it has to show you python: 3.12.9
poetry shell 
poetry install 
uvicorn app.mai:app --reload
```
Once your project is running, you can test the endpoint http://127.0.0.1:8000/health to verify the application is working properly.

Locate a file called `.env.example` in your project's root directory it will contain these values.

```sh
GROQ_API_KEY= # If you choose to use GROQ, you can place the API KEY here. Replace this value with your favorite LLM's API KEY.
PROJECT_ID= # The project ID in your Google Cloud Firestore account.
COLLECTION_NAME= # Your Firestore collection name.
TEMPERATURE_MODEL= # How much randomness you want in your LLM's answers
MODEL_NAME= # THe model name that you want to use
MAX_TOKENS= # Maximum response length (in tokens) for your model
```

You will need an Google Cloud Firestore account please watch this [video](https://www.youtube.com/watch?v=TW02hwhBvo4&ab_channel=TownCoder) if you have any question 

# IMPORTANT

If you need any help with the installation, don’t hesitate to leave me a message or contact me vittory.dev@gmail.com