# Example of BLOCKING code inside async

import asyncio
import time  # blocking function (normal synchronous sleep)

async def task1():
    print("Task 1: started")

    print("Task 1: going to BLOCK the event loop now")

    # ❌ This is a blocking call
    # What happens here:
    # - This does NOT pause only task1
    # - It completely FREEZES the entire event loop
    # - No other coroutine can run during this time
    # - Even if other tasks are ready, they must WAIT

    time.sleep(10)  # blocks everything for 3 seconds

    print("Task 1: finished (event loop was blocked during this time)")


async def task2():
    print("Task 2: started")

    # This is a proper non-blocking wait
    # BUT it will not behave as expected because of blocking in task1

    print("Task 2: waiting for 10 second (should run during Task 1)")

    await asyncio.sleep(10)  # normally this allows switching

    print("Task 2: finished")


async def main():
    print("Main: starting both tasks\n")

    # Both tasks are scheduled to run together
    # But actual execution depends on event loop availability

    await asyncio.gather(
        task1(),  # starts first → hits blocking sleep → freezes everything
        task2()   # cannot proceed properly until blocking is over
    )

    print("\nMain: all tasks completed")


# Starts event loop
# Notice behavior:
# - Task 2 will NOT run during the 10-second sleep of task1
# - Everything appears sequential because of blocking

start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"\nTotal time to takes is {end - start:.2f}")