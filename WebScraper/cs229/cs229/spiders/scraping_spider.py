'''
Made by : Amitoj Kaur Chawla
Date: 01 September 2014
'''

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from cs229.items import Cs229Item
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector

class Cs229Spider(CrawlSpider):
    name = "cs229"
    allowed_domains = ["cs229.stanford.edu"]
    start_urls = [ ## url to download pdf files from
        "http://cs229.stanford.edu/projects2013.html"
    ]
    rules = (Rule(SgmlLinkExtractor(allow_domains=('http://cs229.stanford.edu/projects2013.html', )), callback='parse_urls', follow=True),) 

	

def parse_urls(self, response):
	hxs=HtmlXPathSelector(response) ##extracting xpath
	item=Cs229Item()
	item['pdf_urls']=hxs.select('//a/@href')
	pdf_urls=hxs.select('//a/@href').extract()
	for url in pdf_urls :
		yield scrapy.Request(url,callback=self.save_pdf)

def save_pdf(self,response): 
	## save pdf files
	path=self.get_path(item['url'])
	with open(path,"wb") as f:
		f.write(response.body) 


