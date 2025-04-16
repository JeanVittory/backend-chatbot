from google.cloud import firestore
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from app.config.dotenv import PROJECT_ID, COLLECTION_NAME
import datetime
import uuid

def get_messages(user_id:str):
    client = firestore.Client(project=PROJECT_ID)
    chat = FirestoreChatMessageHistory(client=client, session_id=user_id, collection=COLLECTION_NAME)
    if not chat.messages: 
        system_message = SystemMessage(content="You're a useful and friendly assitant. Answer clearly and precisely.")
        ai_message = AIMessage(content="Hello, how can I help you today?", additional_kwargs={"date_time": datetime.datetime.now(), "id": uuid.uuid4()})
        chat.add_messages([system_message, ai_message])
    chat_history = chat.messages
    result = []
    for message in chat_history:
        if message.type == "system": continue
        result.append({
            "id":message.additional_kwargs.get("id"),
            "content": message.content,
            "type": message.type,
            "date_time": message.additional_kwargs.get("date_time"),
        })
    return result