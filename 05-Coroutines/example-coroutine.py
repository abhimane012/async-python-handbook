# Example of Coroutine in Python

import asyncio  # used to work with asynchronous code

# async function = coroutine
async def greet():
    print("Hello")  # runs immediately when coroutine starts
    
    # pauses execution here and gives control back to event loop
    # resumes after 1 second
    await asyncio.sleep(1)
    
    print("World")  # runs after the pause is complete


async def main():
    # calling coroutine greet
    # but it will NOT run immediately like normal function
    await greet()


# starts the event loop and runs the main coroutine
asyncio.run(main())