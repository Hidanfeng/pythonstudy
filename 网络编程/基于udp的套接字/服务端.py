import socket
server_sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_sk.bind(('127.0.0.1',8980))
while True:
    msg,addr = server_sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    server_sk.sendto(msg,addr)