import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
rows=[11,13,15,29]
columns=[31,33,35,37]
keypad=[[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]
GPIO.setup(rows[0],GPIO.OUT)
GPIO.setup(rows[1],GPIO.OUT)
GPIO.setup(rows[2],GPIO.OUT)
GPIO.setup(rows[3],GPIO.OUT)

GPIO.setup(columns[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


try:
	while True:
		nopress=True
		nopress_old=True
		for myrow in [0,1,2,3]:
			for mycolumn in [0,1,2,3]:
				GPIO.output(rows[myrow],1)
				butval=GPIO.input(columns[mycolumn])
				GPIO.output(rows[myrow],0)
				if butval==1:
					myChar=keypad[myrow][mycolumn]
					print(myChar)
					nopress=False
				if butval==1 and nopress==False and nopress_old==True:
					print(myChar)
			nopress_old=nopress		
		sleep(.2)
except KeyboardInterrupt:
	sleep(.2)
	GPIO.cleanup()
	print('Goodbye')	
