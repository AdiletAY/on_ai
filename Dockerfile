FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /onai

WORKDIR /onai

COPY requirements.txt . 


RUN pip install  -r ./requirements.txt


COPY . .

RUN chmod +x ./docker/app.sh