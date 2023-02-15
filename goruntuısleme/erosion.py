import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('resimler/morfoloji2.jpeg')
kernel = np.ones((5,5),np.float32)/25
erosion = cv2.erode(resim,kernel,iterations = 1)

plt.subplot(121),plt.imshow(resim),plt.title('Orijinal Hali')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Aşındırma/Erosion')
plt.xticks([]), plt.yticks([])
plt.show()