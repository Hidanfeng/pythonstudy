from socket import *
import subprocess
server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8089))
server.listen(5)

while True:

    # 循化的从半连接池中取出链接

    conn,client_addr = server.accept()

    while True:
        try:
            cmd = conn.recv(1024)
            if len(cmd)==0:
                break
            res = subprocess.Popen(cmd.decode('utf-8'),
                                   shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
            stderr = res.stderr.read()
            stdout = res.stdout.read()
            # conn.send(stderr)
            stdstr = stderr+stdout
            data_size = len(stdstr)
            # conn.send(str(data_size).encode('utf-8'))
            #做一个固定长度的header
            header = bytes(str(data_size),'utf-8').zfill(8)
            print('header: ',header)
            conn.send(header)
            conn.send(stdstr)
            print(len(stdstr))
        except Exception:
            break
    conn.close()