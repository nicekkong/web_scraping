from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

images = bsObj.find("img", {"src":re.compile("\.\./img/gifts/img.*\.jpg")})


lam = bsObj.findAll(lambda tag : len(tag.attrs) ==2)

for img in lam:
    print("\n====================================")
    print(img)
    print("====================================\n")


