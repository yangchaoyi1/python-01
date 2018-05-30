from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("",7788))
recvData = udpSocket.recvfrom(1024)
"""
destIp = input("请输入目的ip：")
destPort = int(input("请输入目的port："))
sendData = input("请输入要发送的数据：")

udpSocket.sendto(sendData.encode('utf-8'),(destIp,destPort))"""
content,destInfo = recvData
print("content is %s"%content)
print("content is %s"%content.decode("gb2312"))