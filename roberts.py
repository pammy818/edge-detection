import cv2
import numpy as np

#step1:compressed image size
image=cv2.imread('greenscreen.jpg',0) 
rows,cols=image.shape 
g_f = np.copy(image)
g_f = g_f.astype("float")


Roberts = np.zeros((rows, cols))

for i in range(rows-1):
    for j in range(cols-1):
        gx = abs(g_f[i + 1, j+ 1] - g_f[i, j])
        gy = abs(g_f[i+ 1, j] - g_f[i, j + 1])
        if gx>=12 and gy >= 12:
           Roberts[i,j] = gx + gy
 
cv2.imshow('roberts',Roberts)

cv2.waitKey(0)