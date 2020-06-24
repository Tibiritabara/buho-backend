FROM python:3.8

ARG DB_USER="postgres"
ARG DB_PASSWORD="987123654"
ARG DB_HOST="172.17.0.1"
ARG DB_PORT="5432"
ARG DB_NAME="test"

ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DB_NAME=${DB_NAME}

RUN python3 -m pip install "pipenv==2018.11.26"

WORKDIR /app/buho

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy --ignore-pipfile --dev

COPY . /app

RUN python manage.py migrate

CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=warning", "buho.wsgi"]
