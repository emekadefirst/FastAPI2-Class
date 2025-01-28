import asyncio
import http.client
from bs4 import BeautifulSoup

DOMAIN = "arise.tv"
PATH = "category/business/"


async def fetch():
    page_number = 0
    while True:
        yield page_number  # Async generator producing values
        page_number += 1
        conn = http.client.HTTPConnection(DOMAIN)
        conn.request("GET", f"{PATH}/page/{page_number}/")
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            soup = BeautifulSoup(
                data, "html.parser"
            )  # Use `data` instead of `response.content`
            for article in soup.find_all("article"):
                title = article.find("h3")
                if title:
                    print(title.text.strip())
                time = article.find("span", {"class": "date-container"})
                if time:
                    print(time.text.strip())
                print("\n")
        conn.close()


async def main():
    async for _ in fetch():  # Consume the async generator
        pass


# Run the main coroutine
asyncio.run(main())
