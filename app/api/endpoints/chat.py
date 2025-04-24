from fastapi import APIRouter
from ...services.llm import ( generate_response)

router = APIRouter()

@router.post("/chat")
def chat(query):
    response = generate_response(query)

    return {"message": response}