import cv2 as cv
import numpy as np
from sticker import *

right_eye_cascade = cv.CascadeClassifier('right.xml')
left_eye_cascade = cv.CascadeClassifier('left.xml')

def detectEye (gray, frame, isLeft):
    eyes = None
    if isLeft:
        eye = left_eye_cascade.detectMultiScale(gray, 1.3, 5)
    else:
        eye = right_eye_cascade.detectMultiScale(gray, 1.3, 5)
    img = cv.imread('liveStickers/eye-left.png', cv.IMREAD_UNCHANGED)

    h, w, *_ = img.shape
    imgH = (h * 3 / 100)
    imgW = (w * 3 / 100)

    for (x,y,w,h) in eye:
        x=x+30
        y=y+30

        roi = frame[y:y+h, x:x+w]

        sticker = Sticker(x, y, cv.cvtColor(img, cv.COLOR_BGR2BGRA),7)
        frame = formatSticker(frame, sticker.image, int((x - sticker.image.shape[0] / 2)),
                              int((y - sticker.image.shape[1] / 2)))
    return frame

