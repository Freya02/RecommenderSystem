import DatabaseConnection as db
import ContentBased1 as cb1

def price():
    cursor = db.mydb.cursor()
    query="select phonefeatures.PhoneID,phonefeatures.ModelName,phonefeatures.Price*ratings.value_for_money as PriceFinal from phonefeatures,ratings where phonefeatures.PhoneID=ratings.pid order by PriceFinal desc;"
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
    return  FinalResult

def getPhones():
    iList=cb1.getFinal()
    query="SELECT PhoneID,ModelName,Price FROM `phonefeatures` WHERE PhoneID in ("+iList[0]+", "+iList[1]+", "+iList[2]+", "+iList[3]+", "+iList[4]+", "+iList[5]+", "+iList[6]+", "+iList[7]+", "+iList[8]+", "+iList[9]+") order by Price"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def getMaxPrice(price):
    cursor = db.mydb.cursor()
    iList=cb1.getFinal()
    query="SELECT PhoneID,ModelName,Price FROM `phonefeatures` WHERE PhoneID in ("+str(iList[0])+", "+str(iList[1])+", "+str(iList[2])+", "+str(iList[3])+", "+str(iList[4])+", "+str(iList[5])+", "+str(iList[6])+", "+str(iList[7])+", "+str(iList[8])+", "+str(iList[9])+") and Price<"+str(price)+" order by Price"
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def getMaxMinPrice(minPrice,maxPrice):
    cursor = db.mydb.cursor()
    iList=cb1.getFinal()
    query="SELECT PhoneID,ModelName,Price FROM `phonefeatures` WHERE PhoneID in ("+str(iList[0])+", "+str(iList[1])+", "+str(iList[2])+", "+str(iList[3])+", "+str(iList[4])+", "+str(iList[5])+", "+str(iList[6])+", "+str(iList[7])+", "+str(iList[8])+", "+str(iList[9])+") and Price>"+str(minPrice)+" and Price<"+str(maxPrice)+" order by Price"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

#print(getMaxPrice(5000))
