from google.cloud import firestore
from app.config.dotenv import PROJECT_ID, COLLECTION_NAME

def validate_user(user_id:str):
    client = firestore.Client(project=PROJECT_ID)
    doc_ref = client.collection(COLLECTION_NAME).document(user_id)
    doc_exists = doc_ref.get().exists
    return doc_exists