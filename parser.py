# shop_scraper.py
import requests
from bs4 import BeautifulSoup
import datetime
import urllib.request
import tkinter
import camelot
def monthToNum(shortMonth):
    return {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря"
    }[shortMonth]

now = datetime.datetime.now()

url = 'https://permaviat.ru/raspisanie-zamen/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='file_link')

for n, i in enumerate(items, start=1):
    itemName = i.find('div', class_='header').find('a').text.strip()
    if (str(itemName).__contains__(str(now.day + 1)) and str(itemName).__contains__(monthToNum(6))):
        print(f'Выложено расписание: {itemName}')
        link = i.find('div', class_='header').find('a').get("href")
        print(f"{url}{link}")
        urllib.request.urlretrieve(f"https://permaviat.ru{link}", "temp.pdf")
      
input()
