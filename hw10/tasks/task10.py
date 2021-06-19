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
    print(what)  # (6)


async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

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


# from multiprocessing import Pool
# from concurrent.futures import ThreadPoolExecutor
import json
from datetime import datetime

# from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from requests.models import Response


def get_html(url):
    with requests.Session() as session:
        response = session.get(url)
    return response.text


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def get_all_links_and_growth(html):
    soup = BeautifulSoup(html, "lxml")

    tds = soup.find("tbody", class_="table__tbody")

    while tds := tds.find_next("tr"):
        a = tds.find("td", class_="table__td table__td--big").find("a").get("href")
        link = "https://markets.businessinsider.com" + a
        growth = to_float(
            tds.find_all(class_="table__td")[-1].find_all("span")[-1].text[:-1]
        )

        yield link, growth


def actual_exchange_rate(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.find("valute", id="R01235").find("value").text


def to_float(number: str):
    try:
        number = number.replace(",", "")
        return float(number)
    except ValueError as err:
        raise err(f"Can't convert {number} to float.")


def convertion_USD_to_RUB(func):
    def wrapper(price):

        return func(to_float(price), USD)

    USD = to_float(
        actual_exchange_rate(get_html("http://www.cbr.ru/scripts/XML_daily.asp"))
    )

    return wrapper


@convertion_USD_to_RUB
def convert(price, USD):
    return price * USD


async def get_page_data(html, growth):
    soup = BeautifulSoup(html, "lxml")
    lock = asyncio.Lock()

    # code_name_price_area = soup.find('div', class_="price-section__row")

    try:
        code = (
            soup.find("div", class_="price-section__row")
            .find(class_="price-section__category")
            .find_next()
            .text[2:]
        )
    except:
        code = ""

    try:
        name = (
            soup.find("div", class_="price-section__row")
            .find(class_="price-section__label")
            .text[:-1]
        )
    except:
        name = ""

    async with lock:
        add_to_buffer(code, name, growth=growth)

    try:
        price = convert(
            soup.find("div", class_="price-section__row")
            .find(class_="price-section__current-value")
            .text
        )
    except:
        price = 0

    async with lock:
        add_to_buffer(code, name, price=price)
    try:
        PE = to_float(
            soup.find("div", class_="snapshot__data-item").find(
                text=True, recursive=False
            )
        )

    except:
        PE = 0
    async with lock:
        add_to_buffer(code, name, PE=PE)

    try:
        low_52_week = to_float(
            soup.find(class_="snapshot__data-item snapshot__data-item--small").find(
                text=True, recursive=False
            )
        )

        high_52_week = to_float(
            soup.find(
                class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right"
            ).find(text=True, recursive=False)
        )
        potential_profit = (high_52_week - low_52_week) * 100 / low_52_week
    except:
        potential_profit = 0

    async with lock:
        add_to_buffer(code, name, potential_profit=potential_profit)


def write_json(file, data):
    with open(file, "a") as f:
        json.dump(data, f, indent=4)
        # print(data['name'], 'parsed')


async def make_all(link, growth):
    html = await fetch_response(link)
    # response = await fetch_response(link)
    # print(response)
    # html = await response.text()
    # print(html)
    await get_page_data(html, growth)

    # write_json(data)


def write_results(
    func,
    top_10_price=[],
    top_10_PE=[],
    top_10_growth=[],
    top_10_potential_profit=[],
    write_to_file=None,
):

    tops = {
        "price": top_10_price,
        "P/E": top_10_PE,
        "growth": top_10_growth,
        "potential profit": top_10_potential_profit,
    }

    if write_to_file:
        for key, value in tops.items():
            write_json("Top_10_" + key + ".json", value)

    def wrapper(code, name, price=None, PE=None, growth=None, potential_profit=None):
        if price:
            return func(code, name, price, tops["price"], "price")
        if PE:
            return func(code, name, -PE, tops["P/E"], "P/E")
        if growth:
            return func(code, name, growth, tops["growth"], "growth")
        if potential_profit:
            return func(
                code,
                name,
                potential_profit,
                tops["potential profit"],
                "potential profit",
            )

    return wrapper


@write_results
def add_to_buffer(code, name, parameter, top, delete_it):
    print(delete_it, ":", top, "\n")
    if top == []:
        top.append({code, name, parameter})

    elif len(top) < 10:
        my_insert(code, name, parameter, top)
    elif parameter > top[-1][-1]:
        top.pop()
        my_insert(code, name, parameter, top)


def my_insert(code, name, parameter, top):
    if parameter >= top[0][-1]:
        top.insert(0, {code, name, parameter})
    elif parameter > top[-1][-1]:
        i = -2
        while parameter >= top[i][-1]:
            i -= 1
        top.insert(i, {code, name, parameter})


def just_function():
    pass


async def main():
    start = datetime.now()
    url = "https://markets.businessinsider.com/index/components/s&p_500"
    # all_companies = [(link, growth)
    #                  for link, growth in get_all_links(get_html(url))]

    with open("index.html") as f:
        html = f.read()

    tasks = [
        asyncio.create_task(make_all(link, growth))
        for link, growth in get_all_links_and_growth(html)
    ]

    # all_companies = [[link, growth]
    #                  for link, growth in get_all_links_and_growth(html)]

    # tasks = [asyncio.create_task(make_all(link, growth))
    #          for link, growth in get_all_links_and_growth(get_html(url))]

    await asyncio.gather(*tasks)

    write_results(just_function, write_to_file=True)

    # with ThreadPoolExecutor() as p:
    #     write_results(p.map(make_all, all_companies))

    end = datetime.now()
    total = end - start
    print(str(total))


if __name__ == "__main__":
    asyncio.run(main())
