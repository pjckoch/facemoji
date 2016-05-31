import cv2
import numpy as np
from PIL import Image


def image_as_nparray(image):
    return np.asarray(image)


def nparray_as_image(nparray, mode='RGB'):
    return Image.fromarray(np.asarray(np.clip(nparray, 0, 255), dtype='uint8'), mode)


def load_gray_image(source):
    image = cv2.imread(source)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def draw_with_alpha(source_image, image_to_draw, x, y, w, h):
    image_to_draw = image_to_draw.resize((h, w), Image.ANTIALIAS)
    image_array = image_as_nparray(image_to_draw)
    for c in range(0, 3):
        source_image[y:y + h, x:x + w, c] = image_array[:, :, c] * (image_array[:, :, 3] / 255.0) \
                                            + source_image[y:y + h, x:x + w, c] * (1.0 - image_array[:, :, 3] / 255.0)