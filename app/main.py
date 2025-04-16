from fastapi import FastAPI
from .routes.post_message import post_message
from .routes.get_messages import get_message
from .routes.health import health_check
from .routes.websocket import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplaza "*" con tu dominio frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_check.router)
app.include_router(post_message.router)
app.include_router(get_message.router)
app.include_router(router)
