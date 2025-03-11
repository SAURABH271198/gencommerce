from fastapi import FastAPI
from .chatbot import router as chatbot_router
from .voice_search import router as voice_router
from .image_search import router as image_router

app = FastAPI()

app.include_router(chatbot_router, prefix="/ai")
app.include_router(voice_router, prefix="/ai")
app.include_router(image_router, prefix="/ai")

@app.get("/")
def root():
    return {"message": "Gen-Com-AI is running"}

