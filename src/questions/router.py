import datetime

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.questions.models import Question
from sqlalchemy import insert, select, desc

import httpx
import asyncio
import json

router_questions = APIRouter(
    prefix='/questions',
    tags=['Questions']
)

URL = "https://jservice.io/api/random"


@router_questions.post('/')
async def get_questions(questions_num: int, session: AsyncSession = Depends(get_async_session)):
    """ Эндпоинт получения новых вопросов """
    last_question = await get_last_question(session)

    values = []

    while questions_num != 0:
        used_id = await get_used_ids(session)

        questions = await get_questions_from_api(questions_num)
        objects = [(q['id'], q['question'], q['answer'], q['created_at']) for q in json.loads(questions[0])]

        questions_num = 0

        for id, question, answer, created_at in objects:
            if id not in used_id:
                values.append(
                    {'question_id': id, 'text_question': question, 'text_answer': answer, 'date': datetime.datetime.strptime(
                        created_at, "%Y-%m-%dT%H:%M:%S.%fZ").date()})
            else:
                questions_num += 1

    stmt = insert(Question).values(values)
    await session.execute(stmt)
    await session.commit()

    return {
        "last_question": last_question
    }


async def get_questions_from_api(questions_num: int):
    """ Метод получения вопросов из внешнего API """
    data = await task(questions_num)
    return data


@router_questions.get('/get_all_questions')
async def get_all_questions(session: AsyncSession = Depends(get_async_session)):
    """ Эндпоинт получения всех вопросов из БД """
    query = select(Question)
    result = await session.execute(query)
    data = []
    for item in result.all():
        data.append(item[0].__dict__)
    return {
        'data': data,
    }


async def task(questions_num):
    """ Вспомогательный метод создания запроса на URL внешнего API """
    async with httpx.AsyncClient() as client:
        result = await asyncio.gather(request(client, questions_num))
        return result


async def request(client, questions_num):
    """ Вспомогательный метод получения ответа из внешнего API """
    response = await client.get(URL + f'?count={str(questions_num)}')
    return response.text


@router_questions.get('/last')
async def get_last_question(session: AsyncSession = Depends(get_async_session)):
    """ Эндпоинт получения последнего вопроса из БД """
    quary = select(Question).order_by(desc(Question.id))
    result = await session.execute(quary)
    first = result.first()
    if first is None:
        return None
    last_question = first[0].__dict__
    return last_question


async def get_used_ids(session: AsyncSession = Depends(get_async_session)):
    """ Метод получения существующих в БД id вопросов """
    quary = select(Question)
    result = await session.execute(quary)
    ids = []
    for item in result.all():
        ids.append(item[0].__dict__['question_id'])
    return ids
