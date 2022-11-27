import cv2 as cv
class StickerModel:
    def __init__(self, image, name, scale):
        self.image = image
        self.name = name
        self.scale = scale

stickersList = [
    StickerModel(cv.imread("stickers/nadaverirmao.png", cv.IMREAD_UNCHANGED), "Nada ver irmão", 25),
    StickerModel(cv.imread("stickers/mopaz.png", cv.IMREAD_UNCHANGED), "Mopaz", 15),
    StickerModel(cv.imread("stickers/loadingcat.png", cv.IMREAD_UNCHANGED), "Loading cat", 15),
    StickerModel(cv.imread("stickers/azideia.png", cv.IMREAD_UNCHANGED), "Azi ideia", 20),
    StickerModel(cv.imread("stickers/coreana.png", cv.IMREAD_UNCHANGED), "Coreana", 20),
    StickerModel(cv.imread("stickers/pigmeu.png", cv.IMREAD_UNCHANGED), "Pigmeu", 20),
    StickerModel(cv.imread("stickers/queloucura.png", cv.IMREAD_UNCHANGED), "Que loucura", 20),
]