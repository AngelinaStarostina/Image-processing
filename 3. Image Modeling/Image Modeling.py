import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import math

height = 150
width = 150
ang = math.radians(45)


def first_quarter(r, g, b):
    for i in range(int(height/2), 0, -1):
        for j in range(int(width/2), width):
            if isF(i - int(height / 2), j - int(width / 2), 1):
                r[i, j], g[i, j], b[i, j] = 0, 0, 255
    return b


def fourth_quarter(r, g, b):
    for i in range(int(height/2), height):
        for j in range(int(width/2), width):
            if isF(i - int(height / 2), j - int(width / 2), 4):
                r[i, j], g[i, j], b[i, j] = 0, 0, 255


def isF(i, j, quarter):
    a = 0.045
    b = 0
    c = width/4

    if quarter == 1:
        if (a * i ** 2 + b * i + c) >= j >= (a * (i + 2) ** 2 + b * (i + 2) + c):
            return True
    if quarter == 4:
        if (a * i ** 2 + b * i + c) >= j >= (a * (i - 2) ** 2 + b * (i - 2) + c):
            return True
    else:
        return False


def rotate_matrix(source, ang):
    x0 = int(height / 2)
    y0 = int(width / 2)
    new_im = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            x = int((i - x0) * math.cos(ang) - (j - y0) * math.sin(ang)) + x0
            y = int((i - x0) * math.sin(ang) + (j - y0) * math.cos(ang)) + y0

            if x < height and y < width:
                if x > 0 and y > 0:
                    new_im[x, y] = source[i, j]
    return new_im


def rotate(r, g, b, ang):
    r1 = r
    g1 = g
    b1 = b
    source = cv2.merge((r, g, b)).astype(np.int64)
    for i in range(4):
        b = rotate_matrix(b, ang)
        r = rotate_matrix(r, ang)
        g = rotate_matrix(g, ang)
        img1 = cv2.merge((r, g, b)).astype(np.int64)
        source = source + img1
    ang = math.radians(-45)
    for i in range(4):
        b1 = rotate_matrix(b1, ang)
        r1 = rotate_matrix(r1, ang)
        g1 = rotate_matrix(g1, ang)
        img1 = cv2.merge((r1, g1, b1)).astype(np.int64)
        source = source + img1
    return source


def image_mod(height, width):
    r = np.zeros((height, width)).astype(np.int64)
    g = np.zeros((height, width)).astype(np.int64)
    b = np.zeros((height, width)).astype(np.int64)

    first_quarter(r, g, b)
    fourth_quarter(r, g, b)
    img = rotate(r, g, b, ang)
    plt.imshow(img)
    plt.show()
    return cv2.merge((r, g, b)).astype(np.int64)


def apply_mask(image):
    for i in range(0, height, int(height/50)):
        for j in range(0, width, int(width/50)):
            image[i, j] = min(random.random(), 250)
    return image


img = image_mod(height, width)
img = apply_mask(img)
plt.imshow(img)
plt.show()
