# -*- coding: utf-8 -*-
# @File    : canny_edge_detection.py
# @Author  : Hua Guo
# @Time    : 2019/4/15 下午5:28
# @Disc    :


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../../playing-card-detection-master/input/person.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()