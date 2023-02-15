import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('resimler/lena.png',0)
rows,cols = resim.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
cıktı = cv2.warpAffine(resim,M,(cols,rows))

cv2.imshow("Orijinal resim",resim)
cv2.imshow('Ters Resim',cıktı)
cv2.waitKey(0)
cv2.destroyAllWindows()