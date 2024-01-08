import socket
from threading import Thread,current_thread



def client():
    cu_client = socket.socket()
    cu_client.connect(('127.0.0.1', 8898))
    n = 0
    while True:
        message = f'{current_thread().name} say {n}'
        cu_client.send(message.encode('utf-8'))
        data = cu_client.recv(1024)
        print(data.decode('utf-8'))
        n+=1


if __name__ == '__main__':
    for i in  range(500):
        t = Thread(target=client)
        t.start()