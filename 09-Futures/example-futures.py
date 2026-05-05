# Example of Future in asyncio (with detailed comments)

import asyncio  

async def set_future_value(future):
    # This coroutine simulates some background work
    print("Worker started")

    # simulate delay (like API call, DB query, etc.)
    # function suspends here, event loop can run other tasks
    await asyncio.sleep(2)

    # Future is like an empty box created earlier
    # now we are putting value inside that box
    future.set_result("Data received")

    # once result is set, anyone waiting on this future will resume
    print("Worker finished and value set in future")


async def main():
    # Creating a Future object
    # It does NOT have a value yet
    # It will be filled later by some other coroutine
    future = asyncio.Future()

    # Start background work that will eventually set value in future
    # create_task schedules it to run independently
    asyncio.create_task(set_future_value(future))

    print("Waiting for future result...")

    # await future:
    # pauses here until future.set_result(...) is called
    # once value is set, execution resumes with that value
    result = await future

    print("Future result:", result)


# Start event loop and run main coroutine
asyncio.run(main())