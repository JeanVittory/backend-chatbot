from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from app.utils.numeric_parser import parser
from app.config.dotenv import GROQ_API_KEY, PROJECT_ID, SESSION_ID, COLLECTION_NAME,TEMPERATURE_MODEL, MODEL_NAME, MAX_TOKENS 

def send_message(message:str):
    client = firestore.Client(project=PROJECT_ID)
    chat = FirestoreChatMessageHistory(client=client, session_id=SESSION_ID, collection=COLLECTION_NAME)
    temperature_parsed = parser(TEMPERATURE_MODEL)
    max_tokens_parsed = parser(MAX_TOKENS)
    model = ChatGroq(api_key=GROQ_API_KEY, temperature=temperature_parsed, model=MODEL_NAME, max_tokens=max_tokens_parsed)
    
    chat.add_user_message(message)
    ai_response = model.invoke(chat.messages)
    ai_message = AIMessage(ai_response.content)
    chat.add_ai_message(ai_message)
    
    return ai_response.content