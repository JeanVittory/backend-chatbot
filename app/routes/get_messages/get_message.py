from fastapi import APIRouter, HTTPException
from app.services.get_messages import get_messages

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/{userId}", status_code=200)
async def get_message(userId:str):
    try:
        history_messages = get_messages(userId)
        return {"message": history_messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))