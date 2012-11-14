from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
   name = "reddit"
   allowed_domains = ["reddit.com"]
   start_urls = [
      "http://www.reddit.com/r/hookah",
      "http://www.reddit.com/r/askscience"
   ]

   def parse(self, response):
      filename = response.url.split("/")[-2]
      open(filename, 'wb').write(response.body)
