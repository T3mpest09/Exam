import requests
import json

token = input("Personal access token: ")
title = input("Title: ")
token = "Bearer " + token
headers = {"Authorization":token,
           "Content-Type": "application/json"}

url = "https://webexapis.com/v1/rooms"
body = {
        "title": title
    }

room = requests.post(url, headers=headers, data=json.dumps(body), verify=False).json()
print(json.dumps(room, indent=4))
