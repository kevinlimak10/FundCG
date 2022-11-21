import cv2 as cv
import numpy as np
from numpy import array

def brilho(img, beta_value ):
    img_bright = cv.convertScaleAbs(img, beta=beta_value)

    return img_bright

def grayscale(image):
    converted_image = np.array(image)
    gray_image = cv.cvtColor(converted_image, cv.COLOR_RGB2GRAY)
    return tranformToColorImage(gray_image)

def sketch(image):
    converted_image = np.array(image)
    gray_image = cv.cvtColor(converted_image, cv.COLOR_RGB2GRAY)
    inv_gray_image = 255 - gray_image
    blur_image = cv.GaussianBlur(inv_gray_image, (21, 21), 0, 0)
    sketch_image = cv.divide(gray_image, 255 - blur_image, scale=256)
    return tranformToColorImage(sketch_image)


def sepia(image):
    converted_image = np.array(image)
    converted_image = cv.cvtColor(converted_image, cv.COLOR_RGB2BGR)
    kernel = np.array([[0.272, 0.534, 0.132],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia_image = cv.filter2D(converted_image, -1, kernel)
    sepia_image = cv.cvtColor(sepia_image, cv.COLOR_BGR2RGB)
    return sepia_image


def blur(image):
    b_amount = 9
    converted_image = np.array(image)
    converted_image = cv.cvtColor(converted_image, cv.COLOR_RGB2BGR)
    blur_image = cv.GaussianBlur(converted_image, (b_amount, b_amount), 0, 0)
    blur_image = cv.cvtColor(blur_image, cv.COLOR_BGR2RGB)
    return blur_image


def canny(image):
    threshold1 = 100
    threshold2 = 150
    converted_image = np.array(image)
    converted_image = cv.cvtColor(converted_image, cv.COLOR_RGB2BGR)
    blur_image = cv.GaussianBlur(converted_image, (11, 11), 0)
    canny_image = cv.Canny(blur_image, threshold1, threshold2)
    return tranformToColorImage(canny_image)


def original(image):
    return image


def tranformToColorImage(img):
    image_color = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
    return image_color