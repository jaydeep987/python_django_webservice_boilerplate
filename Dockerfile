# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Set App Env to production
ENV APP_ENV=prod

ENV DB_HOST="$DB_HOST"
ENV DB_NAME="$DB_NAME"
ENV DB_USER="$DB_USER"
ENV DB_PASSWORD="$DB_PASSWORD"
ENV DB_PORT="$DB_PORT"
ENV DB_SCHEMA_NAME="$DB_SCHEMA_NAME"
ENV ALLOWED_HOST="$ALLOWED_HOST"

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./script/entry-point.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entry-point.sh

WORKDIR /app
ADD . /app

RUN mkdir -p /app/root/static
# Collect static files
RUN python manage.py collectstatic

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

ENTRYPOINT [ "/usr/local/bin/entry-point.sh" ]
