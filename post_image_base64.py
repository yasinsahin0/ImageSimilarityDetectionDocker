import cv2
import base64
import image_similarity as sim

def results(image_name):
    with open(str(image_name), "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    similar = sim.Similarity()
    return similar.black_white_result(encoded_string)

# results("data/nane.jpg")