# Example of async iteration in asyncio

import asyncio
import time


class AsyncCounter:
    # ---------------------------------------------
    # ASYNC ITERABLE OBJECT
    # ---------------------------------------------
    # This class supports async iteration using:
    # - __aiter__()
    # - __anext__()

    def __init__(self, limit):
        self.limit = limit  # max number to count
        self.current = 0    # current value


    def __aiter__(self):
        # ---------------------------------------------
        # RETURNS ASYNC ITERATOR OBJECT
        # ---------------------------------------------
        # Usually returns self
        return self


    async def __anext__(self):
        # ---------------------------------------------
        # CALLED ON EACH ITERATION STEP
        # ---------------------------------------------
        # Must be async function
        # Should return next value OR raise StopAsyncIteration

        if self.current >= self.limit:
            # signals end of async iteration
            raise StopAsyncIteration

        # simulate async delay (like fetching next data chunk)
        await asyncio.sleep(10)

        value = self.current
        self.current += 1

        return value


async def main():
    print("Main started\n")

    counter = AsyncCounter(5)

    # ---------------------------------------------
    # ASYNC FOR LOOP
    # ---------------------------------------------
    # Works like normal for loop BUT:
    # - uses await internally
    # - handles async data sources

    async for number in counter:
        print(f"Received:", number)

    print("\nAsync iteration finished")
    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")