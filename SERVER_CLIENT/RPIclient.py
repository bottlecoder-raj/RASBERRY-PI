import socket
msgFromClient='Howdy Server, from your Client.'
bytesToSend=msgFromClient.encode('utf-8')
serverAddress=('10.180.107.226',2222)
bufferSize=1024
UDPClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    cmd=input('What do you want to do with counter,INC or DEC? ')
    cmd=cmd.encode('utf-8')
    UDPClient.sendto(cmd,serverAddress)
    data,address=UDPClient.recvfrom(bufferSize)
    data=data.decode('utf-8')
    print('Data from Server ..',data)
    print('Server IP Address: ',address[0])
    print('Server port: ',address[1])
