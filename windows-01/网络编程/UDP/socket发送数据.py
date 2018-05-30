import socket

udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udpSocket.sendto(b"haha",("10.216.11.214",8080))

udpSocket.sendto(b"haha1",("10.216.11.214",8080))