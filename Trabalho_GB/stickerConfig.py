import cv2 as cv
class StickerModel:
    def __init__(self, image, name, scale):
        self.image = image
        self.name = name
        self.scale = scale

stickersList = [
    None,
    StickerModel(cv.imread("stickers/anya.png", cv.IMREAD_UNCHANGED), "Anya + Barba branca", 10),
    StickerModel(cv.imread("stickers/darwin.png", cv.IMREAD_UNCHANGED), "Darwin", 15),
    StickerModel(cv.imread("stickers/homer.png", cv.IMREAD_UNCHANGED), "Homer", 15),
    StickerModel(cv.imread("stickers/ladopositivo.png", cv.IMREAD_UNCHANGED), "O lado positivo", 15),
    StickerModel(cv.imread("stickers/macaquinho.png", cv.IMREAD_UNCHANGED), "Macaquinho", 25),
    StickerModel(cv.imread("stickers/vergonha.png", cv.IMREAD_UNCHANGED), "Vergonha", 25),
]