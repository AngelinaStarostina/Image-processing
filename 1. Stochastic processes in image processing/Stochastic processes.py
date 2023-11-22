import matplotlib.pyplot as plt
import numpy as np
import math


def rotate_matrix(source, ang, height, width):
    new_im = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            x = int((i - x0) * math.cos(ang) - (j - y0) * math.sin(ang)) + x0
            y = int((i - x0) * math.sin(ang) + (j - y0) * math.cos(ang)) + y0

            if x < height and y < width:
                if x > 0 and y > 0:
                    new_im[x, y] = source[i, j]
    plt.imshow(new_im)
    plt.show()
    return new_im


img = cv2.imread('C:/R/img.jpg')
b, g, r = cv2.split(img)
height = len(g)
width = len(g[0])
x0 = int(height / 2)
y0 = int(width / 2)
plt.imshow(img)
plt.show()
plt.imshow(g)
plt.show()

angle = 81
rad = math.radians(angle)
rot_im1 = rotate_matrix(g, rad, height, width)
rot_im2 = rotate_matrix(rot_im1, -rad, height, width)
res = np.subtract(g, rot_im2)
res = np.abs(res)
plt.imshow(res)
plt.show()
