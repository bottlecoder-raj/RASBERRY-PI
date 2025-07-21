import cv2
import time

print(cv2.__version__)
dispW = 800
dispH = 480

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

#Initialize rectangle property
boxW=250
boxH=125
tlc=50
tlr=75
lrc=tlc+boxW
lrr=tlr+boxH
deltaC=2
deltaR=2
thickness=-1
Rcolor=(125,255,0)

# Initialize timer
prev_time = time.time()

while True:
    stat, frame = cam.read()

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Overlay FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    if tlc+deltaC<0 or lrc+deltaC>dispW-1:
        deltaC=deltaC*(-1)
    if tlr+deltaR<0 or lrr+deltaR>dispH-1:
        deltaR=deltaR*(-1)
    tlc=tlc+deltaC
    tlr=tlr+deltaR
    lrc=lrc+deltaC
    lrr=lrr+deltaR
    cv2.rectangle(frame,(tlc,tlr),(lrc,lrr),Rcolor,thickness)
                
                
    

    cv2.imshow('Picam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
