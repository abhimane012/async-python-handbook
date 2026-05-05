# Example of exception handling with asyncio.create_task

import asyncio
import time


async def risky_task():
    # This coroutine simulates a task that fails during execution

    print("Risky task started")

    # non-blocking wait (event loop remains free)
    await asyncio.sleep(10)

    # ---------------------------------------------
    # SIMULATED FAILURE
    # ---------------------------------------------
    # This exception is raised INSIDE the coroutine
    # It does NOT immediately crash the program
    # Instead, it gets attached to the Task object
    raise ValueError("Error occurred in risky_task")


async def safe_task():
    # This coroutine always completes successfully

    print("Safe task started")

    await asyncio.sleep(20)

    print("Safe task finished")

    return "Safe result"


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # create_task behavior
    # ---------------------------------------------
    # - schedules coroutine to run immediately
    # - wraps coroutine inside a Task object
    # - Task runs independently in event loop
    # - exceptions are stored inside Task until awaited

    task1 = asyncio.create_task(risky_task())
    task2 = asyncio.create_task(safe_task())

    print("Both tasks have been scheduled\n")

    # ---------------------------------------------
    # IMPORTANT BEHAVIOR
    # ---------------------------------------------
    # If we never await a task:
    # - exception may be lost or shown as "Task exception was never retrieved"
    # So we ALWAYS await tasks to handle errors properly

    try:
        # Awaiting task1:
        # - if risky_task fails, exception is raised here
        result1 = await task1
        print("Risky task result:", result1)

    except Exception as e:
        # Exception coming from inside the task is caught here
        print("Caught exception from risky_task:", e)

    # ---------------------------------------------
    # Safe task continues normally
    # ---------------------------------------------
    # This runs independently of task1 failure
    result2 = await task2

    print("Safe task result:", result2)

    print("\nMain finished")


# Start event loop and execute main coroutine
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")