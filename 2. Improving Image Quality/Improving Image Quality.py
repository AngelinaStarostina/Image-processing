import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


def apply_mask(image, mask):
    width = image.shape[1]
    height = image.shape[0]
    mask_range = int(math.floor(mask.shape[0]/2))

    res_image = np.zeros((height, width)).astype(np.int64)

    for i in range(mask_range, width - mask_range):
        for j in range(mask_range, height - mask_range):
            for k in range(-mask_range, mask_range + 1):
                for h in range(-mask_range, mask_range + 1):
                    res_image[j, i] += (mask[mask_range+h, mask_range+k] * image[j+h, i+k])
    return res_image


img = cv2.imread('C:/R/img.jpg', 1)
K = np.array([[0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]])
plt.imshow(img)
plt.show()
b, g, r = cv2.split(img)
b1 = apply_mask(b, K)
g1 = apply_mask(g, K)
r1 = apply_mask(r, K)
plt.imshow(cv2.merge((b1, g1, r1)))
plt.show()
b_sum = (b + b1)
g_sum = (g + g1)
r_sum = (r + r1)
plt.imshow(cv2.merge((b_sum, g_sum, r_sum)).astype(np.int64))
plt.show()
for i in range(len(b_sum)):
    for j in range(len(b_sum[0])):
        b_sum[i, j] = min(b_sum[i, j], 255)
        g_sum[i, j] = min(g_sum[i, j], 255)
        r_sum[i, j] = min(r_sum[i, j], 255)
plt.imshow(cv2.merge((b_sum, g_sum, r_sum)).astype(np.int64))
plt.show()
