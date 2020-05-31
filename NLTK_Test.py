from nltk import *
from nltk.corpus import stopwords
import Ratings as rate
import WordList as wordlist
import DatabaseConnection as db
import getreview as amazon
import GetBlogs as blogs
import json
import GetRatings as getrating
import time
import VeeQuestCrawler.VeeQuestCrawler.spiders.blogscrawler as crawler1
import VeeQuestCrawler.VeeQuestCrawler.spiders.featurecrawler as crawler2
import VeeQuestCrawler.VeeQuestCrawler.spiders.flipkartcrawler as crawler
from scrapy.crawler import CrawlerProcess
import GetFeatures
import time




def preProcess(document):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(document)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    global sentence
    sentences=""
    for w in word_tokens:
        if w not in stop_words:
            sentences=sentences+" "+w
    sentences=sent_tokenize(sentences)
    sentences=[word_tokenize(sent) for sent in sentences]
    sentences=[pos_tag(sent) for sent in sentences]
    return sentences

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=" ")
    else:
        for child in t:
            if type(child)==tree.Tree:
                global noun
                noun=""
                for words in child:
                    if words[1]=="NN":
                        temp=wordlist.getNoun(words[0])
                        if temp!="":
                            noun=temp
                        elif noun=="":
                            noun="misc"
                    elif words[1]=="JJ":
                        if noun in ratings:
                            temp=ratings[noun]
                            temp.append(words[0])
                            ratings[noun]=temp
                        else:
                            ratings[noun]=([words[0]])

"""f = open('C:\\Users\\iamfr\\Desktop\\phonenames.txt', 'r')
line = f.readline()
while line:
    phone=line
    process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    })
    process.crawl(crawler1.QuotesSpider, phoneName=phone)
    process.crawl(crawler2.QuotesSpider, phoneName=phone)
    process.crawl(crawler.FlipkartSpider, phoneName=phone)
    process.start()

    phonename = GetFeatures.getPhoneFeatures()
    data_ = []
    review = amazon.ReadAsin(phone)
    listrev = []
    sentence = ""
    for i in range(0, len(review[0]["reviews"])):
        sentence = sentence + review[0]["reviews"][i]["review_text"]
    sentence = sentence + blogs.getBlogs()
    data_ = preProcess(sentence)
    grammar1 = "Relation:{<NN.*><.*>*<JJ>}"
    grammar2 = "Relation:{<JJ.*><.*>*<NN>}"
    ratings = {}
    cp = RegexpParser(grammar1)
    for i in range(0, len(data_)):
        result = cp.parse(data_[i])
        traverse(result)
    cp1 = RegexpParser(grammar1)
    for i in range(0, len(data_)):
        result = cp.parse(data_[i])
        traverse(result)
    rates = rate.rateReviews(ratings)
    print(rates)
    featureList = ["processor", "ram", "camera", "battery", "screen_quality", "launch_months", "misc"]
    featureList = ["camera", "battery", "display", "value_for_money", "performance"]
    global stars
    stars = 0
    values = []
    cursor = db.mydb.cursor()
    values.append(cursor.rowcount + 1)
    values.append(phonename)
    values.append(0)
    for words in featureList:
        try:
            temp = rates[words]
            positive = temp[0]
            negative = temp[1]
            pos = ((positive) / (positive + negative)) * 2.5
            neg = ((negative) / (positive + negative)) * 2.5
            stars = pos + (2.5 - neg)
            values.append(stars)
        except KeyError:
            values.append(0)
    sum = 0
    for i in range(2, 7):
        sum = sum + i
    overall = sum / 5
    values[2] = overall
    print("Ratings = ", values)

    #
    # FLIPKART RATINGS CODE HERE
    #

    fliprating = getrating.getRatings()
    print(fliprating)

    final_ratings = []
    querystmt = "SELECT phoneID FROM `phonefeatures` WHERE ModelName=\"" + phonename + "\""
    cursor.execute(querystmt)
    phid = cursor.fetchone()
    final_ratings.append(phid[0])
    final_ratings.append(phonename)
    final_ratings.append((round(values[2], 1) + round(float(fliprating["Overall"]))) / 2)
    final_ratings.append((round(values[3], 1) + round(float(fliprating["Camera"]))) / 2)
    final_ratings.append((round(values[4], 1) + round(float(fliprating["Battery"]))) / 2)
    final_ratings.append((round(values[5], 1) + round(float(fliprating["Display"]))) / 2)
    final_ratings.append((round(values[6], 1) + round(float(fliprating["Value for Money"]))) / 2)
    final_ratings.append((round(values[7], 1) + round(float(fliprating["Performance"]))) / 2)
    final_ratings.append(1)
    print(final_ratings)
    query = "insert into ratings values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = tuple(final_ratings)
    cursor.execute(query, values)
    db.mydb.commit()
    #time.sleep(10)
    line = f.readline()"""
phone=input("Enter phone name:")
process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    })
process.crawl(crawler1.QuotesSpider, phoneName=phone)
process.crawl(crawler2.QuotesSpider, phoneName=phone)
process.crawl(crawler.FlipkartSpider, phoneName=phone)
process.start()

phonename = GetFeatures.getPhoneFeatures()
data_ = []
review = amazon.ReadAsin(phone)
listrev = []
sentence = ""
if len(review)!=0:
    for i in range(0, len(review[0]["reviews"])):
        sentence = sentence + review[0]["reviews"][i]["review_text"]
sentence = sentence + blogs.getBlogs()
data_ = preProcess(sentence)
grammar1 = "Relation:{<NN.*><.*>*<JJ>}"
grammar2 = "Relation:{<JJ.*><.*>*<NN>}"
ratings = {}
cp = RegexpParser(grammar1)
for i in range(0, len(data_)):
    result = cp.parse(data_[i])
    traverse(result)
cp1 = RegexpParser(grammar1)
for i in range(0, len(data_)):
    result = cp.parse(data_[i])
    traverse(result)
rates = rate.rateReviews(ratings)
print(rates)
featureList = ["processor", "ram", "camera", "battery", "screen_quality", "launch_months", "misc"]
featureList = ["camera", "battery", "display", "value_for_money", "performance"]
global stars
stars = 0
values = []
cursor = db.mydb.cursor()
values.append(cursor.rowcount + 1)
values.append(phonename)
values.append(0)
for words in featureList:
    try:
        temp = rates[words]
        positive = temp[0]
        negative = temp[1]
        pos = ((positive) / (positive + negative)) * 2.5
        neg = ((negative) / (positive + negative)) * 2.5
        stars = pos + (2.5 - neg)
        values.append(stars)
    except KeyError:
        values.append(0)
sum = float(0)
for i in range(2, 7):
    sum = sum + float(i)
overall = sum / 5.0
values[2] = overall
print("Ratings = ", values)

#
# FLIPKART RATINGS CODE HERE
#

fliprating = getrating.getRatings()
print(fliprating)

final_ratings = []
querystmt = "SELECT phoneID FROM `phonefeatures` WHERE ModelName=\"" + phonename + "\""
cursor.execute(querystmt)
phid = cursor.fetchone()
final_ratings.append(phid[0])
final_ratings.append(phonename)
final_ratings.append((round(values[2], 1) + round(float(fliprating["Overall"]))) / 2)
final_ratings.append((round(values[3], 1) + round(float(fliprating["Camera"]))) / 2)
final_ratings.append((round(values[4], 1) + round(float(fliprating["Battery"]))) / 2)
final_ratings.append((round(values[5], 1) + round(float(fliprating["Display"]))) / 2)
final_ratings.append((round(values[6], 1) + round(float(fliprating["Value for Money"]))) / 2)
final_ratings.append((round(values[7], 1) + round(float(fliprating["Performance"]))) / 2)
final_ratings.append(1)
print(final_ratings)
query = "insert into ratings values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values = tuple(final_ratings)
cursor.execute(query, values)
db.mydb.commit()

