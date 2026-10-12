# CSC3131 Book Reviews

## Stack choices

- Presentation: HTML rendered with Flask's Jinja templates. This keeps the first interface small and avoids requiring a separate JavaScript frontend build.
- Application: Python with Flask. It is quick to run locally and provides routes for the page, the books list, and a health check.
- Data: SQLite with Flask-SQLAlchemy. SQLite stores the review records in a local database file without requiring a separate database server during early development.

## Run locally

From the repository root, install the dependencies and start the Flask app:

```sh
python -m pip install -r requirements.txt
cd src
python app.py
```

Open `http://127.0.0.1:5000/`. Use the **Get books** button to display records loaded from the database. The database is created and populated with example reviews on first startup.

Health check: `http://127.0.0.1:5000/health` returns `{"status":"ok"}`.

JSON endpoint: `http://127.0.0.1:5000/api/books` returns the book records.

## Run with Docker

Copy `src/.env.example` to `src/.env`, then from the repository root run:

```sh
docker compose up --build
```

Open `http://localhost:8080/`. Stop with Ctrl+C. Dockerfile builds the Python
image; compose.yaml runs it with port 8080, the env file and a persistent SQLite volume.