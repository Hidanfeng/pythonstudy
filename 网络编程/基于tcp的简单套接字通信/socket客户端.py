import socket

#1创建对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2建立链接
sk.connect(('127.0.0.1',8092))
while True:
    msg = input('输入你要发送的')
    if len(msg)==0:
        continue
    if msg =='exit':
        break
    sk.send(msg.encode('utf-8'))
    message = sk.recv(1024).decode('utf-8')
    print(message)
sk.close()