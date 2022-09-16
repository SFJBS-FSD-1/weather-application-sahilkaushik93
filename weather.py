import json
from flask import Flask, render_template, request
import urllib.request as myrequest
import requests
import datetime

app = Flask(__name__) # creating instance of flask

## Home Page
@app.route("/", methods=["GET","POST"])
def weather_home_page():
    print(request.method)
    if request.method == "POST":
        city = request.form["city"]

        print(city)
        api = "997ea79e1c9575bd4f087cf90e68205d"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        print(url)
        response = requests.get(url).json()
        print(response)

        if response["cod"]==200:

    # data = json.loads(response)
            data = {"temp": response["main"]["temp"],
                    "name": response["name"],
                    "lat": response["coord"]["lat"],
                    "lon": response["coord"]["lon"],
                    "sunrise_epoch": datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),
                    "sunset_epoch": datetime.datetime.fromtimestamp(response.get('sys')['sunset']),
                    "status":200
                    }

            print(data["temp"])
            print(data["name"])
            print(data["lat"])
            print(data["lon"])
            print(data["sunrise_epoch"])
            print(data["sunset_epoch"])


            return render_template("home.html", weatherinfo = data)

        elif response["cod"]=="404":
            data = {"message":response["message"], "status":404}
            return render_template("home.html", weatherinfo=data)
        elif response["cod"]=="400":
            data = {"message":response["message"], "status":400}
            return render_template("home.html", weatherinfo=data)


    else:
        print("loading home page")
        data = None
        return render_template("home.html",weatherinfo=data)

app.run(port=5002)

# http://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=997ea79e1c9575bd4f087cf90e68205d
# "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid"=997ea79e1c9575bd4f087cf90e68205d