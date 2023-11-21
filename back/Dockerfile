FROM python:3.11.1-slim

WORKDIR /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY back/requirements.txt requirements.txt
RUN apt-get update \
    && apt-get -y install apt-transport-https libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

COPY . .
