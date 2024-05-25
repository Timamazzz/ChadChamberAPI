#!/bin/sh

# Create database migrations
python manage.py makemigrations --noinput

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Run your custom command (initdb)
python manage.py initdb

# Start Gunicorn
exec "$@"
