FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir requests

CMD ["python", "webcheck.py"]
