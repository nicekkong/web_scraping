import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen("http://www.pythonscraping.com")


html = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon").text
bsObj = BeautifulSoup(html, "html.parser")

content = bsObj.find("div", {"class" : "field-items"}).find("div", {"class":"field-item even"}).get_text()

print(content)

