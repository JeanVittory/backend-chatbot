from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from app.utils.numeric_parser import parser
from app.config.dotenv import GROQ_API_KEY, PROJECT_ID, SESSION_ID, COLLECTION_NAME,TEMPERATURE_MODEL, MODEL_NAME, MAX_TOKENS 
import datetime

def send_message(message:str):
    client = firestore.Client(project=PROJECT_ID)
    chat = FirestoreChatMessageHistory(client=client, session_id=SESSION_ID, collection=COLLECTION_NAME)
    temperature_parsed = parser(TEMPERATURE_MODEL)
    max_tokens_parsed = parser(MAX_TOKENS)
    model = ChatGroq(api_key=GROQ_API_KEY, temperature=temperature_parsed, model=MODEL_NAME, max_tokens=max_tokens_parsed)
    
    if not chat.messages: 
        system_message = SystemMessage(content="You're a useful and friendly assitant. Answer clearly and precisely.")
        ai_message = AIMessage(content="Hello, how can I help you today?", additional_kwargs={"date_time": datetime.datetime.now()})
        chat.add_messages([system_message, ai_message])
    
    user_message = HumanMessage(content=message, additional_kwargs={"date_time": datetime.datetime.now()})
    chat.add_user_message(user_message)
    ai_response = model.invoke(chat.messages)
    ai_message = AIMessage(content=ai_response.content, additional_kwargs={"date_time": datetime.datetime.now()})
    chat.add_ai_message(ai_message)
    
    return ai_response.content