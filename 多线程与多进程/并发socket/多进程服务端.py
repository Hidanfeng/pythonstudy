import socket
from multiprocessing import Process,set_start_method

server_clint = socket.socket()
server_clint.bind(('127.0.0.1',8092))
server_clint.listen(5)


def task(conn):

    while True:
        try:
            data = conn.recv(1024)
        except:
            break
        if not data:
            break
        print(data.decode('utf-8'))
        conn.send(data.upper())
    conn.close()



if __name__ == '__main__':
    set_start_method('fork')
    while True:
        conn, adress = server_clint.accept()
        p = Process(target=task,args=(conn,))
        p.start()

