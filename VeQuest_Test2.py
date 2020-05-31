"""from numpy import *
reviews=random.randint(low=1,high=10,size=(6,10))
print(reviews)
mean_val=zeros(shape=(6,1))
for i in range(reviews.shape[0]):
    idx=[0,1,2,3,4,5,6,7,8,9]
    mean_val[i]=mean(reviews[i,idx])
    reviews[i,idx]=reviews[i,idx]-mean_val[i]
print(reviews)
print(mean_val)
f=open("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\positive-words.txt","r")
wordslist=[];
for word in f:
    wordslist.append(word[0:int(len(word)-1)])
temp=input("Get word")
if temp in wordslist:
    print("In the set")
else:
    print("Not in the set")
def tempfunction(text):
    print (text)
tempfunction("Somethign printed")
te={"rating":1,"is":2,"given":3}
for wrods in te:
    print(te[wrods])"""
"""import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="VeQuest")
query="insert into TemporaryTable values(%s,%s)"
values=(10,20)
cursor=mydb.cursor()
cursor.execute(query,values)
mydb.commit()"""
"""import json
file=open("C:\\Users\\Prashant Mishra\\PycharmProjects\\VeQuest\\ScrapedPages\\FlipkartRatings\\Page.json", "r")
data=json.load(file)
print(data["Display"])"""
"""import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
data_matrix=[[0,4,2,3],
             [2,0,1,3],
             [1,0,0,4],
             [2,2,0,0]]
data_matrix=np.array(data_matrix)
mean_user_rating = data_matrix.mean(axis=1)
similarity=pairwise_distances(data_matrix,metric="cosine")
print(np.array([np.abs(similarity).sum(axis=1)]).T)
ratings_diff=[[0,1.75,-0.25,0.75],
              [0.5,0,-0.5,1.5],
              [0.25,0,0,2.75],
              [1,1,0,0]]
print(mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T)"""


"""a = {'value_for_money': [14, 4], 'misc': [2352, 466], '': [612, 88], 'display': [44, 18], 'camera': [102, 28], 'performance': [26, 6], 'battery': [18, 12]}
b = [0, 'Samsung Galaxy Note9', 4.0, 3.923076923076923, 3.0, 3.548387096774194, 3.888888888888889, 4.0625, 4.173172462739531]
c = {'Overall': '4.5', 'Camera': '4.0', 'Battery': '4.0', 'Display': '4.3', 'Value for Money': '4.8', 'Performance': '4.5'}
final_ratings=[]
final_ratings.append((round(b[2],1)+round(float(c["Overall"])))/2)
final_ratings.append((round(b[3],1)+round(float(c["Camera"])))/2)
final_ratings.append((round(b[4],1)+round(float(c["Battery"])))/2)
final_ratings.append((round(b[5],1)+round(float(c["Display"])))/2)
final_ratings.append((round(b[6],1)+round(float(c["Value for Money"])))/2)
final_ratings.append((round(b[7],1)+round(float(c["Performance"])))/2)
print(final_ratings)"""

"""features={"price":1}
if "pricee" in features.keys():
    print("PRESENT")"""

"""total = [4.1923076923076925, 3.333333333333333, 4.333333333333334, 4.090909090909091, 4.117647058823529]
sum=0
for i in total:
    sum=sum+i
print(round(sum/5,3))"""
file=open("user.txt","r")
print(len(file.read()))
