FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 libffi-dev python3-pip git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app
