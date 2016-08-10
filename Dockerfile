FROM python:3.5-slim

MAINTAINER Bence Nagy <bence@underyx.me>

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "gunicorn", "zenbot:app", "--bind", ":80", "--worker-class", "aiohttp.worker.GunicornWebWorker" ]
EXPOSE 80
