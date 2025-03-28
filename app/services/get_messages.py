from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from app.config.dotenv import PROJECT_ID, SESSION_ID, COLLECTION_NAME

def get_messages(userId:str):
    client = firestore.Client(project=PROJECT_ID)
    chat = FirestoreChatMessageHistory(client=client, session_id=userId, collection=COLLECTION_NAME)
    chat_history = chat.messages
    result = []
    for message in chat_history:
        result.append({
            "id":message.additional_kwargs.get("id"),
            "content": message.content,
            "type": message.type,
            "date_time": message.additional_kwargs.get("date_time"),
        })
    return result