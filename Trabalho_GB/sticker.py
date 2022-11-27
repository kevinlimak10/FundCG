import cv2 as cv
import numpy as np
from stickerConfig import *

class Sticker:
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        self.scale = scale

        # redimensiona a imagem do sticker conforme a sua determinada escala
        width = int(image.shape[1] * scale / 100)
        height = int(image.shape[0] * scale / 100)
        dim = (width, height)
        self.image = cv.resize(image, dim, interpolation=cv.INTER_AREA)


stickers = []  # stickers posicionados em tela
stickerIndex = 1  # índice do sticker selecionado nas radio box

def createAlphaMask (alpha_channel):
    return np.dstack((alpha_channel, alpha_channel, alpha_channel))

# função que cola o sticker transparente no frame/imagem capturado
def stickerTransparent(background, sticker, x_offset, y_offset):
    bg_h, bg_w, bg_channels = background.shape
    fg_h, fg_w, fg_channels = sticker.shape

    w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
    h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

    if w > 0 or h > 0:
        # clip sticker and background images to the overlapping regions
        bg_x = max(0, x_offset)
        bg_y = max(0, y_offset)
        fg_x = max(0, x_offset * -1)
        fg_y = max(0, y_offset * -1)
        sticker = sticker[fg_y:fg_y + h, fg_x:fg_x + w]
        background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]

        # separate alpha and color channels from the sticker image
        sticker_colors = sticker[:, :, :3]
        alpha_channel = sticker[:, :, 3] / 255  # 0-255 => 0.0-1.0

        # construct an alpha_mask that matches the image shape
        alpha_mask = createAlphaMask(alpha_channel)

        # combine the background with the sticker image weighted by alpha
        composite = background_subsection * (1 - alpha_mask) + sticker_colors * alpha_mask

        # overwrite the section of the background image that has been updated
        background[bg_y:bg_y + h, bg_x:bg_x + w] = composite
    return background


# função para selecionar o sticker na radio box
def handleStickerIndex(*args):
    global stickerIndex
    stickerIndex = args[0]

def printStickers(frame):
    for sticker in stickers:
        frame = stickerTransparent(frame, sticker.image, int((sticker.x - sticker.image.shape[0] / 2)),
                                 int((sticker.y - sticker.image.shape[1] / 2)))
    return frame

def mouseCallback(event, x, y, flags, param):
  global stickerIndex, stickers
  if event == cv.EVENT_LBUTTONDOWN and stickerIndex != 0:
    sticker = Sticker(x, y, cv.cvtColor(stickersList[stickerIndex].image, cv.COLOR_BGR2BGRA), stickersList[stickerIndex].scale)
    stickers.append(sticker)