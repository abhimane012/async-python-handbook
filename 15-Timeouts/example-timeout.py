# Example: asyncio timeout using asyncio.wait_for

import asyncio
import time


async def slow_task():
    # ---------------------------------------------
    # LONG RUNNING COROUTINE
    # ---------------------------------------------
    # This simulates a slow operation like:
    # - API call
    # - database query
    # - file download
    # - network request

    print("Slow task started")

    # non-blocking delay (event loop can run other tasks)
    # BUT this task itself takes 5 seconds total
    await asyncio.sleep(5)

    print("Slow task finished")

    return "Completed"


async def main():
    print("Main started\n")

    try:
        # ---------------------------------------------
        # asyncio.wait_for()
        # ---------------------------------------------
        # Purpose:
        # - runs a coroutine
        # - enforces a maximum time limit (timeout)
        #
        # How it works:
        # - starts slow_task()
        # - waits for it to finish
        # - if it takes longer than timeout → CANCELS it
        # - raises asyncio.TimeoutError

        result = await asyncio.wait_for(
            slow_task(),  # coroutine being executed
            timeout=4     # maximum allowed time in seconds
        )

        # This line only runs if task completes within timeout
        print("Result:", result)

    except asyncio.TimeoutError:
        # ---------------------------------------------
        # TIMEOUT HANDLING
        # ---------------------------------------------
        # This runs when:
        # - task takes longer than allowed timeout
        # - coroutine is cancelled automatically by asyncio

        print("Task timed out! (execution exceeded allowed time)")

    print("\nMain finished")


# Start event loop and execute main coroutine
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")