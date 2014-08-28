# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.Item import Item,Field

class PDFItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title=Field()
	link=Field()
	desc=Field()
    pass
