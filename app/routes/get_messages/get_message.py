from fastapi import APIRouter, HTTPException
from app.services.get_messages import get_messages

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/", status_code=200)
async def get_message():
    try:
        history_messages = get_messages()
        return {"message": history_messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))