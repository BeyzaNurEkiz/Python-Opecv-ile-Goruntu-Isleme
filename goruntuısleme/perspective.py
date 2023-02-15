
import cv2
import numpy as np


img = cv2.imread('resimler/perspektif.jpg')


rows,cols,ch = img.shape


pts1 = np.float32([[32,131],[505,95],[30,245],[463,353]])


pts2 = np.float32([[0,0],[500,0],[0,400],[500,400]])

M = cv2.getPerspectiveTransform(pts1,pts2)


dst = cv2.warpPerspective(img,M,(cols, rows))

cv2.imshow('Orjinal Resim', img)
cv2.imshow('Transformed Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()