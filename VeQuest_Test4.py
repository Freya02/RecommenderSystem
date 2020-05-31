import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances
import DatabaseConnection as db


cursor=db.mydb.cursor()

query1="SELECT COUNT(DISTINCT uid) FROM `purchased_phones`"
rows=cursor.execute(query1)
rows=cursor.fetchone()
rows=rows[0]

query2="SELECT COUNT(DISTINCT pid) FROM `purchased_phones`"
cols=cursor.execute(query2)
cols=cursor.fetchone()
cols=cols[0]

print(rows,cols)
data_matrix=np.zeros((rows,cols))


query3="SELECT * FROM `purchased_phones`"
result=cursor.execute(query3)
result=cursor.fetchall()
i=0
u1={} #{0:101,1:102}
u2={} #{101:0,102:1}
for row in result:
    #data_matrix[row[0]-1,row[1]-1]=row[3]
    if row[1] in u2:
        data_matrix[row[0]-1,u2[row[1]]]=row[3]
    else:
        data_matrix[row[0]-1,i]=row[3]
        u2[row[1]]=i
        u1[i]=row[1]
        i=i+1
print(data_matrix)

user_similarity=pairwise_distances(data_matrix,metric="cosine")


def predict(ratings, similarity):
    mean_user_rating = ratings.mean(axis=1)
    ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
    pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([abs(similarity).sum(axis=1)]).T
    return pred

user_prediction = predict(data_matrix, user_similarity)
print(user_prediction)
print(u1)

"""final_rating=append(review_mobile,rating,axis=1)

unique_mob=unique(final_rating[:,1])
unique_mob=reshape(unique_mob,(unique_mob.shape[0],1))
mobile_rating=random.randint(low=1,high=5,size=(unique_mob.shape[0],6))
final_mob_rating=append(unique_mob,mobile_rating,axis=1)

final_rating=array(final_rating)
n_user=unique(final_rating[:,2])
data_matrix = zeros((10,10))

for i in range(0,final_rating.shape[0]):
    data_matrix[final_rating[i,1]-1,final_rating[i,2]-1]=final_rating[i,0]

user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')
print("------------------------------------------------------------")
#print(data_matrix)
#print(user_similarity)
#print(item_similarity)

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_ratipred = ratings.dot(similarity) / array([absng = ratings.mean(axis=1)
        ratings_diff = (ratings - mean_user_rating[:, newaxis])
        pred = mean_user_rating[:, newaxis] + similarity.dot(ratings_diff) / array([abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        (similarity).sum(axis=1)])
    return pred

user_prediction = predict(data_matrix, user_similarity, type='user')
item_prediction = predict(data_matrix, item_similarity, type='item')
global maxh
print(user_prediction)
for i in range(0,user_prediction.shape[0]):
    maxh=0
    for j in range(0,user_prediction.shape[1]):
        if user_prediction[i,j] > user_prediction[i,maxh]:
            maxh=j
    print("User ",i+1,":",maxh," Mobile")

for i in range(0,item_prediction.shape[1]):
    maxh=0
    for j in range(0,item_prediction.shape[0]):
        if user_prediction[j,i] > user_prediction[maxh,i]:
            maxh=j
    print("Mobile ",i+1,":",maxh," User")
"""