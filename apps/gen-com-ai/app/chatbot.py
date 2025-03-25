from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
from .config import settings


class ChatRequest(BaseModel):
    message: str

router = APIRouter()

client = openai.OpenAI(api_key=settings.open_ai_key)

@router.post("/chat")
async def chatBot( body : ChatRequest):
    try:
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": body.message}
        ])
    except Exception:
        raise HTTPException(status_code=500, detail="your limit expired")
    
    return {"response": response["choices"][0]["message"]["content"]}
