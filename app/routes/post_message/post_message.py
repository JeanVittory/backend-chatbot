from fastapi import APIRouter, Depends, HTTPException
from app.middlewares.validate_tokens import validate_tokens
from app.models.message import Message
from app.services.send_message import send_message

router = APIRouter(prefix="/message", tags=["message"])

@router.post("/", status_code=200)
async def post_message(message: Message = Depends(validate_tokens)):
    try:
        ai_response = send_message(message.content)
        return {"message": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))