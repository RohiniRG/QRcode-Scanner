from pyzbar.pyzbar import decode
import cv2
import numpy


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    for info in decode(frame):
        data = info.data.decode('utf-8')
        print(data)

    cv2.imshow("Result", frame) 
       
cv2.destroyAllWindows()


