from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.middlewares.validate_tokens import validate_tokens
from app.services.validate_user import validate_user
from app.services.send_message import send_message

router = APIRouter()

@router.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept() 
    try:
        user_id = await websocket.receive_text()
        is_a_user_valid = validate_user(user_id)
        if not is_a_user_valid:
            raise WebSocketDisconnect() 
        
        while True:
            message = await websocket.receive_text()
            await validate_tokens(message)
            ai_response = send_message(message, user_id)
            await websocket.send_text(ai_response)
    except WebSocketDisconnect as e:
        await websocket.send_text("WebSocket disconnected", e)
    except Exception as e:
        await websocket.send_text(f"An error occurred: {str(e)}")
    finally:
        await websocket.close()