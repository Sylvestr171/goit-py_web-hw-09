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
    for i in content:
        print(i.find("span", class_='text').string)
        print(i.find("small", class_='author').string)
        print(i.find_all("a", class_='tag'))
    # match = re.search(r'var data\s*=\s*(\[\s*{.*?}\s*\]);', content, re.DOTALL)
    # data.extend(json.loads(match.group(1)))

#     if soup.find('li', class_="next"):
#         link_button = soup.find('li', class_="next").find("a")
#         next_link = link_button["href"]
#         next_page_url = START_URL + next_link
#         print (next_page_url)
#         return get_data(next_page_url)
#     else:
#         return data

# date_for_json = list()

get_data(url)

# for n in data:
#     dict_for_date = {'tags': None,'author': None,'quote': None}
#     dict_for_date['tags'] = n['tags']
#     dict_for_date['author'] =  n['author']['name']
#     dict_for_date['quote'] = n['text']
#     date_for_json.append(dict_for_date)

# with open("qoutes.json", "w", encoding="utf-8") as f:
#     json.dump(date_for_json, f, ensure_ascii=False, indent=2)

