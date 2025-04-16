from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Message(BaseModel):
    id: int
    sender: str
    text: str

messages_db: List[Message] = []

@router.post("/messages/")
def send_message(message: Message):
    messages_db.append(message)
    return message

@router.get("/messages/")
def get_messages():
    return messages_db
