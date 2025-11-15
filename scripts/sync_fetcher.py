import time

import requests

urls = [
    "https://example.com",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
]

start = time.time()
for url in urls:
    response = requests.get(url)  # Blocking I/O
    print(url, len(response.text))

print("Time taken:", time.time() - start)
