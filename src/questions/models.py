from datetime import datetime

from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP

from src.database import Base

metadata = MetaData()


class Question(Base):
    __tablename__ = "questions"

    id: int = Column(Integer, primary_key=True)
    question_id: int = Column(Integer, nullable=False)
    text_question: str = Column(String, nullable=False)
    text_answer: str = Column(String, nullable=False)
    date: datetime = Column(TIMESTAMP, nullable=True)
