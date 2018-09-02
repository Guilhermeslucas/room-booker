FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt && \
    python3 manage.py migrate

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
