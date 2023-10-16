# Bewise Junior Test Task
___
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi)
![PyPI](https://img.shields.io/pypi/v/FastAPI?label=fastapi&color=gree)
![PyPI](https://img.shields.io/pypi/v/sqlalchemy?label=sqlalchemy&color=yellow)
![PyPI](https://img.shields.io/pypi/v/alembic?label=alembic&color=pink)
![PyPI](https://img.shields.io/pypi/v/asyncpg?label=asyncpg&color=red)
![PyPI](https://img.shields.io/pypi/v/pydantic?label=pydantic&color=purple)

## :sparkles: Описание проекта
___
REST API, позволяющий сохранять в базе данных вопросы полученные из внешнего API (https://jservice.io/api/random).

Если пришедший из API вопрос уже есть в БД, отправляется повторные запросы, пока не будет получен уникальный.

Для проекта написаны Dokcerfile и Makefile. Для сохранностит данных при рестарте используются volume-ы.

## :clipboard: Использование
Если приложение собирается впервые используйте:
```
make build
```
Для стандартного запуска уже собранного приложения используйте:
```
make run
```
Для подключения к БД Postgres используйте:
```
make db_connect
```
Подключени к БД Postgres напрямую через консоль:
```
docker-compose exec db bash
```
___

## :pushpin: API Endpoints

### QUESTIONS
Группа эндпоинтов для работы с вопросами: создать новые вопросы, получить список всех вопросов, получить последний добавленный вопрос
##### POST - /questions
Эндпоинт для создания новых вопросов

Example Input:
```
{
    "questions_num": 1
} 
```
Example Response:
```
{
  "last_question": {
    "id": 1,
    "question_id": 7169,
    "text_answer": "Blindness",
    "text_question": "At 1980 Olympics for disabled in Holland, Trisha Zorn set world swimming records with this disability",
    "date": "2022-12-30T00:00:00"
  }
}
```
##### GET - /questions
Эндпоинт для получения всех вопросов

Example Response:
```
{
  "data": [
    {
      "id": 1,
      "question_id": 7169,
      "text_answer": "Blindness",
      "text_question": "At 1980 Olympics for disabled in Holland, Trisha Zorn set world swimming records with this disability",
      "date": "2022-12-30T00:00:00"
    },
    {
      "id": 2,
      "question_id": 95353,
      "text_answer": "a billion",
      "text_question": "If a gigawatt you see, this is the number of watts you get",
      "date": "2022-12-30T00:00:00"
    }
  ]
}
```

##### GET - /questions/last
Эндпоинт для получения последнего вопроса

Example Response:
```
{
  "id": 2,
  "question_id": 95353,
  "text_answer": "a billion",
  "text_question": "If a gigawatt you see, this is the number of watts you get",
  "date": "2022-12-30T00:00:00"
}
```
