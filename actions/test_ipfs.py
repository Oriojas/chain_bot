import os
import datetime
import requests

STUARY_API_KEY = os.environ["STUARY_API_KEY"]
FILE_IMG = os.environ["FILE_IMG"]

url = "https://upload.estuary.tech/content/add"

payload = {}
headers = {'Accept': 'application/json',
           'Authorization': f"Bearer {STUARY_API_KEY}"}
files = [('data',
          ('file',
           open(f'{FILE_IMG}/img_response.jpg', 'rb'),
           'application/octet-stream'))]

response = requests.request("POST", url, headers=headers, data=payload, files=files)

cid = eval(response.text).get("cid")

print(cid)
