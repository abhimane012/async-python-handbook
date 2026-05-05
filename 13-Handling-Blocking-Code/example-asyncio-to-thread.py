# Example: Using asyncio.create_task (async) + asyncio.to_thread (blocking)

import asyncio  # core library for async programming (event loop, coroutines, tasks)
import time  # used for blocking simulation + measuring execution time


def blocking_task():
    # This is a normal synchronous function (NOT async)
    # It cannot use await and will BLOCK execution if run directly

    print("Blocking task started")

    # ❌ This sleep blocks the current thread completely
    # If this runs in event loop thread, everything freezes here
    time.sleep(10)

    print("Blocking task finished")

    return "Result from blocking task"


async def async_task_1():
    # This is a coroutine function (async function)
    # It runs inside asyncio event loop

    print("Async task-1 started")

    # ✅ This is non-blocking sleep
    # Event loop can switch to other tasks during this wait
    await asyncio.sleep(5)

    print("Async task-1 finished")

    return "Result from async task-1"

async def async_task_2():
    # This is a coroutine function (async function)
    # It runs inside asyncio event loop

    print("Async task-2 started")

    # ✅ This is non-blocking sleep
    # Event loop can switch to other tasks during this wait
    await asyncio.sleep(5)

    print("Async task-2 finished")

    return "Result from async task-2"


async def main():
    print("Main started\n")

    # -------------------------------
    # create_task (ASYNC COROUTINE)
    # -------------------------------
    # This schedules async_task_1(), async_task_2() on the event loop immediately
    # It does NOT wait here, it runs concurrently
    async_task_obj_1 = asyncio.create_task(async_task_1())
    async_task_obj_2 = asyncio.create_task(async_task_2())

    # -------------------------------
    # to_thread (BLOCKING FUNCTION)
    # -------------------------------
    # This runs blocking_task() in a separate thread
    # So event loop remains free and NOT blocked
    blocking_task_obj = asyncio.to_thread(blocking_task)

    print("Both tasks started:")
    print("- async_task is running in event loop")
    print("- blocking_task is running in separate thread\n")

    # -------------------------------
    # WAITING FOR RESULTS
    # -------------------------------
    # await means:
    # - pause THIS coroutine (main)
    # - but event loop continues running other tasks
    blocking_result = await blocking_task_obj
    async_result_1 = await async_task_obj_1
    async_result_2 = await async_task_obj_2

    print("\n--- Results ---")
    print("Async result task-1:", async_result_1)
    print("Async result task-2:", async_result_2)
    print("Blocking result:", blocking_result)

    print("\nMain finished")


# -----------------------------------
# MEASURE TOTAL EXECUTION TIME
# -----------------------------------

start = time.perf_counter()

# Starts event loop and runs main coroutine
asyncio.run(main())

end = time.perf_counter()

print(f"\nTotal time to takes is {end - start:.2f}")