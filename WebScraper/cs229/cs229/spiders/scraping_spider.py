from scrapy.spider import BaseSpider
from cs229.items import Cs229Item
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector

class Cs229Spider(BaseSpider):
    name = "cs229"
    allowed_domains = ["cs229.stanford.edu"]
    start_urls = [
        "http://cs229.stanford.edu/projects2013.html"
    ]

def parse(self, response):
	filename = response.url.split("/")[-2]
	pdf_urls=hxs.select('//a/@href').extract()  
	for url in pdf_urls :	
		yield Request(url,callback=self.save_pdf)

def save_pdf(self,response):
	path=self.get_path(item['url'])
	with open(path,"wb") as f:
		f.write(response.body) 