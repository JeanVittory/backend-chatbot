from fastapi import Request, HTTPException
from app.models.message import Message
from app.config.dotenv import MAX_TOKENS

async def validate_tokens(request:Request):
    try:
        json = await request.json()
        body = Message(**json)
        if len(body.content) > int(MAX_TOKENS):
            raise HTTPException(status_code=400, detail="Too many tokens found.")
        return body
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))