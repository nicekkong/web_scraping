from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.span
        print("title\n", title)
    except AttributeError as e:
        print(e)
        return None
    else :
        print ("else clause~~~")

    return title


title = getTitle("http://www.pythonscraping.com/pages/warandpeace.html")

if title==None:
    print("Title could not be found")
else:
    print(title)

#
# try :
#     html = urlopen("http://www.nicekkong.com")
#     bsObj2 = BeautifulSoup(html.read(), "html.parser")
#     print(bsObj2.div.p12345)
# except Exception as e:
#     print("==============================")
#     print(e)
#
