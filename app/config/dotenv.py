from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
TEMPERATURE_MODEL = os.getenv('TEMPERATURE_MODEL')
MODEL_NAME = os.getenv('MODEL_NAME')
MAX_TOKENS = os.getenv('MAX_TOKENS')