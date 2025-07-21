import RPi.GPIO as GPIO
import time
notionPin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(notionPin,GPIO.IN)
time.sleep(10)
try:
	while True:
		motion=GPIO.input(notionPin)
		if motion==1:
			print('Motion Detected!!!')
		else:
			print('.')
		time.sleep(.1)
		
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GOODBYE')	
