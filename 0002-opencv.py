# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:34:19 2021

@author: jywang
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
import face_recognition

#gray-image
# img1=cv2.imread('./image/0010.png',0)
# cv2.imshow('xpp',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img2=cv2.imread('image/0010.png')
# gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# cv2.imshow('1',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img1=cv2.imread('./image/0010.png',0)    #  0是灰度图像
# plt.subplot(2,2,1)
# plt.imshow(img1,cmap='gray',interpolation='bicubic')
# plt.xticks([]),plt.yticks([])
# plt.subplot(2,1,2)
# plt.imshow(img1,cmap='hot',interpolation='bicubic')
# plt.xticks([]),plt.yticks([])
# plt.show()

#视频的读取
# a=cv2.VideoCapture(0)
# while 1:
#     ret, frame = a.read()
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #这个是输入的图像格式转化
#     cv2.imshow('0',frame)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
# a.release()
# cv2.destroyAllWindows()

#人脸捕捉
# a=cv2.VideoCapture(0)
# while 1:
#     ret,frame=a.read()
#     face=face_recognition.face_locations(frame)
#     for top, right, bottom, left in face:
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 6)
#     cv2.imshow('video', frame)  # 显示画面
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# a.release()
# cv2.destroyAllWindows()


#保存video
a=cv2.VideoCapture(0)
while (a.isOpened()):
    ret,frame=a.read()
    frame=cv2.flip(frame,0)
    if cv2.waitKey(1)  &  0xff==ord('q'):
        break


