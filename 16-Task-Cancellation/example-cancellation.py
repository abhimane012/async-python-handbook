# Example of task cancellation in asyncio 

import asyncio
import time


async def long_running_task():
    # ---------------------------------------------
    # LONG RUNNING COROUTINE
    # ---------------------------------------------
    # This simulates a task that keeps doing work over time

    print("Task started")

    try:
        # Loop simulating continuous work
        for i in range(10):
            print(f"Working... step {i}")

            # non-blocking delay
            # this is a suspension point where cancellation can happen
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        # ---------------------------------------------
        # WHAT HAPPENS ON CANCELLATION?
        # ---------------------------------------------
        # When task.cancel() is called:
        # - asyncio sends a CancelledError into this coroutine
        # - it is raised at the next await point
        # - we can catch it here to handle cleanup

        print("Task received cancellation signal!")

        # Here we could:
        # - close files
        # - release resources
        # - save progress

        print("Cleaning up before stopping...")

        # IMPORTANT:
        # Re-raise the exception so asyncio knows task was cancelled
        raise

    # This line will NOT run if task is cancelled
    print("Task completed normally")


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # CREATE TASK
    # ---------------------------------------------
    # - schedules coroutine to run immediately
    # - runs independently in event loop
    task = asyncio.create_task(long_running_task())

    # Let the task run for some time
    # During this time:
    # - task prints steps
    # - event loop continues managing execution
    await asyncio.sleep(3)

    # ---------------------------------------------
    # CANCEL THE TASK
    # ---------------------------------------------
    # - sends cancellation request
    # - does NOT stop instantly
    # - cancellation happens at next await inside coroutine
    print("\nMain: cancelling task...\n")
    task.cancel()

    try:
        # ---------------------------------------------
        # AWAITING CANCELLED TASK
        # ---------------------------------------------
        # When we await a cancelled task:
        # - it raises asyncio.CancelledError here
        await task

    except asyncio.CancelledError:
        # This confirms that task was actually cancelled
        print("Main: confirmed task cancellation")

    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")