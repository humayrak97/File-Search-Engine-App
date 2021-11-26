import scrapy
import textract
from itertools import chain
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#allowing extensions 
TEXTRACT_EXTENSIONS = [".pdf", ".doc", ".docx", ""]

#custom link extractor
class CustomLinkExtractor(LinkExtractor):
    def __init__(self, *args, **kwargs):

#ContentSpider subclasses scrapy.Spider
class ContentSpider(scrapy.Spider):
     name = "content"  #spider

     def start_requests(self):
         urls = [	#urls to be crawled 
             'https://www.imagescape.com/media/uploads/zinnia/2018/08/20/scrape_me.html', 
	     'https://www.northsouth.edu',
         ]
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)

     class scrapy.link.Link(url, text='', fragment='', nofollow=False)
     def parse(self, response):
         for link in self.link_extractor.extract_links(response):
             #yield Request(link.url, callback=self.parse)
	     #writing the scraped content in the text file
             with open('scraped.txt','wb') as f:  
                 f.write(response.url.upper())
                 f.write("\n")
                 f.write(extracted_data)
                 f.write("\n\n")

