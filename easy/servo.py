import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,0)
mypwm=GPIO.PWM(26,50)
for i in range(15):
        mypwm.start(i)
        print(i)
        sleep(.05)
for i in reversed(range(15)):
        mypwm.start(i)
        print(i)
        sleep(.05)
GPIO.cleanup()

