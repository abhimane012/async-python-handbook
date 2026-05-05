# Async Rate Limiter using asyncio (with heavier real public API: GitHub API)

import asyncio
import time
import aiohttp


class AsyncRateLimiter:
    # ---------------------------------------------
    # SIMPLE RATE LIMITER (CONCURRENCY + DELAY CONTROL)
    # ---------------------------------------------
    # Controls:
    # - how many requests can run at the same time (limit)
    # - adds delay between releases (per_seconds)

    def __init__(self, limit, per_seconds):
        self.semaphore = asyncio.Semaphore(limit)
        self.per_seconds = per_seconds

    async def __aenter__(self):
        # acquire slot before making request
        await self.semaphore.acquire()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # release slot after request + wait spacing time
        await asyncio.sleep(self.per_seconds)
        self.semaphore.release()


async def fetch(session, url, limiter, name):
    # ---------------------------------------------
    # FETCH HEAVY REAL API REQUEST (GITHUB API)
    # ---------------------------------------------
    # GitHub API is "heavier" than placeholder APIs:
    # - has headers
    # - rate limits
    # - more realistic network behavior

    async with limiter:
        print(f"[START] {name}")

        async with session.get(url) as response:
            # GitHub returns JSON response
            data = await response.json()

            print(f"[DONE] {name}")

            return {
                "name": name,
                "repo": data.get("full_name"),
                "stars": data.get("stargazers_count"),
            }


async def main():
    # ---------------------------------------------
    # HEAVY REAL PUBLIC API (GITHUB REPOS)
    # ---------------------------------------------
    urls = [
        "https://api.github.com/repos/python/cpython",
        "https://api.github.com/repos/tiangolo/fastapi",
        "https://api.github.com/repos/pallets/flask",
        "https://api.github.com/repos/django/django",
        "https://api.github.com/repos/psf/requests",
    ]

    # ---------------------------------------------
    # RATE LIMIT CONFIG
    # ---------------------------------------------
    # limit=2 → only 2 requests at same time
    # per_seconds=1 → wait 1 second between releases
    limiter = AsyncRateLimiter(limit=1, per_seconds=10)

    # GitHub requires user-agent header
    headers = {
        "User-Agent": "async-rate-limiter-demo"
    }

    async with aiohttp.ClientSession(headers=headers) as session:

        # ---------------------------------------------
        # CREATE TASKS (ALL START IMMEDIATELY)
        # ---------------------------------------------
        tasks = []

        for i, url in enumerate(urls, 1):
            task = asyncio.create_task(fetch(session, url, limiter, f"Repo-{i}"))
            tasks.append(task)

        print("All GitHub requests scheduled...\n")

        # ---------------------------------------------
        # WAIT FOR ALL TASKS
        # ---------------------------------------------
        results = await asyncio.gather(*tasks)

        print("\n--- RESULTS ---\n")

        for r in results:
            print(f"{r['name']} -> {r['repo']} ⭐ {r['stars']}")


# ---------------------------------------------
# EXECUTION TIME MEASUREMENT
# ---------------------------------------------
start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f} sec")