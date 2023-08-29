# образ на основе которого создаём контейнер
FROM python:3.10-alpine

# рабочая директория внутри контейнера
WORKDIR /usr/src/django_app

# переменные окружения для python
# Python не будет создавать файлы кэша .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# не помещает в буфер потоки stdout и stderr
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
# копируем файл requirements.txt из директории где лежит Dockerfile
# в рабочий каталог контейнера /usr/src/django_app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки из директории где лежит Dockerfile
# в рабочий каталог контейнера /usr/src/django_app
#COPY . .

EXPOSE 5000
#CMD gunicorn stocks_products.wsgi -b 0.0.0.0:8000