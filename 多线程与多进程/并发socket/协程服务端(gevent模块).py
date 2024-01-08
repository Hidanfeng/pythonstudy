from gevent import monkey
monkey.patch_all()
from gevent import spawn

from threading import Thread
import socket



def task(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print(data.decode('utf-8'))
                conn.send(data)
        except:
            break
    conn.close()

def run(adress,port):
    server = socket.socket()
    server.bind((adress, port))
    server.listen(5)
    while True:
        conn, client_adress = server.accept()
        # t = Thread(target=task,args=(conn,))
        # t.start()
        spawn(task,conn)

if __name__ == '__main__':
    adress = '127.0.0.1'
    port = 8898
    g = spawn(run,adress,port)
    g.join()



