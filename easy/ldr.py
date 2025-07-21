import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
	while True:
		lightVAL=ADC0834.getResult(0)
		print('Light value: ',lightVAL)
		sleep(.2)
except KeyboardInterrupt:
	sleep(.1)
	GPIO.cleanup()
