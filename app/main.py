from fastapi import FastAPI
from app import health
from app.api import chat

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.include_router(health.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Neco ayakta 👋"}
