# Non-blocking code example using asyncio

import asyncio  # don't worry about this import for now, we will cover it later

async def task1():  # async keyword: don't worry about it, will cover later
    print("Task 1 started")
    
    await asyncio.sleep(5)  # await + sleep: don't worry about these concepts, will cover later
    
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    print("Task 2 finished")

async def main():
    await asyncio.gather(  # gather: don't worry about this, will cover later
        task1(),
        task2()
    )

asyncio.run(main())  # run: don't worry about this, will cover later