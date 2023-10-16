from fastapi import FastAPI

from src.questions.router import router_questions

app = FastAPI(
    title='BewiseJuniorTestTask',
    description='Микросервис вопросов с викторин',
    version='1.0.0',
)

origins = [
    "http://localhost:3000",
]

app.include_router(router_questions)