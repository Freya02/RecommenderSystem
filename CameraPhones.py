import DatabaseConnection as db
import ContentBased1 as cb1
global result
result=""

def camera(cam):
    cursor = db.mydb.cursor()
    #For Rear Camera
    if "rear" in cam:
        query1="SELECT PhoneID,ModelName,phonefeatures.RearCamMP*phonefeatures.NumRearCam*ratings.camera as camerarating from phonefeatures,ratings where phonefeatures.PhoneID=ratings.pid order by camerarating DESC;"
        cursor.execute(query1)
        result1 = cursor.fetchall()
        result=result1

    #For Front Camera
    elif "front" in cam:
        query3="SELECT PhoneID,ModelName,phonefeatures.FrontCamMP*phonefeatures.NumFrontCam*ratings.camera as camerarating from phonefeatures,ratings where phonefeatures.PhoneID=ratings.pid order by camerarating DESC;"
        cursor.execute(query3);
        result3 = cursor.fetchall()
        result=result3

    #For both
    else:
        query2="SELECT PhoneID,ModelName,phonefeatures.RearCamMP*phonefeatures.NumRearCam*phonefeatures.FrontCamMP*phonefeatures.NumFrontCam*ratings.camera as camerarating from phonefeatures,ratings where phonefeatures.PhoneID=ratings.pid order by camerarating DESC;"
        cursor.execute(query2)
        result2 = cursor.fetchall()
        result=result2


    iList=cb1.getFinal()
    print("Result of RS:",iList)
    #print("Best Camera List",result)

    FinalList=[]
    FinalResult=[]
    for i in range(0,len(result)):
        if result[i][0] in iList:
            FinalResult.append(result[i][1])
            FinalList.append(result[i][0])
    print("****************************************************************")
    #print(FinalList)
    #print("Final Answer:",FinalResult)
    return FinalResult
