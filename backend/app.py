from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router as chat_router

app = FastAPI(
    title="AI College Chatbot",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "AI College Chatbot Backend Running Successfully"
    }