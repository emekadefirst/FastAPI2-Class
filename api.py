import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


key = os.getenv("paystack")
# paystack api
url = "https://api.paystack.co/transaction/initialize"
headers = {"Authorization": f"Bearer {key}"}
data = {
    "email": "laitankorede@gmail.com",
    "amount": "100000"
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())


# product api
url = "https://dummyjson.com/products"
response = requests.get(url)
products = response.json()
print("Check out what we have")
for product in products["products"]:
    item = product["title"]
    price = product["price"]
    print(f"We have {item} which goes for ${price}")
