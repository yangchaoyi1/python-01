#coding=utf-8
from socket import *
def main():
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",7788))
    num = 1
    while True:
        recvInfor = udpSocket.recvfrom(1024)
        udpSocket.sendto(recvInfor[0],recvInfor[1])
        print('已经将接收到的第%d个数据返回给对方,内容为:%s'%(num,recvInfor[0]))
        num+=1

if __name__ == "__main__":
    main()
