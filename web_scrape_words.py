#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


# list of pages containing words with different themes
# link : https://www.enchantedlearning.com/wordlist/
words_page_names = ["astronomy", "positivewords", "languages", "metals", "usstates", "vegetables"]
synonym_words_page_names = ["big", "happy", "said"]
words_dict = {}

for page_name in words_page_names + synonym_words_page_names :
    # get URL request
    URL = "https://www.enchantedlearning.com/wordlist/" + page_name + ".shtml"
    page = requests.get(URL)

    # get page content in html format
    # aim is to get class names & type of tags
    soup = BeautifulSoup(page.content, "html.parser")

    words_list = []
    for sp in soup.find_all("div",class_="wordlist-item"):
        words_list.append(sp.text.lower())              #lower text for game purposes

    words_dict[page_name] = words_list
    print(words_list)

