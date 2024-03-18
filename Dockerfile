FROM python:3.8-slim

RUN pip install fastapi uvicorn redis huey

COPY ./main.py /app/main.py

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
