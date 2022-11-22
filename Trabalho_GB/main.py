import cv2 as cv
import numpy as np
from filter import grayscale, original, sketch, sepia, blur, canny

video = cv.VideoCapture(0)

width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
sizeHeader = int(height * 0.2)

writer = cv.VideoWriter('stories.mp4', cv.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

record = False

posList = []


def onMouse(event, x, y, flags, param):
    global posList
    if event == cv.EVENT_LBUTTONDOWN:
        posList.append((x, y))

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
while True:
    check, frame = video.read()
    frameToPreFilter = cv.resize(frame, (widthHeader, sizeHeader))

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

    if record:
        writer.write(frame)
        cv.putText(frame, 'Press Space to stop Record', (0, 130), 4, 1, (200, 255, 155))
    else:
        cv.putText(frame, 'Press R to Start Record or Q to exit', (0, 130), 4, 1, (200, 255, 155))
    cv.imshow("stories", img_final)
    cv.setMouseCallback('stories', onMouse)


    key = cv.waitKey(1)
    if key == ord('r') and not record:
        record = True
    if key == ord(' ') and record:
        record = False
        writer.release()
    if key == ord('q'):
        break

    if key in [ord(k) for k in filters.keys()]:
        selected_filter = chr(key)



video.release()
cv.destroyAllWindows
