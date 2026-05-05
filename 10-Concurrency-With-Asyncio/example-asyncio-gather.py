# Real-life example of asyncio.gather (e-commerce dashboard simulation)

import asyncio
import time 

async def get_user_profile():
    # This function simulates an API call to fetch user profile data
    # It is a coroutine (async function)

    print("Fetching user profile...")

    # Simulating network delay (like calling a backend service)
    # Function SUSPENDS here and allows other coroutines to run
    await asyncio.sleep(5)

    # After delay completes, execution RESUMES from here
    print("User profile received")

    # Returning data (this becomes the result collected by gather)
    return {"name": "Abhishek", "age": 25}


async def get_recent_orders():
    # This function simulates fetching user's recent orders

    print("Fetching recent orders...")

    # Suspends here for 2 seconds (non-blocking wait)
    await asyncio.sleep(8)

    # Resumes after wait is complete
    print("Recent orders received")

    # Returning list of orders
    return ["Order1", "Order2"]


async def get_notifications():
    # This function simulates fetching notifications for the user

    print("Fetching notifications...")

    # Suspends here for 1 second
    await asyncio.sleep(10)

    # Resumes after wait
    print("Notifications received")

    # Returning notifications list
    return ["Notification1"]


async def main():
    print("Opening app dashboard...\n")

    # asyncio.gather:
    # - takes multiple coroutines as input
    # - starts ALL of them immediately (no waiting between them)
    # - runs them concurrently
    # - waits until ALL are completed
    # - collects and returns their results in the SAME ORDER

    results = await asyncio.gather(
        get_user_profile(),   # starts execution -> suspends at sleep
        get_recent_orders(),  # starts execution -> suspends at sleep
        get_notifications()   # starts execution -> suspends at sleep
    )

    print("\n--- Dashboard Data Ready ---")

    # results is a list:
    # results[0] -> return value of get_user_profile
    # results[1] -> return value of get_recent_orders
    # results[2] -> return value of get_notifications

    user_profile = results[0]
    orders = results[1]
    notifications = results[2]

    print("User:", user_profile)
    print("Orders:", orders)
    print("Notifications:", notifications)


# starts the event loop and runs main coroutine

start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"\nTotal time to takes is {end - start:.2f}")