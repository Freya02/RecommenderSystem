import DatabaseConnection as db
import ContentBased1 as cb1


def battery():
    cursor = db.mydb.cursor()
    query="select phonefeatures.PhoneID,phonefeatures.ModelName,phonefeatures.Battery*ratings.pid as BatteryFinal from phonefeatures,ratings where phonefeatures.PhoneID=ratings.pid order by BatteryFinal desc;"
    cursor.execute(query)
    result = cursor.fetchall()
    iList=cb1.getFinal()
    print(result)
    print("Result of RS:",iList)
    FinalList=[]
    FinalResult=[]
    for i in range(0,len(result)):
        if(result[i][0] in iList):
            FinalList.append(result[i][0])
            FinalResult.append(result[i][1])
    print("****************************************************************")
    #print(FinalList)
    #print("Final Answer:",FinalResult)
    return FinalResult
    

    
