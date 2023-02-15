
import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('resimler/medyan.png',0)

filteredImg = cv2.medianBlur(img, ksize=3)

cv2.imshow('Original image', img)
cv2.imshow('Filtered image', filteredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()