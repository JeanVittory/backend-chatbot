from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.middlewares.validate_tokens import validate_tokens
from app.services.send_message import send_message

router = APIRouter()

@router.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept() 
    try:
        while True:
            message = await websocket.receive_text()
            validate_tokens(message)
            ai_response = send_message(message)
            await websocket.send_text(ai_response)
    except WebSocketDisconnect:
        websocket.send_text("WebSocket disconnected")
    except Exception as e:
        websocket.send_text(f"An error occurred: {str(e)}")
    finally:
        await websocket.close()