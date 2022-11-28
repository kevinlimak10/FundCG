import tensorflow.keras
from PIL import Image, ImageOps
import cv2
import numpy as np

from sticker import *

model = tensorflow.keras.models.load_model('model/keras_model.h5')

steps = [
    cv2.imread('gestureStickers/joinha.png', cv2.IMREAD_UNCHANGED),
    cv2.imread('gestureStickers/coracao.png', cv2.IMREAD_UNCHANGED),
]

def predictMotion(rawframe):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.fromarray(rawframe)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    imgClass = np.argmax(prediction)
    return imgClass

def detectMotion(fr):
    a = predictMotion(fr)
    if a != 2:
        sticker = Sticker(30, 30, cv.cvtColor(steps[a], cv.COLOR_BGR2BGRA),25)
        fr = formatSticker(fr, sticker.image, int((70 - sticker.image.shape[0] / 2)),
                              int((70 - sticker.image.shape[1] / 2)))
    return fr