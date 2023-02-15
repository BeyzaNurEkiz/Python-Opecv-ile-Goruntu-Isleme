import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('resimler/lena.png',0)
rows,cols = resim.shape

M = np.float32([[1,0,100],[0,1,50]])
cikti = cv2.warpAffine(resim,M,(cols,rows))

cv2.imshow("Orijinal resim",resim)
cv2.imshow('Otelenmis Resim',cikti)
cv2.waitKey(0)
cv2.destroyAllWindows()