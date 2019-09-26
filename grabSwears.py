#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import re
import json

letter = 'c'

url = "https://www.noswearing.com/dictionary/{}".format(letter)

urlRequest = requests.get(url)

pageSoup = BeautifulSoup(urlRequest.content, "html.parser")
#pageSoup = BeautifulSoup(open("a.html", "r"), "html.parser")

block = pageSoup.find('td', {'valign':'top'})

words = re.findall(r"<b>(\w*?)</b> - (\w*?)<",str(block))


for word in words:
    print("{},{}".format(word[0], word[1]))