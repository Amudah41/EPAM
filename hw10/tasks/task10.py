import aiohttp
import asyncio
import time


urls = [
    "https://docs.python.org/3/",
    "https://google.com",
    "https://example.com",
    "https://python.org",
    "https://www.youtube.com/",
    "https://github.com/",
]


async def say_after(delay, what):
    await asyncio.sleep(delay)  # (4) (5)
    print(what) # (6)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print("Started")
    # Wait until both tasks are completed
    # (should take around 2 seconds.)
    await task1
    await task2 
    print("Finished")

t1 = time.time()
asyncio.run(main())
t2 = time.time()
print(f"It took {t2 - t1} seconds")




async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

async def main_2():
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]

    t1 = time.time()
    await asyncio.gather(*tasks)
    t2 = time.time()

    print(f"It took {t2 - t1} seconds")
    for task in tasks:
        print(task.result().status, end=" ")

asyncio.run(main_2())


# /html/body/main/div[1]/div[3]/div/div[1]/div[2]/table/tbody/tr[7]/td[2]/text()[1]

# //*[@id="index-list-container"]/div[2]/table/tbody/tr[7]/td[2]/text()[1]


# 236.45


# 236.45







# https://markets.businessinsider.com/index/components/s&p_500?p=7