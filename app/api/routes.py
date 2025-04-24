from fastapi import APIRouter
from .endpoints import chat

api_router = APIRouter()

api_router.include_router(
    chat.router, prefix="/api", tags=["Chat"]
)