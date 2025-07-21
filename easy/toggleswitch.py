import RPi.GPIO as GPIO
from time import sleep
delay=.1
inPin=40
outPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
LEDstate=0
buttonstate=1
buttonStateold=1
try:
	while True:
		buttonState=GPIO.input(inPin)
		print(buttonstate)
		if buttonstate==1 and buttonStateold==0:
			LEDstate= not LEDstate
			GPIO.output(outPin,LEDstate)
			buttonStateold=buttonstate
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO Good to go')

