import re
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

START_URL = 'https://quotes.toscrape.com'

next_link = ''
url = START_URL + next_link
# data = []
# about_links = list()

def get_data(url):
    print (url)
    html_doc = requests.get(url)
    if html_doc.status_code==200:
        print (html_doc.status_code)
        get_data_soup = BeautifulSoup(html_doc.text, 'html.parser')
    else:
        print(f"Error, status code >>> {html_doc.status_code}")
    return get_data_soup

def analisis_main_page(soup, data_in_foo=list(), about_links_in_foo=list()):
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
    data_in_foo.extend(data_for_json)

    for link in soup.find_all('a', string="(about)"):
        if link["href"] not in about_links_in_foo:
            about_links_in_foo.append(link["href"])
    
    
    if soup.find('li', class_="next"):
        link_button = soup.find('li', class_="next").find("a")
        next_link = link_button["href"]
        next_page_url = START_URL + next_link
        return analisis_main_page(get_data(next_page_url), data_in_foo, about_links_in_foo)
    else:
        return data_in_foo, about_links_in_foo
        

def analis_autor_page(soup):
    dict_for_data = {'fullname': None,'born_date': None,'born_location': None, 'description': None}
    dict_for_data['fullname'] = soup.find("h3", class_='author-title').text
    dict_for_data['born_date'] = soup.find("span", class_='author-born-date').string
    dict_for_data['born_location'] = soup.find("span", class_='author-born-location').string 
    dict_for_data['description'] = soup.find("div", class_='author-description').string.strip()
    return dict_for_data
    

data, about_links = analisis_main_page(get_data(url))

def write_file(name_of_file, data_for_write):
    with open(name_of_file, "w", encoding="utf-8") as f:
        json.dump(data_for_write, f, ensure_ascii=False, indent=2)
    return print(f"{name_of_file} was print successfull")

write_file("qoutes.json", data)
# with open("qoutes.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

data_about = list()
for ithem in about_links:
    data_about.append(analis_autor_page(get_data(START_URL+ithem)))

write_file("authors.json", data_about)
# with open("authors.json", "w", encoding="utf-8") as f:
#     json.dump(data_about, f, ensure_ascii=False, indent=2)
