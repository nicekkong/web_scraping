from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")


index = 1
for child in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print("\n", index, "//=========================")
    print(child)
    print(index, "=========================//\n")
    index = index+1

print(index)