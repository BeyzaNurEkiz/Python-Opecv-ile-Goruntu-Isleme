import cv2
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread('resimler/lena.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()



