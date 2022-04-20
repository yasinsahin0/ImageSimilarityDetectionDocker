import cv2
import base64
import image_similarity as sim

with open("nane.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())


similar = sim.Similarity()
print(similar.black_white_result(encoded_string))