from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json


hostUrl = "http://namu.wiki"

html = urlopen(hostUrl + "/RecentChanges")
bsObj = BeautifulSoup(html, "html.parser")

recentUrl = bsObj.find("table", {"class" : "table table-hover"})\
    .findAll("a", href=re.compile("^(/w/)"))

recentUrls = []
for row in recentUrl:
    print("{0:<20} : {1}".format(row.get_text(), hostUrl + row.attrs["href"]))
    recentUrl = {'title' : row.get_text(),
                 'url' : hostUrl + row.attrs["href"]
                 }
    recentUrls.append(recentUrl)


result = {'recentUrls' : recentUrls}

print(json.dumps(result))