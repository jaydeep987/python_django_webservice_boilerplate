#!/bin/bash

# Create database migration
python manage.py makemigrations

# Apply database migration
python manage.py migrate

# Finally start server
gunicorn --bind 0.0.0.0:8000 root.wsgi
