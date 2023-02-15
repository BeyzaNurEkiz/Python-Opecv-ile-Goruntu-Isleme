import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('resimler/lena.png',0)
rows,cols = resim.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),60,1)
cikti = cv2.warpAffine(resim,M,(cols,rows))

cv2.imshow("Orijinal resim",resim)
cv2.imshow('Donmus Resim',cikti)
cv2.waitKey(0)
cv2.destroyAllWindows()