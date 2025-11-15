import asyncio
import time


async def say_hello():
    print("Hello")
    await asyncio.sleep(2)  # Non-blocking wait
    print("Hello again after 2 seconds")


async def say_world():
    print("World")
    await asyncio.sleep(1)  # Non-blocking wait
    print("World again after 1 second")


async def main():
    # Schedule both tasks concurrently
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_world())

    # Wait until both tasks are done
    await task1
    await task2


# Start the event loop
start = time.time()
asyncio.run(main())
print("elapsed_time =", time.time() - start)
