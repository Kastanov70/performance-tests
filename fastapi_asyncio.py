import asyncio
from datetime import datetime

import httpx


async def fetch_url(url:str)->tuple[int,str]:
    async with httpx.AsyncClient() as client:
        print("Request from fetch_url")
        response = await client.get(url)
        print("Response from fetch_url")
    return response.status_code, response.text[:50]

async def main():
    urls = [
        "https://postman-echo.com/delay/1",
        "https://postman-echo.com/delay/2",
        "https://postman-echo.com/delay/3",
    ]
    results = await asyncio.gather(*(fetch_url(url) for url in urls))

    for status, text in results:
        print(f"Статус ответа: {status}, начало текста: {text}")

if __name__ == "__main__":
    start_time = datetime.now()
    asyncio.run(main())
    print(datetime.now() - start_time)
