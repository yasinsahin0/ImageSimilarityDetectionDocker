import cv2
import base64
import image_similarity as sim
import datetime

with open("tanımsız.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

st_time = datetime.datetime.now()

import requests

url = "http://127.0.0.1:5000/img"

payload={'img_base64': encoded_string}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

sme = sim.Similarity()
result = sme.black_white_result(encoded_string)
stop_time = datetime.datetime.now()
print("Süre : ", str(stop_time-st_time))
print(response.text)
