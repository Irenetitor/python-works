# Backend with Python and FastAPI

Exercises and examples from the MoureDev Pro course "Backend Python".

## Purpose

This folder contains a simple FastAPI backend used to learn:

- API routing and request handling
- Pydantic models and validation
- Authentication flows (basic token + JWT)
- MongoDB integration
- Static files
- Project structure for small APIs

## Structure

- `main.py`: FastAPI app entry point and router registration
- `routers/`: API route modules (products, users, auth, MongoDB users)
- `db/`: MongoDB client, models, and schema helpers
- `static/`: static assets (served by the app)
- `resources/`: downloaded course files used as references/templates

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- MongoDB connection string available via `MONGO_URI` (Atlas or local)

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

## Routes

Core:

- `GET /` returns a hello message
- `GET /url` returns a sample URL
- `GET /static/...` serves files from `static/`

Products:

- `GET /products` list products
- `GET /products/{id}` get product by index

Users (in-memory):

- `GET /users` list users
- `GET /users/usersjson` list users as plain JSON
- `GET /users/user/{id}` get user by id (path)
- `GET /users/usersquery/?id=...` get user by id (query)
- `POST /users/user` create user
- `PUT /users/user` update user
- `DELETE /users/user/{id}` delete user

Auth (simple token):

- `POST /auth_users/login` returns a bearer token (the username)
- `GET /auth_users/me` returns the current user (requires token)

Auth (JWT):

- `POST /jwtauth/login` returns a JWT bearer token
- `GET /jwtauth/users/me` returns the current user (requires JWT)

Users (MongoDB):

- `GET /userdb` list users
- `GET /userdb/byquery?id=...|username=...|email=...` find by query
- `GET /userdb/{id}` get user by id
- `POST /userdb` create user
- `PUT /userdb` update user
- `DELETE /userdb/{id}` delete user

## MongoDB Notes

The app reads the connection string from the `MONGO_URI` environment variable and writes to the `test` database.

Example (PowerShell):

```powershell
$env:MONGO_URI="mongodb+srv://<user>:<pass>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
python -m uvicorn main:app --reload
```

Example (macOS/Linux):

```bash
export MONGO_URI="mongodb+srv://<user>:<pass>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
python -m uvicorn main:app --reload
```

If `MONGO_URI` is not set, the app will not be able to connect.

## Deployment (Vercel)

This project is deployed on Vercel using `vercel.json`. Set the `MONGO_URI` environment variable in your Vercel project settings before deploying.

## Dependencies

Key dependencies used in this project:

- `fastapi`
- `uvicorn`
- `pydantic`
- `pymongo`
- `python-jose`
- `passlib`
- `python-multipart`

## Notes

This folder follows the MoureDev Pro course "Backend Python":
https://campus.mouredev.pro/courses/backend-python

---

Happy coding! 🐍
