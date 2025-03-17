from fastapi import FastAPI
from .routes.post_message import post_message
from .routes.get_messages import get_message
from .routes.websocket import router

app = FastAPI()
app.include_router(post_message.router)
app.include_router(get_message.router)
app.include_router(router)
