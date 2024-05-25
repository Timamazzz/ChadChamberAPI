# Chad Chamber API

## Описание

Chad Chamber API - это проект для управления данными палаты торговли, промышленности, сельского хозяйства, горнодобывающей промышленности и ремесел Чада в России.

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/Timamazzz/ChadChamberAPI
```
2. Создайте файл .env в корне проекта и добавьте в него необходимые переменные окружения:
```bash
SECRET_KEY=
DEBUG=
DJANGO_ALLOWED_HOSTS=

CORS_ALLOW_ALL_ORIGINS=
CORS_ALLOW_CREDENTIALS=

CSRF_TRUSTED_ORIGINS=
CORS_ALLOWED_ORIGINS=

DB_ENGINE=django.db.backends.postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=db
DB_PORT=5432
```

3. Поднимите докер контейнеры
```bash 
docker-compose up --build -d
```

4. Создайте супер пользователя для доступа к админке
```bash
docker-compose exec web python manage.py createsuperuser
```