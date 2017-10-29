from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup


try :
    html = urlopen("http://www.nicekkofdfdng.com/test.jsp")
    print ("try done~!!")
except HTTPError as e :
    print("except")
else :
    print ("else clause")

