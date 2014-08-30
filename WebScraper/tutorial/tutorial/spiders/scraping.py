from scrapy.selector import HtmlXPathSelector
from scrapy.spider import Spider
from tutorial.items import PDFItem


class CSSpider(BaseSpider):
	name="cs229"
	allowed_domains=["cs229.stanford.edu"]
	start_urls=[
	"http://cs229.stanford.edu/projects2013.html",
        "http://cs229.stanford.edu/projects2012.html"]
	

def parse(self,response):
	hxs=HtmlXPathSelector(response)
	items=PDFItem()	
	pdf_urls=hxs.select('//a')
	for url in pdf_urls:
		item["pdf_urls"]=url.select('//a[contains(@href, "proj")]/@href').extract()
		yield Request(url,callback=self.save_pdf)

	


def save_pdf(self,response):
	path=self.get_path(response.url)
	with open(path,"wb") as f:
		f.write(response.body)
