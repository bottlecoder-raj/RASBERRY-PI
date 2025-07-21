import cv2
import time

print(cv2.__version__)
dispW = 800
dispH = 480

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# Initialize timer
prev_time = time.time()
upperLeft=(250,60)
lowerRight=(450,120)
rcolor=(0,0,255)  #GBR
thickness=5  #-1 to fill the box
cen=(300,400) 
r=25
cthick=-1

while True:
    stat, frame = cam.read()

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    print(frame[0,0])

    # Overlay FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                
    #Overlay rectangle on frame
    cv2.rectangle(frame,upperLeft,lowerRight,rcolor,thickness)
    
    #Overlay circle on frame
    cv2.circle(frame,cen,r,(255,0,0),cthick)
    
    #print color for the pixel on terminal
    print(frame[0,0])

    cv2.imshow('Picam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
