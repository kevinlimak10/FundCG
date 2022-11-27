from os import listdir
from os.path import isfile, join
from sticker import clearAllStickers
import cv2 as cv

onlyfiles = [f for f in listdir('img') if isfile(join('img', f))]
activeDirImage = 0
def readFiles():
    array = [None]
    for file in onlyfiles:
        readedFile = cv.imread('img/' + file, cv.IMREAD_UNCHANGED)
        array.append(readedFile)
    return array

def handleChangeActiveImage(*args):
    global activeDirImage
    activeDirImage = args[0]
    clearAllStickers()

def getActiveDirImage():
    global activeDirImage
    return activeDirImage




