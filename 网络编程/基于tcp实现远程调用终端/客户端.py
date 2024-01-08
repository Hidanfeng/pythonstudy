from  socket import *

addres = ('118.25.152.22',8024)
client = socket(AF_INET,SOCK_STREAM)
client.connect(addres)

while True:
    msg = input('>>> ').strip()
    if not msg:continue
    print('msg命令：',msg.encode('utf-8'))
    client.send(msg.encode('utf-8'))
    data_size =int(client.recv(8).decode('utf-8'))
    recv_size = 0
    data = b''
    while recv_size<data_size:
        cmd_res = client.recv(1024)
        recv_size +=len(cmd_res)
        data +=cmd_res
    print('cmd_res',cmd_res)
    print(len(cmd_res))
    print(cmd_res.decode('utf-8'))