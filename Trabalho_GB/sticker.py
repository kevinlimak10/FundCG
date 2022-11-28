import cv2 as cv
import numpy as np
from stickerConfig import *

class Sticker:
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        self.scale = scale
        width = int(image.shape[1] * scale / 100)
        height = int(image.shape[0] * scale / 100)
        dim = (width, height)
        self.image = cv.resize(image, dim, interpolation=cv.INTER_AREA)


stickers = []
stickerIndex = 0

def createAlphaMask (alpha_channel):
    return np.dstack((alpha_channel, alpha_channel, alpha_channel))

def formatSticker(background, sticker, x_offset, y_offset):
    bg_h, bg_w, bg_channels = background.shape
    fg_h, fg_w, fg_channels = sticker.shape

    w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
    h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

    if w > 0 or h > 0:
        bg_x = max(0, x_offset)
        bg_y = max(0, y_offset)
        fg_x = max(0, x_offset * -1)
        fg_y = max(0, y_offset * -1)
        sticker = sticker[fg_y:fg_y + h, fg_x:fg_x + w]
        background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]
        sticker_colors = sticker[:, :, :3]
        alpha_channel = sticker[:, :, 3] / 255
        alpha_mask = createAlphaMask(alpha_channel)
        composite = background_subsection * (1 - alpha_mask) + sticker_colors * alpha_mask
        background[bg_y:bg_y + h, bg_x:bg_x + w] = composite
    return background

def handleStickerIndex(index, windowStickers):
    global stickerIndex
    stickerIndex = index
    canvas = np.zeros((200, 800, 3), np.uint8)

    if stickerIndex != 0:
        text = "Sticker selecionado: " + stickersList[stickerIndex].name
        cv.putText(canvas, text, (20, 20), 2, 1, (200, 255, 155))
    else:
        cv.putText(canvas, 'Nenhum sticker selecionado', (20, 20), 2, 1, (200, 255, 155))
    cv.imshow('stickers', canvas)
def printStickers(frame):
    for sticker in stickers:
        frame = formatSticker(frame, sticker.image, int((sticker.x - sticker.image.shape[0] / 2)),
                              int((sticker.y - sticker.image.shape[1] / 2)))
    return frame

def putSticker(event, x, y, flags, param):
  global stickerIndex, stickers
  if event == cv.EVENT_LBUTTONDOWN and stickerIndex != 0:
    sticker = Sticker(x, y, cv.cvtColor(stickersList[stickerIndex].image, cv.COLOR_BGR2BGRA), stickersList[stickerIndex].scale)
    stickers.append(sticker)

def getStickerIndex():
    return stickerIndex

def clearAllStickers():
    global stickers
    stickers = []