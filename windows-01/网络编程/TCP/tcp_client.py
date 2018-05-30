from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(("10.216.11.214",9090))

client_socket.send("haha".encode("gb2312"))

recv_data = client_socket.recv(1024)

print("recv_data:%s"%recv_data)

client_socket.close()