# Backend with Python and FastAPI

Exercises and examples from the MoureDev Pro course "Backend Python".

## Purpose

This folder contains a simple FastAPI backend used to learn:

- API routing and request handling
- Pydantic models and validation
- Authentication flows (basic + JWT)
- Static files
- Project structure for small APIs

## Structure

- `main.py`: FastAPI app entry point
- `routers/`: API route modules
- `static/`: static assets (served by the app)
- `resources/`: downloaded course files used as references/templates

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

## Usage

Start the development server:

```bash
python -m uvicorn main:app --reload
```

Open the interactive docs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Basic endpoints:

- `GET /` returns a hello message
- `GET /url` returns a sample URL
- `GET /static/...` serves files from `static/`

## Dependencies

Key dependencies used in this project:

- `fastapi`
- `uvicorn`
- `python-jose`
- `passlib[bcrypt]`
- `python-multipart`
- `bcrypt<4.0.0`

## Notes

This folder follows the MoureDev Pro course "Backend Python":
https://campus.mouredev.pro/courses/backend-python

---

Happy coding!
