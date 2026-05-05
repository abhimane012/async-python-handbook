# Example of asyncio Queue (Producer-Consumer pattern)

import asyncio
import time


async def producer(queue):
    # ---------------------------------------------
    # PRODUCER: puts data into queue
    # ---------------------------------------------
    # Simulates generating items (like incoming requests)

    for i in range(5):
        print(f"Producer: preparing item {i}")

        # simulate delay in producing data
        await asyncio.sleep(5)

        # put item into queue
        # if queue is full, this will WAIT (non-blocking)
        await queue.put(i)

        print(f"Producer: added item {i} to queue")

    print("Producer: done producing")


async def consumer(queue):
    # ---------------------------------------------
    # CONSUMER: takes data from queue
    # ---------------------------------------------
    # Simulates processing items

    while True:
        print("Consumer: waiting for item...")

        # get item from queue
        # if queue is empty, this will WAIT (non-blocking)
        item = await queue.get()

        print(f"Consumer: got item {item}")

        # simulate processing time
        await asyncio.sleep(5)

        print(f"Consumer: processed item {item}")

        # mark task as done (important for queue tracking)
        queue.task_done()


async def main():
    print("Main started\n")

    # ---------------------------------------------
    # CREATE QUEUE
    # ---------------------------------------------
    # Queue safely shares data between coroutines
    queue = asyncio.Queue()

    # ---------------------------------------------
    # START PRODUCER AND CONSUMER
    # ---------------------------------------------
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    # ---------------------------------------------
    # WAIT FOR PRODUCER TO FINISH
    # ---------------------------------------------
    await producer_task

    # ---------------------------------------------
    # WAIT UNTIL ALL ITEMS ARE PROCESSED
    # ---------------------------------------------
    # queue.join() waits until:
    # - all items added via put() are processed
    # - and task_done() called for each
    await queue.join()

    # ---------------------------------------------
    # CANCEL CONSUMER (infinite loop)
    # ---------------------------------------------
    consumer_task.cancel()

    print("\nMain finished")


# Start event loop
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal time taken {end - start:.2f}")