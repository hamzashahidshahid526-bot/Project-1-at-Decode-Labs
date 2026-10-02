from fastapi import FastAPI, HTTPException
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
    return {"count": len(user_db), "data": user_db}


@app.post("/users", status_code=201)
def create_user(user: User):
    for u in user_db:
        if u["id"] == user.id:
            raise HTTPException(
                status_code=400, detail="User with this ID already exists")

    user_db.append(user.model_dump())
    return {"message": "User created successfully", "data": user.model_dump()}


@app.get("/users/{user_id}", status_code=200)
def get_user(user_id: int):
    for u in user_db:
        if u["id"] == user_id:
            return {"data": u}

    raise HTTPException(status_code=404, detail="User not found")
