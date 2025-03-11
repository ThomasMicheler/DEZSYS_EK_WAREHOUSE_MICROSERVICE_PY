from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = {}

@app.post("/signup")
def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = user
    print("User " + user.username + " created.")
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: User):
    print("Login request: " + user.username)
    if user.username not in users_db or users_db[user.username].password != user.password:
        print("Login request failed!")
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}
