FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir poetry~=1.1.6 &&\
  poetry install --no-root &&\
  poetry config virtualenvs.create false &&\
  rm -rf ~/.cache/pypoetry/{cache,artifacts}

COPY . /app/
RUN poetry install &&\
  rm -rf ~/.cache/pypoetry/{cache,artifacts}

CMD [ "gunicorn", "zenbot", "--bind=:80", "--worker-class=aiohttp.worker.GunicornWebWorker" ]
EXPOSE 80
