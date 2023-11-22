import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import statistics


def apply_noise(img, percent):
    r, g, b = cv2.split(img)
    width = img.shape[1]
    height = img.shape[0]
    num_of_points = int(height * width * (percent / 100))
    k = num_of_points

    while k >= 0:
        i = random.randrange(0, height)
        j = random.randrange(0, width)
        p = random.choice([0, 255])
        r[i, j] = p
        g[i, j] = p
        b[i, j] = p
        k -= 1
    return cv2.merge((r, g, b)).astype(np.int64)


def w_filter(img, w_size):
    width = img.shape[1]
    height = img.shape[0]
    for i in range(0, height-w_size):
        for j in range(0, width-w_size):
            img[int(i + w_size/2)][int(j + w_size/2)] = (0.5*(np.max(img[i:i+w_size, j:j+w_size]) + np.min(img[i:i+w_size, j:j+w_size])))
    return img


def median_filter(img, w_size):
    width = img.shape[1]
    height = img.shape[0]
    for i in range(height-w_size):
        for j in range(width-w_size):
            median = statistics.median(img[k, s] for k in range(i, i + w_size) for s in range(j, j + w_size))
            img[int(i + w_size/2)][int(j + w_size/2)] = median
    return img


img = cv2.imread('C:/R/img.jpg', 1)
plt.imshow(img)
plt.show()
r, g, b = cv2.split(img)
noise_img = apply_noise(img, 1)
plt.imshow(noise_img)
plt.show()

r, g, b = cv2.split(noise_img)
r = w_filter(r, 3)
g = w_filter(g, 3)
b = w_filter(b, 3)
w_img = cv2.merge((r, g, b)).astype(np.int64)
plt.imshow(w_img)
plt.show()

r, g, b = cv2.split(noise_img)
r = median_filter(r, 3)
g = median_filter(g, 3)
b = median_filter(b, 3)
m_img = cv2.merge((r, g, b)).astype(np.int64)
plt.imshow(m_img)
plt.show()

r, g, b = cv2.split(noise_img)
r = median_filter(r, 5)
g = median_filter(g, 5)
b = median_filter(b, 5)
m_img = cv2.merge((r, g, b)).astype(np.int64)
plt.imshow(m_img)
plt.show()