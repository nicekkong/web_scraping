from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

result = bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling

print(result.get_text())