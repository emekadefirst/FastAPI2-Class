# import statements
from fastapi import FastAPI
from pydantic import BaseModel


class UpdateUser(BaseModel):
    name: str

# #  making an instance of FastAPI
app = FastAPI()


user_data = [
    {
        "id": 1,
        "name": "Bravo"
    },
    {
        "id": 2,
        "name": "Charlie"
    },
    {
        "id": 3,
        "name": "Delta"
    }
]

@app.get('/all-users')
def all():
    return {"message": "All users", "data": user_data}

@app.get("/projects/{id}")
def get_project(id: int):
    user = id - 1
    for user in user_data:
        return f"We found {user}"
    return "User not found"


@app.put('/user/{id}')
def update_details(id: int, new_data: UpdateUser):
    user = id - 1
    user_data[user]['name'] = new_data.name
    return user_data

@app.delete('/user/{id}')
def delete(id: int):
    user = id - 1
    user_data.pop(user)
    return {"message": "User deleted", "data": user_data}

@app.post('/add-new-user')
def add(user: UpdateUser):
    new_id = user_data[-1]["id"] + 1
    user_data.append({"id": new_id, "name": user.name})
    return user_data
