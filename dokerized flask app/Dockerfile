# ---------- Stage 1: Builder ----------
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=/install -r requirements.txt

# ---------- Stage 2: Final Image ----------
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /install /usr/local/lib/python3.10/site-packages

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
