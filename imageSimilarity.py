import cv2

class Similarity:
    
    def imagetoBlackandWhite(image,lowTH=127,highTH=255):   
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, lowTH, highTH, cv2.THRESH_BINARY)
        return blackAndWhiteImage

    def Similarity1(image1,image2):
        img1 = cv2.resize(image1,(300,300), interpolation = cv2.INTER_AREA)
        img2 = cv2.resize(image2,(300,300), interpolation = cv2.INTER_AREA)
        blackwhiteimage1 = Similarity.imagetoBlackandWhite(img1)
        blackwhiteimage2 = Similarity.imagetoBlackandWhite(img2)
        width = blackwhiteimage1.shape[1]
        height = blackwhiteimage1.shape[0]
        ikisidebeyaz = 0
        ikisidesiyah = 0
        birincibeyazikincisiyah = 0
        ikincibeyazbirincibeyaz = 0
        toplam = 0
        for i in range(0,height):
            for j in range(0,width):
                toplam +=1
                if 255 == int(blackwhiteimage1[i][j]) and 255 == int(blackwhiteimage2[i][j]):
                    ikisidebeyaz +=1
                elif 255 == int(blackwhiteimage1[i][j]) and 0 == int(blackwhiteimage2[i][j]):
                    birincibeyazikincisiyah +=1
                elif 0 == int(blackwhiteimage1[i][j]) and 255 == int(blackwhiteimage2[i][j]):
                    ikincibeyazbirincibeyaz +=1
                elif 0 == int(blackwhiteimage1[i][j]) and 0 == int(blackwhiteimage2[i][j]):
                    ikisidesiyah +=1

        yuzde = ((ikisidebeyaz+ikisidesiyah)/toplam)*100
        print("Similarity 1 : %",round(yuzde,2))
        # A sayısı B sayısının yüzde kaçı = (A/B)*100  ~ (A/B)/100

img1 = cv2.imread("images/tallvase.jpg")
img2 = cv2.imread("images/tallvase1.jpg")

Similarity.Similarity1(img1,img2)