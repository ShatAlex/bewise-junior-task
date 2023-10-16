from datetime import datetime
from pydantic import BaseModel


class Question(BaseModel):
    id: int
    question_id: int
    text_question: str
    text_answer: str
    date: datetime

    class Config:
        orm_mode = True
