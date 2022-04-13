# pull official base image
FROM python:3.8.3-slim
#FROM debian-debian-bullseye-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
##
# install psycopg2
RUN apt update \
    && apt install gcc python3-dev -y
##
RUN apt install python3-venv python3-pip -y
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /code/

WORKDIR /code/problog
# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
