import cv2
import base64
import image_similarity as sim

with open("data/eagle.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

a = "ada.jpg"
print(a[3:])
"""


import requests

url = "http://172.105.73.62:5000/img"

payload={'img_base64': encoded_string}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
"""