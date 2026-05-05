# Example of async and await keywords in Python

import asyncio  # used for async programming (we will cover this later)

# async keyword: defines a coroutine function
async def fetch_data():
    print("Start fetching data...")

    # await keyword: pauses execution here without blocking entire program
    await asyncio.sleep(2)

    print("Data fetched successfully")
    return {"data": 123}


# another coroutine function
async def process_data():
    print("Start processing data...")

    await asyncio.sleep(1)

    print("Data processed successfully")


# main coroutine that controls execution
async def main():
    # await makes sure fetch_data completes before moving forward
    data = await fetch_data()
    print("Received:", data)

    await process_data()


# runs the async program
asyncio.run(main())