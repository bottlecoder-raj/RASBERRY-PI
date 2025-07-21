import socket
import time
bufferSize=1024
msgFromServer="Howdy Client,Happy to your server!"
ServerPort=2222
ServerIP='10.180.107.226'
bytesToSend=msgFromServer.encode('utf-8')
RPIsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP,ServerPort)) 
print('Server is up and listening. . .')
cnt=0
while True:
	message,address=RPIsocket.recvfrom(bufferSize)
	message=message.decode('utf-8')
	print(message)
	print('Client Address',address[0])
	if message=='INC':
		cnt=cnt+1
	if message=='DEC':
		cnt=cnt-1
	msg=str(cnt)
	msg=msg.encode('utf-8')		
	RPIsocket.sendto(msg,address)
