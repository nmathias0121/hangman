#!/usr/bin/python3
import os
import shutil
import time
import requests
from bs4 import BeautifulSoup


# list of pages containing words with different themes
# link : https://www.enchantedlearning.com/wordlist/
words_page_names = ["astronomy", "positivewords", "languages", "metals", "usstates", "vegetables"]
synonym_words_page_names = ["big", "happy", "said"]
words_dict = {}

# make directory to store words in files if does not exist already
if not os.path.isdir('words/') :
    os.mkdir('words/')
else:
    shutil.rmtree('words/')
    time.sleep(3)           #time to delete files in dir & the dir itsellf
    os.mkdir('words/')

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

    # write all words with same theme in separate file
    with open('words/' + page_name + '.txt', "w") as file:
        for word in words_list:
            file.write(word + '\n')

