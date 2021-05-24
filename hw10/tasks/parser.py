from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import json
from datetime import datetime
from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

tasks = [asyncio.create_task(fetch_response(url))]

await asyncio.gather(*tasks)

await response.text()


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


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    code_name_price_area = soup.find('div', class_="price-section__row")

    try:
        code = code_name_price_area.find(
            class_="price-section__category").find_next().text[2:]
    except:
        code = ''

    try:
        name = code_name_price_area.find(
            class_="price-section__label").text[:-1]
    except:
        name = ''

    try:
        price = convert(code_name_price_area.find(
            class_="price-section__current-value").text)
    except:
        price = ''

    try:
        PE = to_float(soup.find(
            'div', class_="snapshot__data-item").find(text=True, recursive=False))

    except:
        PE = ""

    try:
        low_52_week = to_float(
            soup.find(class_="snapshot__data-item snapshot__data-item--small").find(text=True, recursive=False))

        high_52_week = to_float(soup.find(
            class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right").find(text=True, recursive=False))
        potential_profit = (high_52_week - low_52_week) * 100 / low_52_week
    except:
        potential_profit = ''

    data = {'code': code, 'name': name, 'price': price,
            "P/E": PE, "potential profit": potential_profit}
    return data


def write_json(data):
    with open('example.json', 'a') as f:
        json.dump(data, f, indent=4)
        # print(data['name'], 'parsed')


def make_all(my_list):
    link, growth = my_list

    tasks = [asyncio.create_task(fetch_response(link))]

    await asyncio.gather(*tasks)

    await response.text()
    html = get_html(link)
    data = get_page_data(html)
    data["growth"] = growth

    return data

    # write_json(data)


async def write_results(data, top_10_price=[], top_10_PE=[],
                        top_10_growth=[], top_10_potential_profit=[]):
    tops = dict(('price',"P/E" "potential profit"),(top_10_price, top_10_PE, top_10_potential_profit)):
        add_to_buffer(data, top, parameter)


def add_to_buffer(data, top, parameter):
    if len(top) < 10:
        top.append({data['code'], data['name'], data[parameter]})
    elif data[parameter] >= top[0]:
            top.pop()
            top.insert(0, data[parameter])
    elif data[parameter] > top[-1]:
        i = -2
        while data[parameter] >= top[i]:
            i -= -1
        top.pop()
        top.insert(i+1, data[parameter] )











def main():
    start = datetime.now()
    url = 'https://markets.businessinsider.com/index/components/s&p_500'
    # all_companies = [(link, growth)
    #                  for link, growth in get_all_links(get_html(url))]

    with open('index.html') as f:
        html = f.read()

    all_companies = [[link, growth]
                     for link, growth in get_all_links_and_growth(html)]
    result = []






    # with ThreadPoolExecutor() as p:
    #     write_results(p.map(make_all, all_companies))

    end = datetime.now()
    total = end - start
    print(str(total))
    print(result)


if __name__ == '__main__':
    main()
