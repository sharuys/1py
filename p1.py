import json
import os
import requests
#from requests_oauthlib import OAuth1

url = "https://api.thenounproject.com/v2/icon/1"
otvet = requests.get(url)
if otvet.status_code == 200:
    data = otvet.json()
    icon = data["icon"]
    filename = icon["filename"]
    icon_data = icon["data"]
    os.makedirs("icons", exist_ok= True)
    with open("icons/" + filename, "wb") as f:
        f.write(icon_data)

    print("icon saved")

else:
    print("ERROR " + str(otvet.status_code))