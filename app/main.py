from fastapi import FastAPI
from .api.routes import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def ping():
    return {"Hello": "World"}