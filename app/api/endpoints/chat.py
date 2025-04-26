from fastapi import APIRouter
from ...services.llm import ( generate_response)
from pydantic import BaseModel

router = APIRouter()

class Query(BaseModel):
    query: str


@router.post("/chat")
def chat(query: Query):
    response = generate_response(query.query)

    return {"message": response}