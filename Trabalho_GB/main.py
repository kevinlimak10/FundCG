import cv2 as cv
import numpy as np
from filter import grayscale, original, sketch, sepia, blur, canny
from sticker import *

video = cv.VideoCapture(0)

width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
sizeHeader = int(height * 0.2)

writer = cv.VideoWriter('stories.mp4', cv.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

record = False

posList = []

initialImg = cv.imread('stickers/mopaz.png')
cv.imshow("stories", initialImg)

canvas = np.zeros((200,800,3), np.uint8)

cv.putText(canvas, 'Nenhum sticker selecionado', (20, 20), 2, 1, (200, 255, 155))
cv.imshow("stickers", canvas)
def selectSticker(*args):
    handleStickerIndex(args[0], canvas)

cv.createTrackbar('Sticker', "stickers", 0, len(stickersList) - 1, selectSticker)

def onMouse(event, x, y, flags, param):
    global posList
    if event == cv.EVENT_LBUTTONDOWN:
        posList.append((x, y))

def mouseCallback(event, x, y, flags, param):
    if getStickerIndex() != 0:
        putSticker(event, x, y, flags, param)
    else:
        onMouse(event, x, y, flags, param)

def checkChangeFilter(x,y):
    return


filters = {
    '0': original,
    '1': grayscale,
    '2': sketch,
    '3': sepia,
    '4': blur,
    '5': canny
}

widthHeader = int(width / len(filters))
selected_filter = '0'
cv.setMouseCallback('stories', mouseCallback)

while True:
    check, frame = video.read()
    frameToPreFilter = cv.resize(frame, (widthHeader, sizeHeader))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    frame = printStickers(frame)

    # cv.imshow("stories", frame)
    filter = filters.get(selected_filter)
    if filter is not None:
        frame = filter(frame)

    previews = [original(frameToPreFilter),
                grayscale(frameToPreFilter),
                sketch(frameToPreFilter),
                sepia(frameToPreFilter),
                blur(frameToPreFilter),
                canny(frameToPreFilter)]

    img_preview = cv.hconcat([previews[0], previews[1], previews[2], previews[3], previews[4], previews[5]])

    # resize to original size
    img_preview = cv.resize(img_preview, (width, sizeHeader))
    # get final size
    frame = cv.resize(frame, (width, height - sizeHeader))

    img_final = cv.vconcat([img_preview, frame])


    # cv.resize(frame, (240, 160))

    if len(posList) > 0:
        x,y = posList[0]
        if y > 0 and x > 0 and y <= sizeHeader and x <= width:
            selected_filter = str(int(x/widthHeader))
        posList = []

    cv.imshow("stories", img_final)

    key = cv.waitKey(1)
    if key == ord('q'):
        break


    if key in [ord(k) for k in filters.keys()]:
        selected_filter = chr(key)



video.release()
cv.destroyAllWindows
