from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikidedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "https://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title :::::: " + title)

        items = dict()
        item['title'] = title

        item_list = list()
        item_list.append(item)

        items['items'] = item_list

        return items


