# pull official base image
FROM python:3.8.3-slim
#FROM debian-debian-bullseye-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
## update
RUN apt update && apt -y upgrade && apt autoclean

RUN apt install -y gcc python3-dev libpq-dev python3-pip 
# install venv
RUN apt install -y python3-venv 
RUN apt install -y curl wget vim tree fabric 
# client postgres
RUN apt install -y postgresql-client wkhtmltopdf
# install Openssh
RUN apt install -y openssh-server
RUN apt clean
##

##
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /code/

WORKDIR /code/problog
# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
