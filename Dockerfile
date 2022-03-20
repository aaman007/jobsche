FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 0

WORKDIR /app

COPY requirements.txt /app/

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && pip install -r requirements.txt --no-cache-dir \
    && apk del build-deps

COPY . /app/

CMD flask run --host=0.0.0.0