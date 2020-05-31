from flask import Flask
from flask import render_template,jsonify,request
import requests
from engine import *
import random
import responses

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])


@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        entities = response.get("entities")
        topresponse = response["intent"]
        intent = topresponse.get("name")
        print("Intent {}, Entities {}".format(intent,entities))
        if intent == "best_phone":
            response_text = responses.getBestPhone(entities).title()
        elif intent == "camera_phone":
            response_text = responses.getBestCameraPhone(entities).title()
        elif intent == "ram_internal":
            response_text = "Ram and internal intent was called"
        elif intent == "battery_phone":
            response_text = responses.getBatterPhone().title()
        elif intent == "user_id":
            file=open("user.txt","w")
            file.write(entities[0]["value"])
            file.close()
            response_text = "Hello Prashant!"
        else:
            response_text = get_random_response(intent)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
