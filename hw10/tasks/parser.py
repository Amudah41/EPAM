import json

import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main_page_parsing(url):
    html = await fetch_response(url)
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find("tbody", class_="table__tbody")
    for link, growth in get_all_links_and_growth(tds):
        company_page_parsing(await fetch_response(link), growth)


def get_all_links_and_growth(tds):
    while tds := tds.find_next("tr"):
        a = tds.find("td", class_="table__td table__td--big").find("a").get("href")
        link = "https://markets.businessinsider.com" + a
        growth = to_float(
            tds.find_all(class_="table__td")[-1].find_all("span")[-1].text[:-1]
        )

        yield link, growth


def company_page_parsing(html, growth):
    soup = BeautifulSoup(html, "lxml")

    code = (
        soup.find("div", class_="price-section__row")
        .find(class_="price-section__category")
        .find_next()
        .text[2:]
    )

    name = (
        soup.find("div", class_="price-section__row")
        .find(class_="price-section__label")
        .text[:-1]
    )

    add_to_buffer(code, name, growth, "growth")

    price = convert(
        soup.find("div", class_="price-section__row")
        .find(class_="price-section__current-value")
        .text
    )

    add_to_buffer(code, name, price, "price")

    PE = to_float(
        soup.find("div", class_="snapshot__data-item").find(text=True, recursive=False)
    )

    add_to_buffer(code, name, -PE, "PE")

    low_52_week = soup.find(
        class_="snapshot__data-item snapshot__data-item--small"
    ).find(text=True, recursive=False)

    high_52_week = soup.find(
        class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right"
    ).find(text=True, recursive=False)

    if all((low_52_week, high_52_week)):
        low_52_week = to_float(low_52_week)
        add_to_buffer(
            code,
            name,
            round((to_float(high_52_week) - low_52_week) * 100 / low_52_week, 2),
            "potential_profit",
        )


def write_results(
    func,
    top_10_price=[],
    top_10_PE=[],
    top_10_growth=[],
    top_10_potential_profit=[],
    write_to_file=False,
):
    tops = {
        "price": top_10_price,
        "PE": top_10_PE,
        "growth": top_10_growth,
        "potential_profit": top_10_potential_profit,
    }

    if write_to_file:
        for key, value in tops.items():
            write_json("./hw10/Top_10_" + key + ".json", value)

    def wrapper(code, name, param, param_name):
        return func(code, name, param, tops[param_name], param_name)

    return wrapper


@write_results
def add_to_buffer(code, name, param, top, param_name):
    if not top:
        top.append({"code": code, "name": name, param_name: param})

    elif param >= top[0][param_name]:
        if len(top) == 10:
            top.pop()
        top.insert(0, {"code": code, "name": name, param_name: param})

    elif len(top) < 10:
        if param < top[-1][param_name]:
            top.append({"code": code, "name": name, param_name: param})
            return

        i = -1
        while param >= top[i][param_name]:
            i -= 1
        top.insert(i + 1, {"code": code, "name": name, param_name: param})

    elif param > top[-1][param_name]:
        i = -1
        while param >= top[i][param_name]:
            i -= 1
        top.insert(i + 1, {"code": code, "name": name, param_name: param})
        top.pop()


def actual_exchange_rate_page_parsing(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.find("valute", id="R01235").find("value").text


def to_float(number: str):
    try:
        return float(number.replace(",", "."))
    except ValueError:
        return float(number.replace(",", "", (len(number) - 4) // 3).replace(",", "."))


def actual_USD(func):
    def wrapper(price):

        return func(to_float(price), USD)

    USD = to_float(
        actual_exchange_rate_page_parsing(
            requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
        )
    )

    return wrapper


@actual_USD
def convert(price, USD):
    return round(price * USD, 2)


def write_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def pass_function():
    pass


async def main():
    url = "https://markets.businessinsider.com/index/components/s&p_500?p="
    tasks = [
        asyncio.create_task(main_page_parsing(url + str(page))) for page in range(1, 11)
    ]
    await asyncio.gather(*tasks)

    write_results(pass_function, write_to_file=True)


if __name__ == "__main__":
    ...

    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(main())

    # total time of parsing: 0:02:40.799727
    # Download speed: 21.28 Mb/s
    # Upload Speed : 28.65 Mb/s
