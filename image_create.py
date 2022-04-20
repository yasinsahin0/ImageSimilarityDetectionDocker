import cv2
import numpy as np
import random


w, h = 50, 50
data = np.zeros((h, w, 3), dtype=np.uint8)

for i in range(0,50):
    for a in range(0,50):
        R = random.randint(0,255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        data[i,a] = [R,G,B]

rsz = cv2.resize(data,(400,400))
cv2.imshow("aa",rsz)
cv2.waitKey(0)
cv2.destroyAllWindows()