from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI(title="Decode Labs Project 1 - Rest API")
user_db = []


class User(BaseModel):
    id: int
    name: str
    email: str


@app.get("/users", status_code=200)
def get_users():
    return {" count": len(user_db), "data": user_db}


@app.post("/users", status_code=201)
def create_user(user: User):
    user_db.append(user.dict())
    return {"message": "User created successfully", "data": user.dict()}


@app.get("/users/{user_id}", status_code=200)
def get_user(user_id: int):
    for u in user_db:
        if u["id"] == user_id:
            return {"data": u}
    return {"message": "User not found", "code": 404}
