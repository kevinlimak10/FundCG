import numpy as np
import cv2 as cv

img = cv.imread('baboon.png')  # original
img2 = cv.imread('baboon.png')  # aplicar grayscale com media aritmetica, pesos iguais por canal
img3 = cv.imread('baboon.png')  # aplicar grayscale com media ponderada, usando a distribuição dos cones RGB

print(img.shape)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        media = img.item(i, j, 0) * 0.333 + img.item(i, j, 1) * 0.333 + img.item(i, j, 2) * 0.3333
        mediaPond = img.item(i, j, 0) * 0.07 + img.item(i, j, 1) * 0.71 + img.item(i, j, 2) * 0.21

        # img2 recebe o valor de intensidade resultante da média aritmética dos canais
        img2.itemset((i, j, 0), media)  # canal B
        img2.itemset((i, j, 1), media)  # canal G
        img2.itemset((i, j, 2), media)  # canal R

        # img3 recebe o valor de intensidade resultante da média ponderada dos canais
        img3.itemset((i, j, 0), mediaPond)  # canal B
        img3.itemset((i, j, 1), mediaPond)  # canal G
        img3.itemset((i, j, 2), mediaPond)  # canal R
    # print(img[i,j])

cv.imshow("Colorida", img)
cv.imshow("GrayScale Media Aritmetica", img2)
cv.imshow("GrayScale Media Ponderada", img3)
k = cv.waitKey(0)