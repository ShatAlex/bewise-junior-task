FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /fastapi_app

COPY . .
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --upgrade pip && pip install -r requirements.txt


RUN chmod +x docker/run.sh
RUN chmod +x docker/tmp.sh