FROM python:3.8-slim
ENV PORT=8000
COPY requirements.txt /
RUN pip install -q -r requirements.txt
COPY ./app /app
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
