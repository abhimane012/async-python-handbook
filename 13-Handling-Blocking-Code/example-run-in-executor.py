# Example: run_in_executor + async function together

import asyncio
import time


def blocking_io():
    # Normal blocking function (cannot use await)
    # If run in event loop thread, it would freeze everything

    print("Blocking IO started")

    time.sleep(10)  # ❌ blocks thread

    print("Blocking IO finished")

    return "Data from blocking IO"


async def async_task():
    # Proper async function (runs in event loop)

    print("Async task started")

    # non-blocking wait (event loop can do other work)
    await asyncio.sleep(5)

    print("Async task finished")

    return "Result from async task"


async def main():
    print("Main started\n")

    loop = asyncio.get_running_loop()

    # ----------------------------------------
    # run blocking function in thread pool
    # ----------------------------------------
    # event loop stays free while this runs in background thread
    blocking_future = loop.run_in_executor(
        None,
        blocking_io
    )

    # ----------------------------------------
    # start async function normally
    # ----------------------------------------
    # this runs immediately in event loop
    async_task_future = asyncio.create_task(async_task())

    print("Both tasks started (one in thread, one in event loop)\n")

    # ----------------------------------------
    # event loop continues working while both run
    # ----------------------------------------
    await asyncio.sleep(2)
    print("Event loop still active while tasks run...\n")

    # ----------------------------------------
    # wait for both results
    # ----------------------------------------
    blocking_result = await blocking_future
    async_result = await async_task_future

    print("\nResults:")
    print("Blocking:", blocking_result)
    print("Async:", async_result)

    print("\nMain finished")


# ----------------------------------------
# measure execution time
# ----------------------------------------

start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"\nTotal time to takes is {end - start:.2f}")