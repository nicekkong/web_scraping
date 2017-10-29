from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(), 'utf-8'))


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")

content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "utf-8")
content = content.decode("utf-8")

print(content)