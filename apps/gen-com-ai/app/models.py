from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def chatBot():
    return { "messgae": 'chat bot will run from heer'}
