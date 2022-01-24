FROM python:3.10.2-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir poetry~=1.1.6 &&\
  poetry config virtualenvs.create false &&\
  poetry install --no-root &&\
  rm -rf /root/.cache/* /tmp/* &&\
  find / \( -name '*.pyc' -o -path '*/__pycache__*' \) -delete

COPY . /app/
RUN poetry install &&\
  rm -rf /root/.cache/* /tmp/* &&\
  find / \( -name '*.pyc' -o -path '*/__pycache__*' \) -delete

CMD [ "gunicorn", "zenbot", "--bind=:80", "--worker-class=aiohttp.worker.GunicornWebWorker" ]
EXPOSE 80
