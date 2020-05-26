FROM python:3.7.1

ENV PYTHONDONTWRITEBYTECODE=True

RUN mkdir -p /usr/src
WORKDIR /usr/src

ADD ./requirements.txt /usr/src/requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt

ADD . /usr/src