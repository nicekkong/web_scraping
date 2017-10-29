from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://ko.wikipedia.org")
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.find(id="mw-content-text"))