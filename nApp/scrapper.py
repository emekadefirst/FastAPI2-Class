import asyncio
import requests
import threading
from bs4 import BeautifulSoup


base = "https://www.arise.tv"
path = "category/business/"


async def fetch():
    n = list(range(217))
    for number in n:
        response = requests.get(f"{base}/{path}/page/{number}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            for data in soup.find_all("article"):
                title = data.find("h3")
                print(title.text.strip())
                time = data.find("span", {"class": "date-container"})
                print(time.text.strip())
                print("\n")


async def main():
    event = await fetch()
    task = threading.Thread(target=event) # setting the function on a thread
    print(task.start())

asyncio.run(main())
