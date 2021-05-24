FROM python:3.9-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry~=1.1.6 &&\
  poetry install --no-root

COPY . /app/

RUN poetry install

CMD [ "gunicorn", "zenbot", "--bind", ":80", "--worker-class", "aiohttp.worker.GunicornWebWorker" ]
EXPOSE 80
