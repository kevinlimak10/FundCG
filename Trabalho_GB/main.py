import cv2 as cv

video = cv.VideoCapture(0)

width= int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

writer= cv.VideoWriter('stories.mp4', cv.VideoWriter_fourcc(*'mp4v'), 20, (width,height))

record = False


while True:
    check,frame = video.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if record:
        writer.write(frame)
        cv.putText(frame, 'Press Space to stop Record', (0, 130), 4, 1, (200, 255, 155))
    else:
        cv.putText(frame, 'Press R to Start Record or Q to exit', (0, 130), 4, 1, (200, 255, 155))
    cv.imshow("smile meter", frame)

    key = cv.waitKey(1)
    if (key == ord('r') and not record):
        record = True
    if (key == ord(' ') and record):
        record = False
        writer.release()
    if(key == ord('q')):
        break

video.release()
cv.destroyAllWindows

