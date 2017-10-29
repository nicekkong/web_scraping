from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

print(type(bsObj.findAll("a")))

i = 1

print("1)+++++++++++++++++++++++++++++++++++++++++++++++++")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

print("2)+++++++++++++++++++++++++++++++++++++++++++++++++")
for link in bsObj.find("div", {"id":"bodyContent"})\
        .findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    print(link.attrs['title'], " : " , link.attrs['href'])
