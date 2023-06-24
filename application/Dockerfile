FROM python:3.11.0-alpine

WORKDIR /srv/www/app

COPY pyproject.toml poetry.lock ./
COPY . ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-interaction --no-ansi --no-dev

CMD ["uvicorn", "application.main:app", "--reload", "--host", "0.0.0.0"]