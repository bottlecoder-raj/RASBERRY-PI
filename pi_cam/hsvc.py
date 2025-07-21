import cv2
import time
import numpy as np

print(cv2.__version__)
dispW = 800
dispH = 480

hueLow=0
hueHigh=15

satLow=100
satHigh=255

valLow=100
valHigh=255

Lowerbound=np.array([hueLow,satLow,valLow])
Upperbound=np.array([hueHigh,satHigh,valHigh])

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# Initialize timer
prev_time = time.time()

while True:
    stat, frame = cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    myMask=cv2.inRange(frameHSV,Lowerbound,Upperbound)
    myMasksmall=cv2.resize(myMask,(int(dispW/2),int(dispH/2)))  
    objectofInterest=cv2.bitwise_and(frame,frame,mask=myMask)
    objectofInterestSmall=cv2.resize(objectofInterest,(int(dispW/2),int(dispH/2)))  
    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    
    print(frameHSV[int(dispH/2),int(dispW/2)])

    # Overlay FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow('Picam', frame)
    cv2.imshow('MyMASK',myMasksmall)
    cv2.imshow('Object',objectofInterestSmall)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
