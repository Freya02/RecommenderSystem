#import ContentBased1 as cb
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances
import DatabaseConnection as db
import sys
global  top10_pid_list

def ContentBased(pidlist):
    top10_pid_list=set()
    
    pids=pidlist
    
    cursor=db.mydb.cursor()
    query1="select count(distinct pid) from ratings"
    rows=cursor.execute(query1)
    rows=cursor.fetchone()
    rows=rows[0]
    
    query3="SELECT pid,overall,camera,battery,display,value_for_money,performance FROM ratings"
    result=cursor.execute(query3)
    result=cursor.fetchall()
    
    data_matrix=np.zeros((rows,6))
    i=0
    u1={} #{0:101,1:102}
    u2={} #{101:0,102:1}
    
    for row in result:
        for j in range(0,6):
            data_matrix[i,j]=row[j+1]
        u1[row[0]] = i
        u2[i] = row[0]
        i = i + 1
    item_similarity = pairwise_distances(data_matrix, metric="cosine")
    
    #print(u1)
    global ind
    ind=[]
    for pid in pids:
        if pid in u1.keys():
            rowvalue=u1[pid]
            #print(rowvalue)
            all=[]
            for j in range(0,rows):
                all.append(item_similarity[rowvalue][j])
            in_arr=np.array(all)
            #If you negate an array, the lowest elements become the highest elements and vice-versa.
            ind=np.argsort(-in_arr)
            #ind = np.argpartition(all, -10)[-10:]
            #print(ind[0:10])
            ind=ind[0:10]
            for index in ind:
                if index in u2.keys():
                    top10_pid_list.add(u2[index])
                else:
                    print("Index not in  u2")
        else:
            print("PID(s) not present")
    
    #print(top10_pid_list)
    top10_pid_list=list(top10_pid_list)
    #Matrix Factorisation Code
    phone_score = []
    weight = len(top10_pid_list)
    
    query = "SELECT PERFORMANCE, CAMERA, BATTERY, DISPLAY FROM USERS WHERE UID="+str(1)
    cursor.execute(query)
    pref = list(cursor.fetchone())
    pref.insert(0,1)
    pref.append(1)
    
    for i in top10_pid_list:
        query = "SELECT OVERALL, CAMERA, BATTERY, DISPLAY, VALUE_FOR_MONEY, PERFORMANCE FROM RATINGS WHERE PID="+str(i)
        cursor.execute(query)
        rating = list(cursor.fetchall())
    
        score = np.array(rating).dot(np.array(pref))/np.sum(pref)
        phone_score.append(round(score[0],1) * weight)
        weight = weight - 1
    
    #print("Scores for the phones : ")
    #print(phone_score)
    
    max=0
    ranks=[]
    for i in range(0,10):
        for j in range(0,10):
            if phone_score[max] < phone_score[j]:
                max=j
        ranks.append(top10_pid_list[max])
        phone_score[max] = -1
        max = 0
    return ranks
    print("Content Final Recommendations : ",ranks)
