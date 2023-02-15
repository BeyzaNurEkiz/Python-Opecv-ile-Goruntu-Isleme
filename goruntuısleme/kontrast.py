import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('resimler/grilena.png') 
alpha=3
beta=0
contrast = cv2.convertScaleAbs(resim, alpha=alpha, beta=beta)

plt.subplot(121),plt.imshow(resim),plt.title('Orijinal Hali')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(contrast),plt.title('Kontrast Filtresi')
plt.xticks([]), plt.yticks([])
plt.show()