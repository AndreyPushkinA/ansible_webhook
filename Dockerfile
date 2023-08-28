FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 libffi-dev && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y git

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app
