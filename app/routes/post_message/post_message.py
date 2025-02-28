from fastapi import APIRouter, Depends
from app.middlewares.validate_tokens import validate_tokens
from app.models.message import Message

router = APIRouter(prefix="/message", tags=["message"])

@router.post("/" )
async def post_message(message: Message = Depends(validate_tokens)):
    print("Hello from handler", message.message)
    return {"message": "Message received"}
