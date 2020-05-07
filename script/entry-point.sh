#!/bin/bash

# Collect static files
yes | python manage.py collectstatic

# Create database migration
yes | python manage.py makemigrations

# Apply database migration
yes | python manage.py migrate

# Finally start server
gunicorn --bind 0.0.0.0:8000 root.wsgi
