# pull official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt