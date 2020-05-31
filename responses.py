from ContentBased1 import getFinal
import DatabaseConnection as db
import geturls
import random
import CameraPhones
import PricePhones
import BatteryPhones

def getSpecs(phone_name):
    cursor = db.mydb.cursor()
    query="SELECT phonefeatures.CPU,phonevariants.Internal,phonevariants.RAM,phonefeatures.RearCamMP,phonefeatures.FrontCamMP,phonefeatures.Battery,phonefeatures.Price FROM `phonefeatures`,phonevariants WHERE ModelName='"+phone_name+"' and phonefeatures.PhoneID=phonevariants.PhoneID"
    cursor.execute(query);
    result = cursor.fetchall()
    print(result)
    specs="\n\n<b>Specifications: </b>\n"
    specs=specs+"Processor: <b>"+str(result[0][0])+"</b>\n"
    if len(result)>1:
        specs=specs+"It comes in <b>"+str(len(result))+"</b> different variants:\n"
        for i in range(0,len((result))):
            specs=specs+"Internal Storage: <b>"+str(result[i][1])+"GB</b> "
            specs=specs+"RAM: <b>"+str(result[i][2])+"GB</b>\n"
    else:
        specs=specs+"Internal Storage: <b>"+str(result[0][1])+"GB</b> "
        specs=specs+"RAM: <b>"+str(result[0][2])+"GB</b>\n"
    specs=specs+"Rear Camera: <b>"+str(result[0][3])+" MP</b>\n"
    specs=specs+"Front Camera: <b>"+str(result[0][4])+" MP</b>\n"
    specs=specs+"Battery: <b>"+str(result[0][5])+" MAH</b>\n"
    specs=specs+"<b>PRICE: ₹"+str(result[0][6])+"</b>"
    """specs="\n\n"+phone_name+" comes with a <b>"+str(result[0][0])+"</b>\nThe internal storage it offers is <b>"+str(result[0][1])+"GB</b>"
    specs=specs+" and supported by <b>"+str(result[0][2])+"GB</b> of RAM\n"
    specs=specs+"It has a laser sharp Rear Camera of <b>"+str(result[0][3])+"MP</b> and a <b>"+str(result[0][4])+"MP</b> of Front Camera\n"
    specs=specs+"It is powered by a huge <b>"+str(result[0][5])+"MAH</b> of Battery\n"
    if len(result)>1:
        specs=specs+"It comes in "+str(len(result))+" variants.\n"
    specs=specs+"<b>PRICE: ₹"+str(result[0][6])+"</b>"""
    return specs

def getBestPhone1():
    list = getFinal()
    cursor = db.mydb.cursor()
    query="SELECT ModelName FROM `phonefeatures` WHERE PhoneID="+str(list[0])
    cursor.execute(query);
    result = cursor.fetchall()
    print(result[0][0])
    #urls=geturls.geturllist(result[0][0],"amazon")
    urls=['https://www.amazon.in/Redmi-Pro-Black-64GB-Storage/dp/B07DJHXWZZ', 'https://www.amazon.com/Xiaomi-Factory-Unlocked-Smartphone-Version/dp/B07HK4JNV1']
    resp=uniqueResponses1()+"<b>"+result[0][0]+"</b>\nYou can find the best buy link here:\n"
    phone_name=result[0][0]
    phone_name=phone_name.title()
    resp=resp.title()
    urls="<a href='"+urls[0]+"'><b>"+phone_name+"</b></a>"
    resp=resp+urls
    specs=getSpecs(phone_name)
    return resp+specs

def getBestPhone2(count):
    list = getFinal()
    cursor = db.mydb.cursor()
    result=[]
    for i in list:
        query="SELECT ModelName,Price FROM `phonefeatures` WHERE PhoneID="+str(i)
        query1="select overall from ratings where pid="+str(i)
        cursor.execute(query);
        response=cursor.fetchall()
        cursor.execute(query1)
        response1=cursor.fetchall()
        #result.append(cursor.fetchall().pop()[0])
        result.append("Phone Name: <b>"+response[0][0]+"</b>")
        result.append("Price: <b>"+str(response[0][1])+"</b>"+" Overall Rating: <b>"+str(response1[0][0])+"</b>")
        #print(cursor.fetchall().pop()[0])
    resp = uniqueResponses2()+"\n"
    for i in range(0,count*3):
        resp = resp + result[i] + "\n"
    return resp.title()

def getBestPhone(entities):
    if len(entities) == 0:
        return getBestPhone1()
    elif len(entities) == 1 and entities[0]["entity"]=="count":
        print(entities)
        qtype = entities[0]["entity"]
        qval = entities[0]["value"]
        if qtype == "count":
            return getBestPhone2(int(qval))
    else:
        return getPricePhone(entities)
    
def getBestCameraPhone(entities):
    if len(entities) == 0:
        result=CameraPhones.camera("both")
        print(result[0])
        urls=geturls.geturllist(result[0],"amazon")
        resp=uniqueResponses1()+result[0]+"\nYou can find the best buy link here:\n\n"
        phone_name=result[0]
        phone_name=phone_name.title()
        resp=resp.title()
        urls="<a href='"+urls[0]+"'>"+phone_name+"</a>"
        resp=resp+urls+getSpecs(phone_name)
        return resp
    elif len(entities) == 1:
        qval = entities[0]["value"]
        if qval == "front":
            result=CameraPhones.camera("front")
            print(result[0])
            urls=geturls.geturllist(result[0],"amazon")
            resp="Phone with best front camera is "+result[0]+"\nYou can find the best buy link here:\n\n"
            phone_name=result[0]
            phone_name=phone_name.title()
            resp=resp.title()
            urls="<a href='"+urls[0]+"'>"+phone_name+"</a>"
            resp=resp+urls
            return resp
        elif qval == "rear":
            result=CameraPhones.camera("rear")
            print(result[0])
            urls=geturls.geturllist(result[0],"amazon")
            resp="Phone with the best rear camera is "+result[0]+"\nYou can find the best buy link here:\n\n"
            phone_name=result[0]
            phone_name=phone_name.title()
            resp=resp.title()
            urls="<a href='"+urls[0]+"'>"+phone_name+"</a>"
            resp=resp+urls
            return resp
    
def getPricePhone(entities):
    if len(entities) == 1:
        qval = entities[0]["value"]
        if qval[len(qval)-1]=="k":
            qval=qval[:len(qval)-1]
            qval=qval+"000"
        result = PricePhones.getMaxPrice(qval)
        resp=uniqueResponses1()+result[0][1];
        resp=resp+getSpecs(result[0][1])
        resp=resp+"\n"+"You may also like "+result[1][1]+" and "+result[2][1]
        return resp
    elif len(entities) == 2:
        print(entities[0]["value"],"---",entities[1]["value"])
        if entities[0]["entity"]=="count" and entities[1]["entity"]=="max_price":
            print("Inside if")
            topn = entities[0]["value"]
            minp = entities[1]["value"]
            if minp[len(minp)-1]=="k":
                minp=minp[:len(minp)-1]
                minp=minp+"000"
            result = PricePhones.getMaxPrice(minp)
            resp=uniqueResponses1()+result[0][1];
            resp=resp+getSpecs(result[0][1])
            resp=resp+"\nOther phones you might like are: \n"
            i=1
            while i<len(result) and i<int(topn):
                resp=resp+result[i][1]+"\n"
                i=i+1
            return resp
        elif entities[0]["entity"]=="min_price" and entities[1]["entity"]=="max_price":
            maxp = entities[0]["value"]
            minp = entities[1]["value"]
            if minp[len(minp)-1]=="k":
                minp=minp[:len(minp)-1]
                minp=minp+"000"
            if maxp[len(maxp)-1]=="k":
                maxp=maxp[:len(maxp)-1]
                maxp=maxp+"000"
            result = PricePhones.getMaxMinPrice(maxp,minp)
            resp=uniqueResponses1()+result[0][1];
            resp=resp+getSpecs(result[0][1])
            resp=resp+"\n"+"You may also like \n"
            i=1
            while i<len(result):
                resp=resp+result[i][1]+"\n"
                i=i+1
            return resp
    elif len(entities) == 3 and entities[0]["entity"]=="count" and entities[1]["entity"]=="min_price" and entities[2]["entity"]=="max_price":
            topn = entities[0]["value"]
            maxp = entities[1]["value"]
            minp = entities[2]["value"]
            if minp[len(minp)-1]=="k":
                minp=minp[:len(minp)-1]
                minp=minp+"000"
            if maxp[len(maxp)-1]=="k":
                maxp=maxp[:len(maxp)-1]
                maxp=maxp+"000"
            result = PricePhones.getMaxMinPrice(maxp,minp)
            resp=uniqueResponses1()+result[0][1];
            resp=resp+getSpecs(result[0][1])
            resp=resp+"\n"+"You may also like \n"
            i=1
            while i<len(result) and i<int(topn):
                resp=resp+result[i][1]+"\n"
                i=i+1
            return resp

def getBatterPhone():
    result = BatteryPhones.battery()
    resp=uniqueResponses1()+result[0];
    resp=resp+getSpecs(result[0])
    resp=resp+"\n"+"You may also like "+result[1]+" and "+result[2]
    return resp

def uniqueResponses1():
    resp=[
        "You will like ",
        "You can go for ",
        "You will surely like ",

    ]
    return resp[random.randint(0,len(resp)-1)]

def uniqueResponses2():
    resp=[
        "This is the list we found for you:",
        "These are the phone that you will like:",
        "Best suggestions for you:",
        "Top phones for you:"
    ]
    return resp[random.randint(0,len(resp)-1)]
#print(getBestPhone1())
#You can find the phone here
#find the phone at

