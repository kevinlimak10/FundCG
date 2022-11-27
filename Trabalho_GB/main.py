import cv2 as cv
from sticker import *

video = cv.VideoCapture(0)
width= int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

initialImg = cv.imread('stickers/mopaz.png')
cv.imshow("smile meter", initialImg)
cv.createTrackbar('Sticker', "smile meter", 0, len(stickersList), handleStickerIndex)

while True:
    check,frame = video.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    frame = printStickers(frame)

    cv.imshow("smile meter", frame)
    cv.setMouseCallback('smile meter', mouseCallback)


    key = cv.waitKey(1)
    if(key == ord('q')):
        break

video.release()
cv.destroyAllWindows

