from scrapy.contrib.spiders import DmozSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtarctor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Items
from scraper.items import Item

class CSSpider(DmozSpider):
	name="cs229"
	allowed_domains=["cs229.stanford.edu"]
	start_urls=[
	"http://cs229.stanford.edu/projects2013.html",
        "http://cs229.stanford.edu/projects2012.html"]
	rules=(Rule(SgmlLinkExtractor(allow=(r'\.pdf',)restrict_xpaths('//a')),callback='parse_listing',follow='True'),)

def parse_listing(self,response):
	hxs=HtmlXPathSelector(response)
	items=PDFItem()	
	pdf_urls=hxs.select('//a')
	for url in pdf_urls:
		yield Request(url,callback=self.save_pdf)

	return items
'''
	for site in sites:
		item=PDFItem()
		item['title']=site.select('a/text()').extract()
		item['link']=site.select('a/@href').extract()
		item['desc'] = site.select('text()').extract()
		items.append(item)
	return items
'''
spider=CSSpider()
	
def save_pdf(self,response):
	path=self.get_path(response.url)
	with open(path,"wb") as f:
		f.write(response.body)
