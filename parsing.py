# from pprint import pprint
import requests
from bs4 import BeautifulSoup


class Parser:
    __URl = 'https://www.binance.com/ru/markets'
    __HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    @classmethod
    def __get_html(cls, url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URl, headers=cls.__HEADERS)
        return req

    @staticmethod
    def __get_data(html):
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



    @classmethod
    def parser(cls):
        html = cls.__get_html()
        if html.status_code == 200:
            crypto = []
            for i in range(1, 2):
                html = cls.__get_html()
                current_page = cls.__get_data(html.text)
                crypto.extend(current_page)
            return crypto
        else:
            raise Exception("Bad request!")



