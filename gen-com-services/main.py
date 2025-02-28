from fastapi import FastAPI
from .api.v1 import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
