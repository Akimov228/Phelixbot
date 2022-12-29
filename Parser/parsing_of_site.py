# from pprint import pprint
import requests
from bs4 import BeautifulSoup

URl = 'https://www.binance.com/ru/markets'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="css-vlibs4")
    crypto = []
    for item in items:
        coins = {
            'title': item.find('div', class_="css-1ap5wc6").getText(),
            'price': item.find('div', class_="css-ovtrou").getText(),
            'capital': item.find('div', class_="css-s779xv").getText()
                }
        crypto.append(coins)
    return crypto



#
# html = get_html(URl)
# get_data(html.text)

def parser():
    html = get_html(URl)
    if html.status_code == 200:
        crypto = []
        for i in range(1, 2):
            html = get_html(URl)
            current_page = get_data(html.text)
            crypto.extend(current_page)
        return crypto
    else:
        raise Exception("Bad request!")



