import io
import ssl
import urllib.request
import PyPDF2
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# allowed extensions
from search_engine.models import CrawlingQueue
from ..pipelines import CrawlingPipeline
from ..items import CrawlingItem

# from search_engine.models import CrawlingQueue

ALLOWED_EXTENSIONS = [".pdf"]


# StrategyLinkExtractor subclasses LinkExtractor
class StrategyLinkExtractor(LinkExtractor):
    def __init__(self, *args, **kwargs):
        super(StrategyLinkExtractor, self).__init__(*args, **kwargs)
        # leaving default values in "deny_extensions" other than the ones we want.
        self.deny_extensions = [ext for ext in self.deny_extensions if ext not in ALLOWED_EXTENSIONS]


# ContentSpider subclasses CrawlSpider
class ContentSpider(CrawlSpider):
    name = "content"  # spider

    items = CrawlingItem()
    start_urls = []

    # useful links for crawling:
    # 'https://www.imagescape.com/media/uploads/zinnia/2018/08/20/scrape_me.html',
    # book
    # https://codex.cs.yale.edu/avi/os-book/OSE2/index.html,
    # review ques
    # https://codex.cs.yale.edu/avi/os-book/OSE2/review-dir/index.html,
    # practice questions
    # https://codex.cs.yale.edu/avi//os-book/OS9/practice-exer-dir/index.html,
    # 311db -practice exercises
    # https://www.db-book.com/Practice-Exercises/index-solu.html,

    def __init__(self, *args, **kwargs):

        self.get_objects_in_queue()

        # Follows the rule set in StrategyLinkExtractor class
        # parse() method is used for parsing the data
        # CrawlSpider-based spiders have internal implementation, so we explicitly set callbacks for new requests to avoid unexpected behaviour
        self.rules = (
        Rule(StrategyLinkExtractor(), follow=True, callback="parse", process_links=None, process_request=None,
             errback=None),)
        super(ContentSpider, self).__init__(*args, **kwargs)

    def set_urls(self, urltext):
        urls_list = urltext.split(",")
        for url in urls_list:
            url = url.strip()  # trims whitespace
            self.start_urls.append(url)

    def get_objects_in_queue(self):
        objects_in_queue = CrawlingQueue.objects.all()  # fetches all objects from DB table
        for object_in_queue in objects_in_queue:
            self.items['clustername'] = object_in_queue.clusterName  # attributes of the objects are to items
            self.items['username'] = object_in_queue.userName
            self.set_urls(object_in_queue.url)
            print(self.start_urls)

    # parse() processes response and returns scraped data
    def parse(self, response):
        self.logger.info('Yippy! We have found: %s', response.url)  # shows a message with response
        if hasattr(response, "text"):
            pass  # we disregard any HTML text
        else:
            # filtering out extensions that are in our ALLOWED_EXTENSIONS list from the list of returned urls
            extension = list(filter(lambda x: response.url.lower().endswith(x), ALLOWED_EXTENSIONS))[0]
            if extension:  # if extensions are found
                # writing the scraped URLs in the text file in append mode
                self.items['link'] = str(response.url)
                # bypassing ssl
                ssl._create_default_https_context = ssl._create_unverified_context
                # calling urllib to create a reader of the pdf url
                r = urllib.request.urlopen(response.url)
                reader = PyPDF2.pdf.PdfFileReader(io.BytesIO(r.read()))

                # creating data string by scanning pdf pages
                data = ""
                for datas in reader.pages:
                    data += datas.extractText()
                # print(data)  #prints content in terminal

                self.items['content'] = str(data)
                yield self.items
