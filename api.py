import os
import json
import requests
from app import all_product, product_id

# print(all_product())
print(product_id(1))


# product_url = "https://dummyjson.com/products"

# response = requests.get(product_url)

# if response.status_code == 200:
#     products = response.json()
#     items = []
#     for product in products["products"]:
#         name = product["title"]
#         price = product["price"]
#         item = {
#             "name": name,
#             "price": price * 1635
#         }
#         return items.append(item)
# return items
