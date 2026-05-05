# Example of synchronization in asyncio using Lock

import asyncio
import time


# Shared resource (global variable)
counter = 0


async def increment(name, lock):
    # ---------------------------------------------
    # COROUTINE THAT MODIFIES SHARED STATE
    # ---------------------------------------------
    # Multiple coroutines will try to update 'counter'

    global counter

    print(f"{name} waiting for lock...")

    # ---------------------------------------------
    # ACQUIRE LOCK
    # ---------------------------------------------
    # Only ONE coroutine can enter this block at a time
    # Others will WAIT here until lock is released
    async with lock:
        print(f"{name} acquired lock")

        # Read current value
        temp = counter

        # Simulate some delay (context switch can happen here)
        await asyncio.sleep(10)

        # Modify value
        counter = temp + 1

        print(f"{name} updated counter to {counter}")

    # ---------------------------------------------
    # LOCK RELEASED AUTOMATICALLY
    # ---------------------------------------------
    print(f"{name} released lock")


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # CREATE LOCK
    # ---------------------------------------------
    # Lock ensures safe access to shared resource
    lock = asyncio.Lock()

    # ---------------------------------------------
    # START MULTIPLE COROUTINES
    # ---------------------------------------------
    # All try to modify same counter concurrently
    await asyncio.gather(
        increment("Task A", lock),
        increment("Task B", lock),
        increment("Task C", lock)
    )

    print(f"\nFinal counter value: {counter}")

    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")