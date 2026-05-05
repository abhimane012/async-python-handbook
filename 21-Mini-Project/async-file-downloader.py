# Async file downloader using aiohttp + aiofiles
# Demonstrates fully non-blocking download + async file writing

import asyncio
import time
import aiohttp
import aiofiles


async def download_file(session, url, filename):
    # ---------------------------------------------
    # ASYNC DOWNLOAD FUNCTION
    # ---------------------------------------------
    # This function is fully non-blocking because:
    # - network I/O uses await (aiohttp)
    # - file writing uses aiofiles (async disk I/O)

    print(f"Starting download: {filename}")

    # ---------------------------------------------
    # FETCH DATA FROM NETWORK (NON-BLOCKING)
    # ---------------------------------------------
    async with session.get(url) as response:
        content = await response.read()

    # ---------------------------------------------
    # WRITE FILE ASYNCHRONOUSLY (NON-BLOCKING)
    # ---------------------------------------------
    # aiofiles ensures file writing does NOT block event loop
    async with aiofiles.open(filename, "wb") as f:
        await f.write(content)

    print(f"Completed download: {filename}")


async def main():
    # ---------------------------------------------
    # LIST OF REAL IMAGE URLS
    # ---------------------------------------------
    urls = {
        "img1.jpg": "https://picsum.photos/400",
        "img2.jpg": "https://picsum.photos/500",
        "img3.jpg": "https://picsum.photos/600",
        "img4.jpg": "https://picsum.photos/600",
        "img5.jpg": "https://picsum.photos/600",
        "img6.jpg": "https://picsum.photos/600",
        "img7.jpg": "https://picsum.photos/600",
        "img8.jpg": "https://picsum.photos/600",
        "img9.jpg": "https://picsum.photos/600",
        "img10.jpg": "https://picsum.photos/600",
    }

    async with aiohttp.ClientSession() as session:

        # ---------------------------------------------
        # CREATE TASKS FOR CONCURRENT EXECUTION
        # ---------------------------------------------
        # All downloads start together immediately
        tasks = []

        for filename, url in urls.items():
            task = asyncio.create_task(
                download_file(session, url, filename)
            )
            tasks.append(task)

        print("All downloads started (concurrently)\n")

        # ---------------------------------------------
        # WAIT FOR ALL DOWNLOADS TO COMPLETE
        # ---------------------------------------------
        await asyncio.gather(*tasks)

        print("\nAll downloads finished")


# ---------------------------------------------
# MEASURE TOTAL EXECUTION TIME
# ---------------------------------------------
start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f} sec")