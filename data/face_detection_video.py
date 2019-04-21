import importlib
import time
import sys
importlib.reload(sys)
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

#fgbg = cv2.createBackgroundSubtractorMOG2()
a=1
while(a!=2):
    #print(time.time())
    ret, frame = cap.read()
    #fgmask = fgbg.apply(frame)
    cv2.imwrite("a.png", frame)
    imagepath =r"a.png"  # r'./heat.jpg'
    # 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
    face_cascade = cv2.CascadeClassifier(
        r'G:\UF\demo\haarcascade_frontalface_default.xml')
    # 读取图片
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    #a=format(len(faces))
    #print(a)
    #print(format(len(faces)))
    #print("发现{0}个人脸!".format(len(faces)))
    for (x, y, w, h) in faces:
        # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
        cv2.circle(image, (int(((x + x + w) / 2)), int(((y + y + h) / 2))), int(w / 2), (0, 255, 0), 2)
        cv2.imshow("Finding Faces!", image)
    #cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()