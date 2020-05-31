import scrapy
import geturls as urls
import re
import json
import Constants

global urll,flipfetaures
urll=""
flipfetaures={}


class FlipkartSpider(scrapy.Spider):

    name = "FlipkartCrawler"

    def __init__(self, phoneName=None, *args, **kwargs):
        self.phone = phoneName
        super(FlipkartSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        urllist = urls.geturllist(self.phone,"flipkart")
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.logged_in)

    def logged_in(self, response):
        tags = response.css("text.PRNS4f::text").extract()
        overall = response.css("div._1i0wk8::text").extract()

        flipfetaures["Overall"] = overall[0]
        flipfetaures["Camera"] = tags[0]
        flipfetaures["Battery"] = tags[1]
        flipfetaures['Display'] = tags[2]
        flipfetaures['Value for Money'] = tags[3]
        urltovisit = response.css("a.col-3-12._2kDYyJ.tsPZ29::attr(href)").extract()
        urll = "https://www.flipkart.com" + urltovisit[0]
        yield scrapy.Request(url=urll, callback=self.parse)

    def parse(self, response):

        filename = 'Page.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
        file = open(Constants.base_file+"\\ScrapedPages\\FlipkartRatings\\Page.txt", "r")
        urll = response.url
        for words in file:
            regex = re.search('"value":"Performance","firstLoad":true,"tabId":"[A-Za-z0-9-]*', words)
            if regex:

                temp = regex.group(0)
                # print(temp)
                regex1 = re.search('"tabId":"[A-Za-z0-9-]*', temp)
                if regex1:
                    temp1 = regex1.group(0)
                    temp1 = temp1.replace('"', "")
                    temp1 = temp1.split(":")
                    temp1 = temp1[1]
                    temp1 = "aid=" + temp1
                    print(urll)
                    newurl = re.sub(r"aid=[A-Za-z0-9-]*", temp1, urll)

                    yield scrapy.Request(url=newurl, callback=self.finalcrawl)

    def finalcrawl(self, response):
        tags = response.css("text.PRNS4f::text").extract()
        flipfetaures['Performance'] = tags[0]
        with open(Constants.base_file+"\\ScrapedPages\\FlipkartRatings\\Page.json", "w") as file:
            file.write(json.dumps(flipfetaures))
        print(flipfetaures)
