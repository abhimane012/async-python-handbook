# Demonstrating suspension using await by calling coroutines inside each other

import asyncio  # will be covered later

async def step_three():
    print("Step 3 started")
    await asyncio.sleep(2)  # function suspends here
    print("Step 3 finished")


async def step_two():
    print("Step 2 started")

    await asyncio.sleep(2)  # function suspends here
    print("Step 2 resumed after wait")

    # calling another coroutine inside (suspension continues through call chain)
    await step_three()

    print("Step 2 finished")


async def step_one():
    print("Step 1 started")

    await asyncio.sleep(2)  # function suspends here
    print("Step 1 resumed after wait")

    # calling next coroutine
    await step_two()

    print("Step 1 finished")


async def main():
    await step_one()

asyncio.run(main())