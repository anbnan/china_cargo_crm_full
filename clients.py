from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Client(BaseModel):
    id: int
    name: str
    phone: str
    email: str

clients_db: List[Client] = []

@router.post("/clients/")
def create_client(client: Client):
    clients_db.append(client)
    return client

@router.get("/clients/")
def list_clients():
    return clients_db
