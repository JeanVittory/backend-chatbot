from fastapi import FastAPI
from .routes.post_message import post_message

app = FastAPI()
app.include_router(post_message.router)
