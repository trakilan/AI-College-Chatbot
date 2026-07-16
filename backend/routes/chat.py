from fastapi import APIRouter
from models.chat_models import ChatRequest, ChatResponse
from chatbot import get_chat_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = get_chat_response(request.question)

    return ChatResponse(answer=answer)