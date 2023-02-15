import cv2
import numpy as np

from matplotlib import pyplot as plt

resim=cv2.imread("resimler/netlestirme.PNG",0)


kernel = np.array([[0.1111111, 0.1111111, 0.1111111], [0.1111111, 0.1111111, 0.1111111], [0.1111111, 0.1111111, 0.1111111]])
resim2 = cv2.filter2D(resim,-1,kernel)



cv2.imshow('Orijinal Resim', resim2)
cv2.imshow('Filtrelenmis Resim', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()