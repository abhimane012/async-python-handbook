# Clear real-world style example of asyncio Task (parallel API calls simulation)

import asyncio
import time

async def api_call(name, delay):
    # This function simulates an API request
    # It is a coroutine (async function)

    print(f"[START] {name}")

    # await suspends ONLY this function here
    # while waiting, other tasks keep running
    await asyncio.sleep(delay)  

    print(f"[END] {name}")

    # returning fake response like an API
    return f"{name} response"


async def main():
    # create_task() schedules coroutines to run "in background"
    # they start immediately without waiting for each other

    user_task = asyncio.create_task(api_call("User API", 10))
    orders_task = asyncio.create_task(api_call("Orders API", 8))
    payments_task = asyncio.create_task(api_call("Payments API", 7))

    print("All API calls triggered...\n")

    # Even though we await later,
    # all tasks are already running concurrently in background

    user_result = await user_task  # waits only if not finished yet
    orders_result = await orders_task
    payments_result = await payments_task

    print("\n--- Results ---")
    print(user_result)
    print(orders_result)
    print(payments_result)



start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter() # starts async program execution

print(f"\nTotal time of execution is {end - start:.2f} seconds")