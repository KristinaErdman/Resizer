FROM python:3.11 AS base
RUN pip install poetry && poetry config virtualenvs.create false
WORKDIR /resizer


COPY pyproject.toml .
COPY poetry.lock .


FROM base AS dev
RUN poetry install

FROM base AS prod
RUN poetry install --without dev
COPY . .
