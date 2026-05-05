# Example: asyncio.gather with return_exceptions=True (all tasks complete, errors returned)

import asyncio
import time


async def task1():
    # ---------------------------------------------
    # SUCCESSFUL COROUTINE
    # ---------------------------------------------

    print("Task 1 started")

    # non-blocking wait (event loop can switch tasks here)
    await asyncio.sleep(10)

    print("Task 1 finished")

    # normal return value
    return "Result 1"


async def task2():
    # ---------------------------------------------
    # FAILING COROUTINE
    # ---------------------------------------------

    print("Task 2 started")

    await asyncio.sleep(20)

    # ---------------------------------------------
    # SIMULATED ERROR
    # ---------------------------------------------
    # This exception WILL NOT crash gather when
    # return_exceptions=True is used
    raise ValueError("Error in Task 2")


async def task3():
    # ---------------------------------------------
    # ANOTHER SUCCESSFUL COROUTINE
    # ---------------------------------------------

    print("Task 3 started")

    await asyncio.sleep(10)

    print("Task 3 finished")

    return "Result 3"


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # asyncio.gather BEHAVIOR WITH return_exceptions=True
    # ---------------------------------------------
    # 1. Runs ALL coroutines concurrently
    # 2. Waits for ALL of them to finish
    # 3. DOES NOT stop execution if any task fails
    # 4. Instead of raising exception:
    #    → it captures exception and returns it in results list
    #
    # So:
    # - Success → normal return value
    # - Failure → Exception object in result list

    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True  # prevents gather from crashing
    )

    print("\n--- Gather Results ---")

    # ---------------------------------------------
    # RESULTS STRUCTURE:
    # ---------------------------------------------
    # results is a list in same order as tasks passed
    # each item can be:
    # - string/int/etc (normal return)
    # - Exception object (if task failed)

    for i, result in enumerate(results, start=1):

        # check if result is an exception
        if isinstance(result, Exception):
            print(f"Task {i} failed →", repr(result))
        else:
            print(f"Task {i} succeeded →", result)

    print("\nMain finished")


# Start asyncio event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")