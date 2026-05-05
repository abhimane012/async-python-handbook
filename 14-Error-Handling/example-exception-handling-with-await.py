# Example of exception handling with await in asyncio

import asyncio
import time  # will be covered later


async def risky_task():
    # This coroutine simulates a task that may fail

    print("Risky task started")

    # async sleep (non-blocking delay)
    await asyncio.sleep(1)

    # ---------------------------------------------
    # Simulated error condition
    # ---------------------------------------------
    # When this line runs, an exception is raised
    # This exception will propagate to wherever this coroutine is awaited
    raise ValueError("Something went wrong inside risky_task")


async def safe_task():
    # This coroutine simulates a normal successful async operation

    print("Safe task started")

    # non-blocking wait (event loop remains free)
    await asyncio.sleep(2)

    print("Safe task finished")

    # returning normal result
    return "Safe result"


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # TRY / EXCEPT AROUND AWAIT
    # ---------------------------------------------
    # When we await a coroutine:
    # - if it raises an exception
    # - that exception is thrown here
    # - so we must handle it using try/except

    try:
        # coroutine execution starts here
        result1 = await risky_task()

        # this line will NOT run because exception occurs above
        print("Risky result:", result1)

    except Exception as e:
        # exception raised inside risky_task is caught here
        # this prevents program from crashing
        print("Caught error from risky_task:", e)

    print("\nEven after error, program continues...\n")

    # ---------------------------------------------
    # NORMAL COROUTINE EXECUTION AFTER FAILURE
    # ---------------------------------------------
    # Even though risky_task failed,
    # event loop is still alive and can run other coroutines

    result2 = await safe_task()

    print("Safe result:", result2)

    print("\nMain finished")


# Start event loop and run main coroutine
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"Total time takes {end - start:.2f}")