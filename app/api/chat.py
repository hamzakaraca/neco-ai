from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import generate_reply

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message
    return {"reply": f"Sen şunu dedin: {user_message}"}

from fastapi import APIRouter
from pydantic import BaseModel, Field


router = APIRouter()

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)

@router.post("/chat")
def chat(req: ChatRequest):
    reply = generate_reply(req.message)
    return {"reply": reply}

    