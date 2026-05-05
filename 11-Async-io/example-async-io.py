# Detailed example focused on how asyncio works

import asyncio  # core library that provides event loop + async features


async def task1():
    # This is a coroutine (special function handled by asyncio)

    print("Task 1: started")

    # When this line runs:
    # - task1 is PAUSED (suspended)
    # - control goes back to asyncio event loop
    # - event loop can now run some other coroutine
    await asyncio.sleep(2)

    # After 2 seconds:
    # - event loop resumes this coroutine from here
    print("Task 1: resumed after waiting")

    print("Task 1: finished")


async def task2():
    print("Task 2: started")

    # Suspends this coroutine for 1 second
    await asyncio.sleep(1)

    print("Task 2: resumed after waiting")

    print("Task 2: finished")


async def main():
    # main is also a coroutine and acts as entry point

    print("Main: starting tasks\n")

    # asyncio.gather:
    # - gives multiple coroutines to event loop
    # - event loop manages execution of all of them
    # - they run concurrently (not one-by-one)
    # - execution switches when 'await' is hit

    await asyncio.gather(
        task1(),  # starts -> runs until first await -> suspends
        task2()   # starts -> runs while task1 is waiting
    )

    # This line runs only after BOTH coroutines are finished
    print("\nMain: all tasks completed")


# asyncio.run():
# - creates event loop
# - runs main() inside it
# - keeps loop running until main() is complete
# - then closes the loop
asyncio.run(main())