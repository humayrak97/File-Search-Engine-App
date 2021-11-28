import scrapy
import textract
from itertools import chain
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#allowing extensions 
EXTENSIONS = [".pdf", ".doc", ".docx", ""]

#custom link extractor
class CustomLinkExtractor(LinkExtractor):
    def __init__(self, *args, **kwargs):
	 super(CustomLinkExtractor, self).__init__(*args, **kwargs)
        # leaving default values in "deny_extensions" other than the ones we want.
        self.deny = [ext for ext in self.deny if ext not in EXTENSIONS]


#ContentSpider subclasses scrapy.Spider
class ContentSpider(scrapy.Spider):
     name = "content"  #spider

     def init(self, *args, kwargs):
        self.rules = (Rule(CustomLinkExtractor(), follow=Flase, callback="parse_item"),)
        super(ContentSpider, self).init(*args, **kwargs)

     def start_requests(self):
         urls = [	#urls to be crawled 
             'https://www.imagescape.com/media/uploads/zinnia/2018/08/20/scrape_me.html', 
	     'https://www.northsouth.edu',
         ]
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)

     class scrapy.link.Link(url, text='', fragment='', nofollow=False)
     def parse(self, response):
	extension = list(filter(lambda x: response.url.lower().endswith(x), EXTENSIONS))[0] #if extensions are found
          if hasattr(response, "text"):
            pass
         else:
	     EXTENSIONS
             extension = list(filter(lambda x: response.url.lower().endswith(x), EXTENSIONS))[0]
             if extensions 
	      #writing the scraped content in the text file
              with open('scraped.txt','wb') as f:  
                 f.write(response.url.lower())  #converting feteched urls to lower case
                 f.write("\n")
                 f.write(extracted_data)
                 f.write("\n\n")

