import socket
cu_client  = socket.socket()
cu_client.connect(('127.0.0.1',8898))


while True:
    message = input('>>>>').strip()
    cu_client.send(message.encode('utf-8'))
    data = cu_client.recv(1024)
    print(data.decode('utf-8'))