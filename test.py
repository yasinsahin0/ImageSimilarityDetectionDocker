import cv2
import base64
import image_similarity as sim

with open("data/eagle.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

sm =sim.Similarity()
print(sm.black_white_result(encoded_string))
"""
decode = base64.b64decode(encoded_string)
with open("save_image/save_ff.jpg", "wb") as fh:
    fh.write("decode")
"""