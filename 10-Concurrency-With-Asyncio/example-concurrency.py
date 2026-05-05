# real-life example of concurrency using asyncio (food delivery app simulation)

import asyncio 
import time

async def place_order():
    # simulates user placing an order
    print("Order placed")

    # suspends this function for 1 second (non-blocking wait)
    # while this is waiting, other tasks can run
    await asyncio.sleep(4)

    print("Restaurant accepted order")


async def prepare_food():
    # simulates kitchen preparing food
    print("Food preparation started")

    # takes longer time, but does not block other tasks
    await asyncio.sleep(15)

    print("Food is ready")


async def assign_delivery():
    # simulates finding a delivery partner
    print("Searching for delivery partner")

    # during this wait, other coroutines continue running
    await asyncio.sleep(7)

    print("Delivery partner assigned")


async def main():
    # create_task schedules all coroutines to start immediately
    # they begin execution without waiting for each other

    order_task = asyncio.create_task(place_order())
    food_task = asyncio.create_task(prepare_food())
    delivery_task = asyncio.create_task(assign_delivery())

    print("All processes started...\n")

    # Even though we are awaiting one by one,
    # all tasks are already running concurrently in background

    await order_task      # waits only if task not finished yet
    await food_task
    await delivery_task

    print("\nOrder completed successfully!")


# starts the event loop and runs main coroutine

start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"Total time to takes is {end - start:.2f}")