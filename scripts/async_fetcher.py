# import asyncio
# import time
#
# import aiohttp
#
# urls = [
#     "https://example.com",
#     "https://httpbin.org/delay/2",
#     "https://httpbin.org/delay/3",
# ]
#
#
# async def fetch(session, url):
#     async with session.get(url) as response:  # Non-blocking
#         text = await response.text()
#         print(url, len(text))
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session, url) for url in urls]
#         await asyncio.gather(*tasks)  # Run all tasks concurrently
#
#
# start = time.time()
# asyncio.run(main())
# print("Time taken:", time.time() - start)
#
#
import asyncio
import time

import httpx

urls = [
    "https://example.com",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
]


async def fetch(client, url):
    response = await client.get(url, timeout=15.0)  # Increase timeout
    print(url, len(response.text))


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        await asyncio.gather(*tasks)  # Run all tasks concurrently


start = time.time()
asyncio.run(main())
print("Time taken:", time.time() - start)
