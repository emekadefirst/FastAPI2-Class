import asyncio
import aiohttp
from bs4 import BeautifulSoup

DOMAIN = "https://arise.tv"
PATH = "category/business/"


async def fetch():
    page_number = 1  # Start from page 1
    async with aiohttp.ClientSession() as session:  # Use aiohttp session for HTTPS
        while True:
            url = f"{DOMAIN}/{PATH}page/{page_number}/"
            print(f"Fetching: {url}")

            async with session.get(url) as response:
                if response.status != 200:
                    print(
                        f"Page {page_number} returned status {response.status}. Exiting."
                    )
                    break

                data = await response.text()
                soup = BeautifulSoup(data, "html.parser")

                articles = soup.find_all("article")
                if not articles:  # Stop if no articles are found
                    print(f"No articles found on page {page_number}. Exiting.")
                    break

                for article in articles:
                    title = article.find("h3")
                    if title:
                        print(f"Title: {title.text.strip()}")
                    time = article.find("span", {"class": "date-container"})
                    if time:
                        print(f"Date: {time.text.strip()}")
                    print("\n")

                page_number += 1  # Move to the next page


async def main():
    await fetch()  # Call fetch as a regular coroutine


# Run the main coroutine
asyncio.run(main())
