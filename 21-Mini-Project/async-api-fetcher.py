# Updated Async API fetcher using working public APIs

import asyncio
import aiohttp
from rich import print_json

async def fetch_json(session, url):
    # Generic async fetcher for JSON APIs
    print(f"Fetching: {url}")

    async with session.get(url) as response:
        data = await response.json()
        print(f"Done: {url}")
        return data


async def main():
    async with aiohttp.ClientSession() as session:

        # ---------------------------------------------
        # WORKING PUBLIC APIS
        # ---------------------------------------------

        urls = {
            "joke": "https://official-joke-api.appspot.com/random_joke",
            "dog": "https://dog.ceo/api/breeds/image/random",
            "cat_fact": "https://catfact.ninja/fact"
        }

        # ---------------------------------------------
        # CREATE CONCURRENT TASKS
        # ---------------------------------------------
        tasks = {}
        for key, url in urls.items():
            tasks[key] = asyncio.create_task(fetch_json(session, url))

        print("All API requests started...\n")

        # ---------------------------------------------
        # WAIT FOR ALL TASKS
        # ---------------------------------------------
        results = {}
        for key, task in tasks.items():
            results[key] = await task

        print("\n--- RESULTS ---\n")

        print_json(data=results,sort_keys=True)


asyncio.run(main())