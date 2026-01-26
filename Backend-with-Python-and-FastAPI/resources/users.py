from fastapi import FastAPI
from pydantic import BaseModel

# Inicia el server: uvicorn users:app --reload

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
    User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)
]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]


@app.get("/users")
async def users():
    return users_list
