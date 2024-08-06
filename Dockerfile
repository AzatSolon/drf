FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . /app/

# Применение миграций
#RUN python manage.py migrate

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]