import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

L1=37
L2=35
L3=33
L4=31
L5=29
GPIO.setup(L1,GPIO.OUT)
GPIO.setup(L2,GPIO.OUT)
GPIO.setup(L3,GPIO.OUT)
GPIO.setup(L4,GPIO.OUT)
GPIO.setup(L5,GPIO.OUT)


GPIO.cleanup()
