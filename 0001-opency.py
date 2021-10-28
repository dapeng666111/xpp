import requests
import requests
import cv2
import numpy as np
import face_recognition





# url='https://www.baidu.com/'
# headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
# response=requests.get(url=url,headers=headers)
# a=open('./url.html','w',encoding='utf-8')
# a.write(response.text)


##输入图片
# a=np.array([[[0,0,0],[0,0,255]],
#             [[0,255,0],[0,255,0]],
#             [[255,0,0],[255,0,0]]
#
# ])
# cv2.imwrite('image/xpp.png',a)

##读取图片
# img=cv2.imread('image/fly.png')
# print(img.shape)

# #转化为灰色图像
# img=cv2.imread('image/fly.png')
# a=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imwrite('image/fly_gray.png',a)

#人脸识别
#打开摄像头
a=cv2.VideoCapture(0)
while 1:
    ret,frame = a.read()     #反馈画面
    face=face_recognition.face_locations(frame)  #面部区域
    for top,right,bottom,left in face:
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),6)
    cv2.imshow('video',frame)   #显示画面
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
a.release()
cv2.destroyAllWindows()
