import os as op
import VeeQuestCrawler.VeeQuestCrawler.spiders.blogscrawler as crawler
from scrapy.crawler import CrawlerProcess
import os as os
import Constants

def getBlogs():
    """process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(crawler.QuotesSpider)
    process.start()"""
    files=os.listdir(Constants.base_file+"\\blogs")
    sentence=""
    for file in files:
        f=open(Constants.base_file+"\\blogs\\"+file,"r")
        try:
            for words in f:
                if type(words)==str:
                    sentence=sentence+words
        except UnicodeDecodeError:
            #print("Unicode decode error")
            continue
    return sentence
