import DatabaseConnection as db
import Popularity as pr
import  CollaborativeRS as co
import ContentBased2 as cb2
import sys
global uid
#uid = input("Enter your user ID:")
def getFinal():
    uid = "1"
    file=open("user.txt","r")
    uid = file.read()
    query = "select user_history.uid,user_history.pid,phonefeatures.ModelName from user_history,phonefeatures where user_history.uid=" + uid + " and phonefeatures.PhoneID=user_history.pid  order by user_history.no_of_times_searched desc"
    cursor = db.mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    global pidlist
    pidlist=[]
    flag=False
    phone_to_avoid=122
    if (len(result) == 0):
        print("User Has No Search History...")
        pr.popmodel()
    else:
        global user_id
        user_id=0
        print("User Has Search History...")
        print(result)
        for res in result:
            uid = res[0]
            user_id=uid
            pid = res[1]
            query="select * from purchased_phones where uid="+str(uid)+" and pid="+str(pid);
            cursor.execute(query)
            purchased=cursor.fetchall()
            if len(purchased)!=0:
                #querystmt = "select * from purchased_phones where uid="+str(uid)+" and pid="+str(pid);#+"and overall>=3";
                #cursor.execute(querystmt)
                #checkres = cursor.fetchall()
                #print(checkres)
                if purchased[0][3] >= 3:
                    pidlist.append(res[1])
                else:
                    print("This phone has rating less than 3....")
                    #co.collaborative(uid,res[1])
                    phone_to_avoid=res[1]
                    flag=True
    
            else:
                print("Entry for this phone exists in search history but not in purchased phones....")
        list1=[]
        list2=[]
        if(flag == True):
            list1=co.collaborative(user_id,phone_to_avoid)
        if len(pidlist)!=0:
            list2=cb2.ContentBased(pidlist)
        uniquePhones=set()
        for l in list1:
            uniquePhones.add(l)
        for l in list2:
            uniquePhones.add(l)
        NewList=[]
        i=0
        while len(NewList) < 10:
            if list1[i] in uniquePhones:
                NewList.append(list1[i])
                uniquePhones.remove(list1[i])
            if list2[i] in uniquePhones:
                NewList.append(list2[i])
                uniquePhones.remove(list2[i])
            i=i+1
        return NewList
