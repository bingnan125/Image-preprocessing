# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:15:34 2018

@author: asus
"""

import cv2

img = cv2.imread('C:\\Users\\asus\\Desktop\\myself\\2 RCN\\RCN\\MNIST\\test\\0250.bmp')
result = img.copy()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,190,255,cv2.THRESH_BINARY)
cv2.imwrite("C:\\Users\\asus\\Desktop\\thresh.jpg", thresh)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
eroded = cv2.erode(thresh, kernel)
cv2.imwrite("C:\\Users\\asus\\Desktop\\eroded.jpg", eroded)

binary, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

color = (0, 255, 0)
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
    temp = result[y:(y + h), x:(x + w)]
    #cv2.imwrite("./result/" + str(x) + ".jpg", temp)
    cv2.imwrite("C:\\Users\\asus\\Desktop\\result.jpg", temp)