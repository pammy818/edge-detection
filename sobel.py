import cv2
import numpy as np

#step1:compressed image size
image=cv2.imread('greenscreen.jpg',0) 
rows,cols=image.shape 
g_f = np.copy(image)
g_f = g_f.astype("float")


sobel = np.zeros((rows, cols))

for x in range(rows-1):
    for y in range(cols-1):
        gx = abs((g_f[x + 1, y - 1] + g_f[x + 1, y]+ g_f[x + 1, y] + g_f[x + 1, y + 1]) - (
            g_f[x - 1, y - 1] + g_f[x - 1, y] + g_f[x - 1, y]+ g_f[x - 1, y + 1]))
        gy = abs((g_f[x - 1, y - 1] + g_f[x, y - 1] + g_f[x, y - 1]+ g_f[x + 1, y - 1]) - (
            g_f[x - 1, y +1] + g_f[x, y + 1] + g_f[x, y + 1]+ g_f[x + 1, y + 1]))
        if gx>=30 and gy >= 30:
         sobel[x,y] = gx + gy
 
cv2.imshow('sobel',sobel)

cv2.waitKey(0)