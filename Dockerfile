# образ на основе которого создаём контейнер
FROM python:3.12-slim

# рабочая директория внутри проекта
WORKDIR /var/www/ChadChamberAPI

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .

# добавляем исполняемый флаг для entrypoint.sh
RUN chmod +x entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
