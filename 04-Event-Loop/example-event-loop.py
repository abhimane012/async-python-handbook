# Example of Event Loop using asyncio

import asyncio  # don't worry about this, will cover later
import time
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def task3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 finished")

async def main():
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

# Event loop starts here
start = time.perf_counter()
asyncio.run(main())  # don't worry about this, will cover later
end = time.perf_counter()

print(f"Total time takes is {end - start:.2f}")