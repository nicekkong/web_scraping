from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

i = 0
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    i += 1
    print(i , "===================================")
    print(name.get_text())
    print("===================================\n")
