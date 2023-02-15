import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('resimler/grilena.png')

laplacian = cv2.Laplacian(resim, cv2.CV_64F)

plt.subplot(121),plt.imshow(resim),plt.title('Orijinal Hali')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(laplacian),plt.title('Laplacian filtresi')
plt.xticks([]), plt.yticks([])
plt.show()