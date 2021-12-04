# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    clustername = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    
