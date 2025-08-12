import re
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

START_URL = 'https://quotes.toscrape.com'

next_link = ''
url = START_URL + next_link
data = []

def get_data(url):
    html_doc = requests.get(url)
    if html_doc.status_code==200:
        print (html_doc.status_code)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
    else:
        print(f"Error, status code >>> {html_doc.status_code}")

    content = soup.find_all("div", class_='quote')
    data_for_json = list()
    for ithem in content:
        dict_for_data = {'tags': None,'author': None,'quote': None}
        dict_for_data['quote'] = ithem.find("span", class_='text').string
        dict_for_data['author'] = ithem.find("small", class_='author').string
        tags_list = list()
        for ithem_in_find_all in ithem.find_all("a", class_='tag'):
            tags_list.append(ithem_in_find_all.text)
        dict_for_data['tags'] = tags_list
        data_for_json.append(dict_for_data)
    data.append(data_for_json)

    if soup.find('li', class_="next"):
        link_button = soup.find('li', class_="next").find("a")
        next_link = link_button["href"]
        next_page_url = START_URL + next_link
        print (next_page_url)
        return get_data(next_page_url)
    else:
        return data

get_data(url)

with open("qoutes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

