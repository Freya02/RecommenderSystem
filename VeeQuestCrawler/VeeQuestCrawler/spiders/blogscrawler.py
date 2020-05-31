import scrapy
import geturls as urls
from inscriptis import get_text
import Constants

class QuotesSpider(scrapy.Spider):

    name="blogsCrawler"

    def __init__(self, phoneName=None, *args, **kwargs):
        self.phone=phoneName
        super(QuotesSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        urllist = urls.geturllist(self.phone+" blogs", "")
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = Constants.base_file+'\\blogs\\Page-%s.txt' % page
        resp = response.css("body").extract()
        output = get_text(resp[0])
        with open(filename, 'wb') as f:
            f.write(output.encode())
