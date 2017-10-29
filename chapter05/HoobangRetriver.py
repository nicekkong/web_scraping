import requests
from urllib.request import urlretrieve
import os
from bs4 import BeautifulSoup
import json

DOWNLOAD_DIR = 'my_download'
BASE_URL = "https://www.clien.net"

# 파일 이름만 추출한다.
def extractFileName(fullSrc):
    fileName = fullSrc.replace("https://cdn.clien.net/web/api/file/", "")[12:30]
    return fileName

# 게시물에서 이미지 경로만 찾는다.
def searchImages(targetUrl, isSaveToLocal):
    postContent = targetUrl.find("div", {"class": "post-content"})
    imageUrls = postContent.findAll("img")

    images = []
    for url in imageUrls :
        imageSrc = url.attrs["src"]
        print(imageSrc)
        images.append(imageSrc)
        # 로컬 저장 모드일때만 로컬에 저장한다.
        if isSaveToLocal:
            urlretrieve(imageSrc, DOWNLOAD_DIR + "/" + extractFileName(imageSrc))

    return images


# 해당 링크 추출
def getSubLinks(bulletin_links):
    # JSON 결과값 리턴
    bulletin_list = []
    bulletin_dics = {}
    for link in bulletin_links:
        print(link.get_text().strip())
        print(BASE_URL + link.attrs["href"])
        hoobangUrl = BASE_URL + link.attrs["href"]
        hoobangBsObj = BeautifulSoup(requests.get(hoobangUrl).text, "html.parser")

        # 로컬 디렉토리에 파일 저장 (로컬에 해당 이미지 저장 여부)
        images = searchImages(hoobangBsObj, isSaveToLocal=False)

        subInfo = {
            "title" : link.get_text().strip(),
            "url" : BASE_URL + link.attrs["href"],
            "imageUrls" : images
        }

        bulletin_list.append(subInfo)
        bulletin_dics = {
            "subUrls" : bulletin_list
        }

    print("API Result ::::::::::::::::::::; ")
    print(json.dumps(bulletin_dics))
    return json.dumps(bulletin_dics)

# 검색어를 포함한 게시판 URL 생성
def makeHoobangUrl(searchWord):
    HOOBANG_URL = BASE_URL + "/service/board/park?sk=title&sv=" + searchWord + "&articlePeriod=2017"
    return HOOBANG_URL


url = requests.get(makeHoobangUrl("후방")) # 원하는 검색어를 입력한다.
bsObj = BeautifulSoup(url.text, "html.parser")

bulletin_links = bsObj.find("div", {"class" :"card-grid"}).findAll("a", {"class": "list-subject"})

# 디렉토리 만들기
if bulletin_links is not None:
    directory = os.path.dirname(DOWNLOAD_DIR)
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

getSubLinks(bulletin_links)