import scrapy
import geturls as urls
import Constants

class QuotesSpider(scrapy.Spider):

    name = "FeaturesCrawler"

    def __init__(self, phoneName=None, *args, **kwargs):
        self.phone = phoneName
        super(QuotesSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        urllist = urls.geturllist(self.phone, "gsmarena")
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = Constants.base_file+'\\ScrapedPages\\gsmarenaFeatures\\Page.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
            print(response)
