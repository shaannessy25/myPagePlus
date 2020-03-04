from django.shortcuts import render
import requests
import json
import geocoder

# Create your views here.
key = "ad958ab12b22f3901be8a6cdb93beec3"
okey = "pk.eyJ1Ijoib21hcnNzNjIiLCJhIjoiY2s3YXJsdGh4MG13ODNlcXJhY3l1NnMybiJ9.xmKZ0Yt2_b8evLDsrQcTqQ"

def weatherView(request, location):
    coords = geocode(location)

    req = requests.get("https://api.darksky.net/forecast/"+ key + "/"+ coords)

    reqJson = req.json()

    weather = {
        "temp": reqJson["currently"]["temperature"],
        "humidity": reqJson["currently"]["humidity"],
        "wind": reqJson["currently"]["windSpeed"],
        "summary": reqJson["currently"]["summary"],
        "high": reqJson["daily"]["temperatureHigh"],
        "low": reqJson["daily"]["temperatureLow"]
    }

    return render(request, "base.html", weather=weather)

def geocode(location):
    url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'+ location +'.json?access_token=' + key + '&autocomplete=true'

    res = requests.get(url)
    latitude, longitude = res.json()["features"][0]["geometry"]["coordinates"]

    return str(latitude + ',' + longitude)