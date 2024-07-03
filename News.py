import requests
from ss import *

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + nkey
json_data = requests.get(api_address).json()

def news():
    ar = []
    for i in range(3):
        ar.append("Number " + str(i + 1) + ": " + json_data["articles"][i]["title"] + ".")
    return ar

