import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,0)
numBlink=int(input('How many Blinks do you wish for: '))
for i in range(0,numBlink):
	GPIO.output(37,1)
	time.sleep(.5)
	GPIO.output(37,0)
	time.sleep(.5)
GPIO.cleanup()

