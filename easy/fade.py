import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,0)
mypwm=GPIO.PWM(37,100)
for i in range(100):
	mypwm.start(i)
	sleep(.01)
for i in reversed(range(100)):
	mypwm.start(i)
	sleep(.01)
GPIO.cleanup()
