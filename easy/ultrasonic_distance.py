import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=17
ECHO=27
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
	while True:
		GPIO.output(TRIG,0)
		time.sleep(2E-6)
		GPIO.output(TRIG,1)
		time.sleep(10E-6)
		GPIO.output(TRIG,0)
		while GPIO.input(ECHO)==0:
			pass
		echostart=time.time()
		while GPIO.input(ECHO)==1:
			pass
		echostop=time.time()
		ptt=echostop-echostart
		distance=ptt*5314.64*2.54
		dtt=distance/2
		CM=dtt*2.54
		print(round(dtt,2),'inches---',round(CM,2),'cm')
		time.sleep(.1)
		
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Goodbye')
	time.sleep(1)
