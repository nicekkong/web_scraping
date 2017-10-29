from urllib.error import HTTPError
from urllib.request import urlopen
import json

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress.read().decode('utf-8'))
    except HTTPError:
        return None
    responseJson = json.loads(response)

    return responseJson.get("country_code")

links = getLinks("/wikiPython_(programming_language)")


