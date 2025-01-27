import uvicorn
from fastapi import FastAPI
from sessions import create, all_user, user_by_id
from schemas import User
from chat import chat


app = FastAPI()

app.include_router(chat)

@app.post("/register")
def register(user: User):
    user = create(username=user.username, email=user.email, password=user.password)
    return user

@app.get("/users")
def get_users():
    users = all_user()
    return users

@app.get("/user/{id}")
def user_id(id):
    try:
        user = user_by_id(id)
        print(user)
        return user
    except Exception as e:
        return e


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
