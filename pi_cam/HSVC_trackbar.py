#HSVC_TRACKBA
import cv2
import time
import numpy as np

print(cv2.__version__)
dispW = 800
dispH = 480

def TRAC1(val):
    global hueLow
    hueLow=val
    print('Hue Low',hueLow)
def TRAC2(val):
    global huehigh
    huehigh=val
    print('hue max',huehigh)
def TRAC3(val):
    global satlow
    satlow=val
    print('sat min',satlow)
def TRAC4(val):
    global sathigh
    sathigh=val
    print('sat high',sathigh)
def TRAC5(val):
    global vallow
    vallow=val
    print('val min',vallow)
def TRAC6(val):
    global valhigh
    valhigh=val
    print('val max',valhigh)
    


cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# Initialize timer
prev_time = time.time()


#INITIALIZE TRACKBARS
cv2.namedWindow("My Trackbars")
cv2.createTrackbar('Hue Low','My Trackbars',0,179,TRAC1)
cv2.createTrackbar('Hue High','My Trackbars',0,179,TRAC2)
cv2.createTrackbar('Sat Low','My Trackbars',100,255,TRAC3)
cv2.createTrackbar('Sat High','My Trackbars',255,255,TRAC4)
cv2.createTrackbar('val Low','My Trackbars',100,255,TRAC5)
cv2.createTrackbar('val High','My Trackbars',255,255,TRAC6)

# Set default values
huelow = 0
huehigh = 179
satlow = 100
sathigh = 255
vallow = 100
valhigh = 255



while True:
    stat, frame = cam.read()
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    # Overlay FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    
    
    Lowerbound=np.array([huelow,satlow,vallow])
    Upperbound=np.array([huehigh,sathigh,valhigh])
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    myMask=cv2.inRange(frameHSV,Lowerbound,Upperbound)
    myMasksmall=cv2.resize(myMask,(int(dispW/2),int(dispH/2)))  
    objectofInterest=cv2.bitwise_and(frame,frame,mask=myMask)
    objectofInterestSmall=cv2.resize(objectofInterest,(int(dispW/2),int(dispH/2)))  

    
    print(frameHSV[int(dispH/2),int(dispW/2)])

    cv2.imshow('Picam', frame)
    cv2.imshow('MyMASK',myMasksmall)
    cv2.imshow('Object',objectofInterestSmall)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
