import RPi.GPIO as GPIO
import time
buzzPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin,GPIO.OUT)
buzz=GPIO.PWM(buzzPin,400)
buzz.start(50)
try:
	while True:
		buzz.ChangeFrequency(100)
		time.sleep(1)
		buzz.ChangeFrequency(300)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('\nEND')
	time.sleep(1)
	
