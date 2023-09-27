FROM python:3.10-alpine

WORKDIR /usr/src/django_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/src/django_app/entrypoint.sh"]