import VeeQuestCrawler.VeeQuestCrawler.spiders.blogscrawler as crawler1
import VeeQuestCrawler.VeeQuestCrawler.spiders.featurecrawler as crawler2
import VeeQuestCrawler.VeeQuestCrawler.spiders.flipkartcrawler as crawler
from scrapy.crawler import CrawlerProcess

def callSpiders():
    self.phone=input("Enter the phone name:")

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    })
    process.crawl(crawler1.QuotesSpider,phoneName=self.phone)
    process.crawl(crawler2.QuotesSpider,phoneName=self.phone)
    process.crawl(crawler.FlipkartSpider,phoneName=self.phone)
    process.start()

def getPhone():
    return self.phone
