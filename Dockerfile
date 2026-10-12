FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY src/app.py .
COPY src/db_mitigation/ ./db_mitigation/
COPY src/templates/ ./templates/

EXPOSE 5000
CMD ["flask", "--app", "app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
