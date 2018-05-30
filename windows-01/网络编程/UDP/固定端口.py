from  socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("",7788))
udpSocket.sendto(b"haha",("10.216.11.214",8080))
