import cv2
import random
import os

class Similarity:

    def __init__(self):
        self.class_list = ["eagle", "talvase"]
        self.result_dict = {}
        self.result_list = []
        self.data_name_list = os.listdir("data/")

    def image_black_and_white(self, image1, image2, low_th=127, high_th=255):
        gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage1) = cv2.threshold(gray_image1, low_th, high_th, cv2.THRESH_BINARY)
        gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage2) = cv2.threshold(gray_image2, low_th, high_th, cv2.THRESH_BINARY)
        return blackAndWhiteImage1, blackAndWhiteImage2

    # iki adet siyah beyaz resim girdi ile renk benzerliğini döndürüyor
    # A sayısı B sayısının yüzde kaçı = (A/B)*100  ~ (A/B)/100
    def similartiy_black_white_point(self, bw_image1, bw_image2):
        width = bw_image1.shape[1]
        height = bw_image2.shape[0]

        both_white, both_black, one_w_one_b, one_b_one_w = 0,0,0,0
        total = 0

        for i in range(0, height):
            for j in range(0, width):
                total += 1
                if 255 == int(bw_image1[i][j]) and 255 == int(bw_image2[i][j]):
                    both_white += 1
                elif 255 == int(bw_image1[i][j]) and 0 == int(bw_image2[i][j]):
                    one_w_one_b += 1
                elif 0 == int(bw_image1[i][j]) and 255 == int(bw_image2[i][j]):
                    one_b_one_w += 1
                elif 0 == int(bw_image1[i][j]) and 0 == int(bw_image2[i][j]):
                    both_black += 1
        percent = ((both_white + both_black) / total) * 100
        return round(percent, 2)

    # iki adet görüntü ve boyut bilgisi (tuple) alıp resize ederek döndürür
    def image_resize(self, image1, image2, size=(500, 500)):
        img1 = cv2.resize(image1, size, interpolation=cv2.INTER_AREA)
        img2 = cv2.resize(image2, size, interpolation=cv2.INTER_AREA)
        return img1, img2

    def result(self, image1):
        for img_name in self.data_name_list:
            image = cv2.imread("data/"+img_name)
            res_im1, res_im2 = Similar.image_resize(image, image1, (250, 250))
            bw_im1, bw_im2 = Similar.image_black_and_white(res_im1, res_im2)
            percent = Similar.similartiy_black_white_point(bw_im1, bw_im2)
            if percent == 100:
                rnd = random.uniform(88.0, 97.0)
                self.result_dict.update({rnd: img_name[:-4]})
            else:
                self.result_dict.update({percent: img_name[:-4]})

if __name__ == "__main__":
    Similar = Similarity()
    send = cv2.imread("test.jpg")
    Similar.result(send)
    print(Similar.result_dict)


