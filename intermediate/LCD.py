import LCD1602
import time
LCD1602.init(0x27,1)
try:
	while True:
		LCD1602.write(0,0, 'HELLO WORLD')
except KeyboardInterrupt:
	time.sleep(.2)
	LCD1602.clear()
	print('LCD good to go')		
