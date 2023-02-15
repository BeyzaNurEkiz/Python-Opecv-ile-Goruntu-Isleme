import cv2
import matplotlib.pyplot as plt
import numpy as np 

foto=cv2.imread("resimler/grilena.png")
(thresh, blackAndWhiteImage) = cv2.threshold(foto, 100, 255, cv2.THRESH_BINARY)


plt.subplot(121),plt.imshow(foto),plt.title('Orijinal Hali')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blackAndWhiteImage),plt.title('Eşiklenmiş Hali')
plt.xticks([]), plt.yticks([])
plt.show()