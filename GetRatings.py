import re
import os as op
import VeeQuestCrawler.VeeQuestCrawler.spiders.flipkartcrawler as crawler
from scrapy.crawler import CrawlerProcess
import json
import Constants

def getRatings():
    """process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    })
    process.crawl(crawler.FlipkartSpider)
    process.start()"""
    file=open(Constants.base_file+"\\ScrapedPages\\FlipkartRatings\\Page.json", "r")
    data=json.load(file)
    return data
