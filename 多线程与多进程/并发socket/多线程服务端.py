from threading import Thread
import socket



def task(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            else:
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
        t = Thread(target=task,args=(conn,))
        t.start()

if __name__ == '__main__':
    adress = '127.0.0.1'
    port = 8898
    run(adress,port)

