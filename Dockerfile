FROM python:3.11-slim as os-base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_HOME="/opt/poetry"
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y sqlite3

FROM os-base as poetry-base

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN poetry config virtualenvs.create false
RUN apt-get remove -y curl

FROM poetry-base as app-base

ARG APPDIR=/app
WORKDIR $APPDIR/
COPY . .
COPY pyproject.toml ./pyproject.toml
RUN poetry install --no-dev

# EXPOSE 5000
# # CMD [ "poetry", "run", "python", "-m", "flask", "run", "--host=0.0.0.0" ]