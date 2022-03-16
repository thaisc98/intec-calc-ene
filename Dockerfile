FROM python:alpine3.14

ENV PORT=8000

WORKDIR /app  

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn api:app --host 0.0.0.0 --port $PORT