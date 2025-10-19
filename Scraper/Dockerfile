FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r reqirements.txt

COPY scraper.py .

CMD ["python", "scraper.py"]
