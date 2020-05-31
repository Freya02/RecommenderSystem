import DatabaseConnection as db
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
import sys

def collaborative(userid,phoneid):
    cursor=db.mydb.cursor()
    query = "SELECT PID,OVERALL,CAMERA,BATTERY,DISPLAY,VALUE_FOR_MONEY, PERFORMANCE, PHONE_NAME FROM RATINGS;"
    cursor.execute(query)
    result = cursor.fetchall()
    data_matrix = np.zeros((len(result),6))
    u1 = {}     #{101:0,102:1}
    u2 = {}     #{0:101,1:102}
    i = 0
    for row in result:
        for j in range(0,6):
            data_matrix[i,j]=row[j+1]
        u1[row[0]] = i
        u2[i] = row[0]
        i = i + 1
    item_similarity = pairwise_distances(data_matrix, metric="cosine")

    #pid = input("Enter the phone ID : ")
    phone = item_similarity[u1[int(phoneid)]]

    max = 0
    ntr = []
    for j in range(0,10):
        for i in range(0,len(phone)):
            if phone[max] < phone[i]:
                max = i
        ntr.append(u2[max])
        phone[max] = -1
    #print("Phones not to recommend are : ")
    #print(ntr)

    cursor = db.mydb.cursor()

    query1 = "SELECT COUNT(DISTINCT uid) FROM `purchased_phones`"
    rows = cursor.execute(query1)
    rows = cursor.fetchone()
    rows = rows[0]

    query2 = "SELECT COUNT(DISTINCT pid) FROM `purchased_phones`"
    cols = cursor.execute(query2)
    cols = cursor.fetchone()
    cols = cols[0]

    data_matrix = np.zeros((rows,cols))

    query3 = "SELECT * FROM `purchased_phones`"
    result = cursor.execute(query3)
    result = cursor.fetchall()
    i = 0
    u1 = {} #{0:101,1:102}
    u2 = {} #{101:0,102:1}
    for row in result:
        if row[1] in u2:
            data_matrix[row[0]-1,u2[row[1]]]=row[3]
        else:
            data_matrix[row[0]-1,i] = row[3]
            u2[row[1]] = i
            u1[i] = row[1]
            i = i+1

    user_similarity = pairwise_distances(data_matrix,metric="cosine")

    mean_user_rating = data_matrix.mean(axis=1)
    ratings_diff = (data_matrix - mean_user_rating[:, np.newaxis])
    pred = mean_user_rating[:, np.newaxis] + user_similarity.dot(ratings_diff) / np.array([abs(user_similarity).sum(axis=1)]).T

    user = pred[userid]
    max = 0
    rec = []
    while len(rec) != 10:
        for i in range(0,len(user)):
            if user[max] < user[i]:
                max = i
        if u1[max] not in ntr:
            rec.append(u1[max])
        user[max] = -1
    #print("Phones to recommend are : ")
    #print(rec)

    phone_score = []
    weight = 3

    query = "SELECT PERFORMANCE, CAMERA, BATTERY, DISPLAY FROM USERS WHERE UID="+str(1)
    cursor.execute(query)
    pref = list(cursor.fetchone())
    pref.insert(0,1)
    pref.append(1)

    for i in rec:
        query = "SELECT OVERALL, CAMERA, BATTERY, DISPLAY, VALUE_FOR_MONEY, PERFORMANCE FROM RATINGS WHERE PID="+str(i)
        cursor.execute(query)
        rating = list(cursor.fetchall())

        score = np.array(rating).dot(np.array(pref))/np.sum(pref)
        phone_score.append(round(score[0],1) * weight)
        weight = weight - 1

    max=0
    ranks=[]
    for i in range(0,10):
        for j in range(0,10):
            if phone_score[max] < phone_score[j]:
                max=j
        ranks.append(rec[max])
        phone_score[max] = -1
        max = 0
    return ranks
    print("Collab Final Recommendations : ",ranks)
