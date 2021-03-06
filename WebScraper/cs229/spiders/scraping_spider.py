'''
Made by : Amitoj Kaur Chawla
Date: 01 September 2014
'''

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from cs229.items import Cs229Item
from scrapy.item import Item, Field
##from scrapy.selector import HtmlXPathSelector

class Cs229Spider(CrawlSpider):
    name = "cs229"
    allowed_domains = ["cs229.stanford.edu"]
    start_urls = [ ## url to download pdf files from
        "http://cs229.stanford.edu/projects2013.html"
    ]
    pdf_urls=['http://cs229.stanford.edu/proj2013/CamenzindGoel-jazz_Automatic_Music_Genre_Detection.pdf',
	'http://cs229.stanford.edu/proj2013/SchusterZhuCheng-PredictingTagsforStackOverflowQuestions.pdf']
    rules = (Rule(SgmlLinkExtractor(allow_domains=('http://cs229.stanford.edu/projects2013.html', )), callback='parse_urls', follow=True), )
	

def parse_urls(self, response):
	'''hxs=HtmlXPathSelector(response) ##extracting xpath
	item=Cs229Item()'''
	yield Cs229Item(
	pdf_urls=['http://cs229.stanford.edu/proj2013/CamenzindGoel-jazz_Automatic_Music_Genre_Detection.pdf',
	'http://cs229.stanford.edu/proj2013/SchusterZhuCheng-PredictingTagsforStackOverflowQuestions.pdf']
)
	for url in pdf_urls:
        	open(url, 'wb').write(response.body) 
'''	##hxs.select('//a/@href')
	pdf_urls=hxs.select('//a/@href').extract()
	for url in pdf_urls :
		yield scrapy.Request(url,callback=self.save_pdf)

def save_pdf(self,response): 
	## save pdf files
	path=self.get_path(item['url'])
	with open(path,"wb") as f:
		f.write(response.body) 

'''
