import asyncio

import httpx
from fastapi import FastAPI

app = FastAPI()

urls = [
    "https://free.mockerapi.com/delay/1",
    "https://free.mockerapi.com/delay/2",
    "https://free.mockerapi.com/delay/3",
]

MAX_CONCURRENT_REQUESTS = 2  # Limit concurrent HTTP requests


async def fetch_with_semaphore(
    client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore
):
    async with semaphore:  # Limit concurrency
        try:
            response = await client.get(url, timeout=15.0)
            return {
                "url": url,
                "status": response.status_code,
                "length": len(response.text),
            }
        except httpx.RequestError as e:
            return {"url": url, "error": str(e)}


async def fetch(client: httpx.AsyncClient, url: str):
    try:
        response = await client.get(url, timeout=15.0)  # Timeout = 15 seconds
        return {
            "url": url,
            "status": response.status_code,
            "length": len(response.text),
        }
    except httpx.RequestError as e:
        return {"url": url, "error": str(e)}


def sync_fetch(client: httpx.Client, url: str):
    try:
        response = client.get(url, timeout=15.0)  # Timeout = 15 seconds
        return {
            "url": url,
            "status": response.status_code,
            "length": len(response.text),
        }
    except httpx.RequestError as e:
        return {"url": url, "error": str(e)}


@app.get("/sync-fetch-all")
def fetch_all():
    results = []
    with httpx.Client() as client:
        for url in urls:
            results.append(sync_fetch(client, url))
    return {"results": results}


@app.get("/fetch-all")
async def fetch_all():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return {"results": results}


@app.get("/fetch-all-with-semaphore")
async def fetch_all_with_semaphore():
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_with_semaphore(client, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
    return {"results": results}
