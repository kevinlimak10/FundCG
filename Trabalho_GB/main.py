import cv2 as cv
import numpy as np
from filter import grayscale, original, sketch, sepia, blur, canny

video = cv.VideoCapture(0)

width= int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

writer= cv.VideoWriter('stories.mp4', cv.VideoWriter_fourcc(*'mp4v'), 20, (width,height))

record = False

filters = {
    '0': original,
    '1': grayscale,
    '2': sketch,
    '3': sepia,
    '4': blur,
    '5': canny,
    '6': None,
    '7': None
}

selected_filter = '0'
while True:
    check,frame = video.read()

    frameToPreFilter = cv.resize(frame,(240,160))

    filter = filters.get(selected_filter)
    if filter is not None:
        frame = filter(frame)
    previews = [original(frameToPreFilter),grayscale(frameToPreFilter),sketch(frameToPreFilter),sepia(frameToPreFilter),blur(frameToPreFilter),canny(frameToPreFilter)]

    img_h1 = cv.hconcat([previews[0],previews[3],previews[4]])
    img_h2 = cv.hconcat([previews[1],previews[2],previews[5]])
    # img_final = cv.hconcat([img_h1,img_h2])

    if record:
        writer.write(frame)
        cv.putText(frame, 'Press Space to stop Record', (0, 130), 4, 1, (200, 255, 155))
    else:
        cv.putText(frame, 'Press R to Start Record or Q to exit', (0, 130), 4, 1, (200, 255, 155))
    cv.imshow("Stories", img_h1)

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

