FROM python:3.12-slim

LABEL authors="Laura Carvalho"

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]
