import DatabaseConnection as db
import sys
def popmodel():
    price = input("Enter your budget:")
    query = "SELECT phonefeatures.ModelName,phonefeatures.price,ratings.searched from phonefeatures,ratings WHERE phonefeatures.price!=0 AND phonefeatures.PhoneID=ratings.pid AND phonefeatures.Price<=" + price + " ORDER BY ratings.searched desc LIMIT 1"
    cursor = db.mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    print(result[0], " ", result[1])
