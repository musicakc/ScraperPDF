# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.http import Request
from scrapy.conf import settings

class Cs229Pipeline(FilesPipeline):
    def get_media_requests(self,item,info):
	return [Request(x) for x in item.get('pdf_urls',[])]
    def item_completed(self,results,item,info):
	item['files']=[x for ok,x in results if ok]

    
