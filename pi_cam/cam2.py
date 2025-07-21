import cv2
from picamera2 import Picamera2

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (800, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")

# Start camera
picam2.start()

try:
    while True:
        # Capture frame
        im = picam2.capture_array()
        
        # Display in window
        cv2.imshow("piCam", im)

        # Break loop on 'q' key
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Clean up
    picam2.stop()
    cv2.destroyAllWindows()
    print("Camera and windows closed cleanly.")
