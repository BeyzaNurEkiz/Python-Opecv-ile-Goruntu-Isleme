import cv2
import matplotlib.pyplot as plt
import numpy as np 


foto=cv2.imread("resimler/grilena.png")

aynalananResim= cv2.copyMakeBorder(foto,0,0,512,0,cv2.BORDER_REFLECT)

cv2.imshow("Aynalama",aynalananResim)
cv2.waitKey(0)
cv2.destroyAllWindows()