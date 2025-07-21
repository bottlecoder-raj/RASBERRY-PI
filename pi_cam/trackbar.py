import cv2
import time

def TrackX(val):
    global xPos
    xPos=val
    print('x position',xPos)
def TrackY(val):
    global yPos
    yPos=val
    print('y position',yPos)
def TrackW(val):
    global boxW
    boxW=val
    print('Box width',boxW)
def TrackH(val):
    global boxH
    boxH=val
    print('Box Height',boxH)



print(cv2.__version__)
dispW = 800
dispH = 480

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# Initialize timer
prev_time = time.time()

#INITIALIZE TRACKBARS
cv2.namedWindow("My Trackbars")
cv2.createTrackbar('X pos','My Trackbars',10,dispW-1,TrackX)
cv2.createTrackbar('Y pos','My Trackbars',10,dispH-1,TrackY)
cv2.createTrackbar('Box Width','My Trackbars',10,dispW-1,TrackW)
cv2.createTrackbar('Box Height','My Trackbars',10,dispH-1,TrackH)

boxColor=(0,0,255)


while True:
    stat, frame = cam.read()

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time


    ROI=frame[yPos:yPos+boxH,xPos:xPos+boxW]
    # Overlay FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.rectangle(frame,(xPos,yPos),(xPos+boxW,yPos+boxH),boxColor,3)

    cv2.imshow('Picam', frame)
    cv2.imshow('', ROI)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
