import scrapy
from src.scraping.items import ImageItem

# https://www.google.com/search?q=barack+obama&tbm=isch

class MySpider(scrapy.Spider):
    name = 'google.com'
    allowed_domains = ['google.com']
    start_urls = [
        # 'https://www.google.com/search?q=barack+obama&tbm=isch'
        "https://fr.wikipedia.org/wiki/Barack_Obama"
    ]

    def parse(self, response):
        print("--------------------------")
        print(response)
        item = ImageItem()

        img_urls = []
        url = 'https:' + '//upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/220px-President_Barack_Obama.jpg'
        # url = 'https:' + '//upload.wikimedia.org/wikipedia/commons/thumb/3/39/Honolulu01.JPG/280px-Honolulu01.JPG'
        img_urls.append(response.css('img').attrib['src'])
        # print(s)
        # for _ in response:
        #     img_urls.append()

        item["image_urls"] = [url]
        return item