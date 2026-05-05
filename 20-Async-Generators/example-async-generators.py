# Example of async generator in asyncio

import asyncio
import time


async def async_number_generator(limit):
    # ---------------------------------------------
    # ASYNC GENERATOR FUNCTION
    # ---------------------------------------------
    # - defined using async def
    # - uses 'yield' to produce values
    # - can use 'await' inside (unlike normal generators)

    for i in range(limit):
        print(f"Generator: preparing value {i}")

        # simulate async work (like fetching data)
        await asyncio.sleep(1)

        # yield sends value to caller (like return, but continues later)
        yield i

        print(f"Generator: value {i} consumed\n")


async def main():
    print("Main started\n")

    # calling async generator returns an async generator object
    gen = async_number_generator(5)

    # ---------------------------------------------
    # ASYNC FOR LOOP CONSUMES GENERATOR
    # ---------------------------------------------
    # - automatically awaits each value
    # - handles suspension between yields
    async for value in gen:
        print(f"Consumer received: {value}")

        # simulate processing delay
        await asyncio.sleep(0.5)

    print("\nAsync generator fully consumed")
    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")