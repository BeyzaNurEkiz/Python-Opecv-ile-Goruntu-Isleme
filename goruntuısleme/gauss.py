import cv2
import matplotlib.pyplot as plt
import numpy as np 

foto=cv2.imread("resimler/gauss.png")
foto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
output2 = cv2.GaussianBlur(foto, (7, 7), 3)
cv2.imshow('Original image',foto)
cv2.imshow('Gauss image', output2)

cv2.waitKey(0)
cv2.destroyAllWindows()
