from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.nicekkong.com")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.div)