import os
import json
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field

load_dotenv()

class Grade(BaseModel):
    name: str 
    teacher_name: str
    students: list = []

class Payment(BaseModel):
    id: int
    email: str


class User(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None


app = FastAPI()

key = os.getenv("paystack")
# paystack api


def initiate_payment(email, amount):
    url = "https://api.paystack.co/transaction/initialize"
    headers = {"Authorization": f"Bearer {key}"}
    data = {"email": email, "amount": amount *100}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    data = response.json()
    # payment_url = data["data"]["authorization_url"]

    return data


def product_id(id):
    
    product_url = f"https://dummyjson.com/products/{id}"
    response = requests.get(product_url)
    if response.status_code == 200:
        products = response.json()
        return products['price'] *1635


def all_product():
    product_url = "https://dummyjson.com/products"
    response = requests.get(product_url)
    if response.status_code == 200:
        products = response.json()
        items = []
        for product in products["products"]:
            id = product["id"]
            name = product["title"]
            price = product["price"]
            item = {"id": id, "name": name, "price": price * 1635//1}
            items.append(item)
    return items


@app.get("/products")
def all():
    return all_product()

@app.post("/product/pay")
def pay_details(pay : Payment):
    prod_id = pay.id
    price = product_id(prod_id)
    email = pay.email
    print(email, price//1)
    return initiate_payment(email, price)


@app.post("/user/signup")
def create_user(user: User):
    username = user.username
    return f"{username} has beening registered"


@app.post("/class/create")
async def  add(grade: Grade):
    return "Class Has been created"


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
