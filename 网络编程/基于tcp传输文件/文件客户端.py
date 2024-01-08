'''
文件的上传和下载
'''
from  socket import *
import json

addres = ('127.0.0.1',8098)
client = socket(AF_INET,SOCK_STREAM)
client.connect(addres)

while True:
    msg = input('>>> ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    #先拿到头部长度
    header_size = int(client.recv(4).decode('utf-8'))
    header_json = client.recv(header_size).decode('utf-8')
    header = json.loads(header_json)
    print(header)
    data_size =header['file_size']
    recv_size = 0

    with open('/Users/danfengxu/Desktop/pythonstudy/day202311/网络编程/基于tcp传输文件/file/xu.txt', 'wb') as f:
        while recv_size<data_size:
            cmd_res = client.recv(1024)
            f.write(cmd_res)
            recv_size +=len(cmd_res)

    print(len(cmd_res))
