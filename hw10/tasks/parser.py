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
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('tbody', class_='table__tbody')

    while tds := tds.find_next('tr'):
        a = tds.find(
            'td', class_='table__td table__td--big').find('a').get('href')
        link = 'https://markets.businessinsider.com' + a
        growth = to_float(tds.find_all(
            class_='table__td')[-1].find_all('span')[-1].text[:-1])

        yield link, growth


def actual_exchange_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.find('valute', id="R01235").find('value').text


def to_float(number: str):
    try:
        number = number.replace(",", '')
        return float(number)
    except ValueError as err:
        raise err(f"Can't convert {number} to float.")


def convertion_USD_to_RUB(func):
    def wrapper(price):

        return func(to_float(price), USD)

    USD = to_float(actual_exchange_rate(
        get_html('http://www.cbr.ru/scripts/XML_daily.asp')))

    return wrapper


@convertion_USD_to_RUB
def convert(price, USD):
    return price * USD


async def get_page_data(html, growth):
    soup = BeautifulSoup(html, 'lxml')
    lock = asyncio.Lock()

    # code_name_price_area = soup.find('div', class_="price-section__row")

    code = soup.find('div', class_="price-section__row").find(
        class_="price-section__category").find_next().text[2:]

    name = soup.find('div', class_="price-section__row").find(
        class_="price-section__label").text[:-1]

    async with lock:
        add_to_buffer(code, name, growth, "growth")

    price = convert(soup.find('div', class_="price-section__row").find(
        class_="price-section__current-value").text)

    async with lock:
        add_to_buffer(code, name, price, 'price')

    PE = to_float(soup.find(
        'div', class_="snapshot__data-item").find(text=True, recursive=False))

    async with lock:
        add_to_buffer(code, name, -PE, 'PE')

    low_52_week = to_float(
        soup.find(class_="snapshot__data-item snapshot__data-item--small").find(text=True, recursive=False))

    high_52_week = to_float(soup.find(
        class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right").find(text=True, recursive=False))
    potential_profit = (high_52_week - low_52_week) * 100 / low_52_week

    async with lock:
        add_to_buffer(code, name, potential_profit, "potential_profit")


def write_json(file, data):
    with open(file, 'a') as f:
        json.dump(data, f, indent=4)
        print(f'{file} completed!')


async def make_all(link, growth):
    html = await fetch_response(link)
    # response = await fetch_response(link)
    # print(response)
    # html = await response.text()
    # print(html)
    await get_page_data(html, growth)  # нужна ли здесь ассинхроность - ???

    # write_json(data)


def write_results(func, top_10_price=[], top_10_PE=[],
                  top_10_growth=[], top_10_potential_profit=[], write_to_file=False):

    tops = {'price': top_10_price, "PE": top_10_PE,
            "growth": top_10_growth, "potential_profit": top_10_potential_profit}

    if write_to_file:
        for key, value in tops.items():
            write_json('Top_10_' + key + '.json', value)

    def wrapper(code, name, param, param_name):
        return func(code, name, param, tops[param_name])

    return wrapper


@write_results
def add_to_buffer(code, name, param, top):
    if top == []:
        top.append([code, name, param])

    elif param >= top[0][-1]:
        if len(top) == 10:
            top.pop()
        top.insert(0, [code, name, param])

    elif len(top) < 10:
        if param < top[-1][-1]:
            top.append([code, name, param])
            return

        i = -1
        while param >= top[i][-1]:
            i -= 1
        top.insert(i + 1, [code, name, param])

    elif param > top[-1][-1]:
        i = -1
        while param >= top[i][-1]:
            i -= 1
        top.insert(i + 1, [code, name, param])
        top.pop()


def pass_function():
    pass


async def main():
    start = datetime.now()
    url = 'https://markets.businessinsider.com/index/components/s&p_500'

    # with open('index.html') as f:
    #     html = f.read()

    # tasks = [asyncio.create_task(make_all(link, growth))
    #          for link, growth in get_all_links_and_growth(html)]

    # all_companies = [[link, growth]
    #                  for link, growth in get_all_links_and_growth(html)]

    tasks = [asyncio.create_task(make_all(link, growth))
             for link, growth in get_all_links_and_growth(get_html(url))]

    await asyncio.gather(*tasks)

    write_results(pass_function, write_to_file=True)

    end = datetime.now()
    total = end - start
    print(str(total))


if __name__ == '__main__':
    asyncio.run(main())
    # 0:00:16.436560