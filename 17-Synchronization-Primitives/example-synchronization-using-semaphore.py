# Example of synchronization using asyncio.Semaphore

import asyncio
import time 


async def use_resource(name, semaphore):
    # ---------------------------------------------
    # COROUTINE THAT USES LIMITED RESOURCE
    # ---------------------------------------------
    # Only limited number of coroutines can run this section at same time

    print(f"{name} waiting to access resource...")

    # ---------------------------------------------
    # ACQUIRE SEMAPHORE
    # ---------------------------------------------
    # Semaphore allows N coroutines at the same time
    # Others will WAIT here if limit is reached
    async with semaphore:
        print(f"{name} acquired access")

        # simulate work using resource
        await asyncio.sleep(10)

        print(f"{name} releasing resource")

    # semaphore is automatically released after exiting block


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # CREATE SEMAPHORE
    # ---------------------------------------------
    # value=2 → only 2 coroutines allowed at same time
    semaphore = asyncio.Semaphore(2)

    # ---------------------------------------------
    # START MULTIPLE TASKS
    # ---------------------------------------------
    # Even though 5 coroutines start,
    # only 2 will run inside critical section at once
    await asyncio.gather(
        use_resource("Task 1", semaphore),
        use_resource("Task 2", semaphore),
        use_resource("Task 3", semaphore),
        use_resource("Task 4", semaphore),
        use_resource("Task 5", semaphore),
        use_resource("Task 6", semaphore),
        use_resource("Task 7", semaphore),
        use_resource("Task 8", semaphore),
        use_resource("Task 9", semaphore),
        use_resource("Task 10", semaphore),
    )

    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")