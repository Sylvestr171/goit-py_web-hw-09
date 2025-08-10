import re
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

START_URL = 'https://quotes.toscrape.com/js'

next_link = ''
url = START_URL + next_link
html_doc = requests.get(url)
if html_doc.status_code==200:
    print (html_doc.status_code)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
else:
    print(f"Error, status code >>> {html_doc.status_code}")

content = soup.find("script", string=re.compile('var data =')).string
match = re.search(r'var data\s*=\s*(\[\s*{.*?}\s*\]);', content, re.DOTALL)
data = json.loads(match.group(1))

date_for_json = list()

for i in data:
    dict_for_date = {'tags': None,'author': None,'quote': None}
    dict_for_date['tags'] = i['tags']
    dict_for_date['author'] =  i['author']['name']
    dict_for_date['quote'] = i['text']
    date_for_json.append(dict_for_date)

with open("qoutes.json", "w", encoding="utf-8") as f:
    json.dump(date_for_json, f, ensure_ascii=False, indent=2)


if soup.find('li', class_="next"):
    link_button = soup.find('li', class_="next").find("a")
    next_link = link_button["href"]
    next_page_url = START_URL + next_link
