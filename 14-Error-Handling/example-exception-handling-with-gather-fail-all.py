# Example: asyncio.gather exception handling (fail-all behavior )

import asyncio
import time 


async def task1():
    # First coroutine (successful task)

    print("Task 1 started")

    # non-blocking delay (event loop can run other tasks)
    await asyncio.sleep(10)

    print("Task 1 finished")

    # returning value to gather
    return "Result 1"


async def task2():
    # Second coroutine (this one will FAIL intentionally)

    print("Task 2 started")

    await asyncio.sleep(10)

    # ---------------------------------------------
    # SIMULATED ERROR
    # ---------------------------------------------
    # When this exception occurs:
    # - it is captured by asyncio.gather internally
    # - gather will immediately raise it to caller
    # - other tasks may be cancelled depending on timing
    raise ValueError("Error in Task 2")


async def task3():
    # Third coroutine (successful task)

    print("Task 3 started")

    await asyncio.sleep(20)

    print("Task 3 finished")

    return "Result 3"


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # asyncio.gather BEHAVIOR
    # ---------------------------------------------
    # 1. Starts ALL tasks at the same time (concurrently)
    # 2. Waits for ALL tasks to complete
    # 3. BUT if ANY task raises an exception:
    #    - gather immediately raises that exception
    #    - result is NOT returned normally
    #    - remaining tasks may be cancelled or interrupted
    #
    # Important:
    # This is called "fail-fast" behavior

    try:
        results = await asyncio.gather(
            task1(),
            task2(),  # this will fail
            task3()
        )

        # This line will not execute if any task fails
        print("Results:", results)

    except Exception as e:
        # This catches the FIRST exception raised inside any task
        print("\nCaught exception from gather:", e)

    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")