import requests
import json

token = input("Personal access token: ")
token = "Bearer " + token
roomId = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZDJlNGI1NzAtMjdlOS0xMWVjLTk1ZTUtNmRkMmM1YTNmNzhj"

headers = {"Authorization":token,
           "Content-Type": "application/json"}

email = input("Person Email:")
mem_url = "https://webexapis.com/v1/memberships"
mem_body = {
        "roomId": roomId,
        "personEmail": email
    }
mem_post = requests.post(mem_url, headers=headers, data=json.dumps(mem_body), verify=False).json()

text = input("Text: ")
msg_url = "https://webexapis.com/v1/messages"
msg_body = {
        "roomId": roomId,
        "text": text
    }
msg_post = requests.post(msg_url, headers=headers, data=json.dumps(msg_body), verify=False).json()
print(json.dumps(mem_post, indent=4))
print(json.dumps(msg_post, indent=4))
