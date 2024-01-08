'''
文件的上传和下载
'''
import os
from socket import *
import subprocess
import json
server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8098))

server.listen(5)

while True:

    # 循化的从半连接池中取出链接

    conn,client_addr = server.accept()

    while True:
        try:
            cmd = conn.recv(1024)
            if len(cmd)==0:
                break
            file_list = cmd.decode('utf-8').split()
            print(file_list)
            # cmd = file_list[0].strip()
            # res = subprocess.Popen(cmd,
            #                        shell=True,
            #                        stderr=subprocess.PIPE,
            #                        stdout=subprocess.PIPE)
            # stderr = res.stderr.read()
            # stdout = res.stdout.read()
            # conn.send(stderr)
            # stdstr = stderr+stdout
            # data_size = len(stdstr)
            # conn.send(str(data_size).encode('utf-8'))
            #做一个固定长度的header
            if file_list[1]:
                file_name = file_list[1]
                file_size = os.path.getsize(file_name)
                print(file_name)
            else:
                file_name = None
                file_size = None
            header = {
                'file_name': file_name,
                'file_size': file_size,
                'md5': 'hhhh'
            }

            header_json = json.dumps(header)
            #头部信息
            header_bytes = header_json.encode('utf-8')
            #头部长度
            header_h = bytes(str(len(header_bytes)),'utf-8').zfill(4)
            # print('header: ',header)
            conn.send(header_h)
            conn.send(header_bytes)
            with open(file_name,'rb',encoding='utf-8') as f:
                for line in f:
                    conn.send(line)

            # conn.send(stdstr)
            # print(len(stdstr))
        except Exception:
            break
    conn.close()