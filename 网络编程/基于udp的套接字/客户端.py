import socket
client_sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input('>>> ').strip()
    if not msg:continue
    client_sk.sendto(msg.encode('utf-8'),('127.0.0.1',8980))
    back_msg,addr = client_sk.recvfrom(1024)
    print(back_msg.decode('utf-8'),addr)