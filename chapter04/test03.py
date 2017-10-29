from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
from urllib.error import HTTPError
import json

random.seed(datetime.datetime.now())

def                      getLinks(articleUrl):

    url = "http://en.wikipedia.org"+articleUrl
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")

    div_attr = {"id" : "bodyContent"}

    return bsObj.find("div", div_attr)\
        .findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
    historyUrl += pageUrl + "&action=history"
    print("history url is : " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    ipAddresses= bsObj.findAll("a", {"class":"mw-anonuserLink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())

    return addressList

#
# links = getLinks("/wiki/Python_(programming_language)")
#
# while(len(links) > 0):
#     for link in links:
#         print("******************************************")
#         historyIPs = getHistoryIPs(link.attrs["href"])
#         for historyIP in historyIPs:
#             print(historyIP)
#
#     newLink=links[random.randint(0, len(links)-1)].attrs["href"]
#     links = getLinks(newLink)




def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress.read().decode('utf-8'))
    except HTTPError:
        return None
    responseJson = json.loads(response)

    return responseJson.get("country_code")


links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0) :
    for link in links:
        print("============================================")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from " + country)

newLink = links[random.randint(0, len(links)-1)].attr["href"]
links = getLinks(newLink)
