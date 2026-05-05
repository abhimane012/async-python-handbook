# Example: ProcessPoolExecutor + asyncio.create_task

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def cpu_intensive_task(n):
    # ---------------------------------------------
    # CPU-BOUND FUNCTION (BLOCKING)
    # ---------------------------------------------
    # This function performs heavy computation
    # It does NOT use async/await
    # It would block event loop if run normally

    print(f"[PROCESS] CPU task started with n={n}")

    total = 0

    # Heavy CPU computation loop
    # This simulates tasks like:
    # - image processing
    # - ML calculations
    # - large number crunching
    for i in range(n):
        total += i * i

    print(f"[PROCESS] CPU task finished with n={n}")

    time.sleep(20)

    return total


async def async_task():
    # ---------------------------------------------
    # ASYNC TASK (EVENT LOOP BASED)
    # ---------------------------------------------
    # This runs inside asyncio event loop
    # It is non-blocking

    print("[ASYNC] Task started")

    # This pauses ONLY this coroutine
    # Event loop can switch to other tasks during this time
    await asyncio.sleep(2)

    print("[ASYNC] Task finished")

    return "Async result done"


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # PROCESS POOL EXECUTOR
    # ---------------------------------------------
    # Why we use this:
    # - Python has GIL (Global Interpreter Lock)
    # - CPU-heavy tasks cannot run truly in parallel in threads
    # - ProcessPoolExecutor uses multiple processes
    # - Each process has its own Python interpreter
    # - So CPU tasks run in true parallelism

    with ProcessPoolExecutor() as executor:

        # Get current event loop
        loop = asyncio.get_running_loop()

        # ---------------------------------------------
        # SUBMIT CPU TASKS TO PROCESS POOL
        # ---------------------------------------------
        # run_in_executor sends function to process pool
        # returns a Future (result will come later)

        cpu_task1 = loop.run_in_executor(
            executor,
            cpu_intensive_task,
            5_000_000
        )

        cpu_task2 = loop.run_in_executor(
            executor,
            cpu_intensive_task,
            4_000_000
        )

        # ---------------------------------------------
        # START ASYNC TASK IN EVENT LOOP
        # ---------------------------------------------
        # This runs immediately in event loop
        async_task_obj = asyncio.create_task(async_task())

        print("All tasks started:\n")
        print("- CPU tasks running in separate processes")
        print("- Async task running in event loop\n")

        # ---------------------------------------------
        # IMPORTANT BEHAVIOR
        # ---------------------------------------------
        # Even while CPU processes are running:
        # - event loop is NOT blocked
        # - async tasks can still execute
        # - system remains responsive

        await asyncio.sleep(1)
        print("Event loop is still responsive while CPU work runs...\n")

        # ---------------------------------------------
        # WAIT FOR ALL RESULTS
        # ---------------------------------------------
        # Awaiting means:
        # - pause current coroutine (main)
        # - BUT does NOT stop event loop

        cpu_result1 = await cpu_task1
        cpu_result2 = await cpu_task2
        async_result = await async_task_obj

        print("\n--- FINAL RESULTS ---")
        print("CPU Result 1:", cpu_result1)
        print("CPU Result 2:", cpu_result2)
        print("Async Result:", async_result)

    print("\nMain finished")


# ---------------------------------------------
# EXECUTION TIME MEASUREMENT
# ---------------------------------------------
# Helps understand performance benefit of concurrency


if __name__ == "__main__":
    # This guard prevents child processes (created by multiprocessing on macOS/Windows)
    # from re-running this file when they import it.
    # Without it, ProcessPoolExecutor would repeatedly re-execute this script,
    # causing infinite process spawning and BrokenProcessPool errors.

    start = time.perf_counter()

    asyncio.run(main())

    end = time.perf_counter()

    print(f"\nTotal time to takes is {end - start:.2f}")