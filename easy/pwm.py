import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,0)
pwm_value=int(input('Enter a value[0 to 100]: '))
mypwm=GPIO.PWM(37,100)
mypwm.start(pwm_value)
sleep(2)
GPIO.cleanup()
