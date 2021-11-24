import scrapy
from scrapy.linkextractors import LinkExtractor

#ContentSpider subclasses scrapy.Spider
class ContentSpider(scrapy.Spider):
     name = "content"  #spider

     def start_requests(self):
         urls = [
             
         ]
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)

     class scrapy.link.Link(url, text='', fragment='', nofollow=False)
     def parse(self, response):
         for link in self.link_extractor.extract_links(response):
             #yield Request(link.url, callback=self.parse)
             with open('scraped.txt','wb') as f: 
                 f.write(response.url.upper())
                 f.write("\n")
                 f.write(extracted_data)
                 f.write("\n\n")

