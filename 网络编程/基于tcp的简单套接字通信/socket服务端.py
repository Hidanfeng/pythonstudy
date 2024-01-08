from socket import *
import os
from multiprocessing import Process,Manager
from time import sleep
#1创建socket对象
sk = socket(AF_INET,SOCK_STREAM) #流式协议=》tcp协议
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#2绑定地址
sk.bind(('127.0.0.1',8092))

#3监听链接请求
sk.listen(5) #5指的是半链接池的大小

#等待链接


def talk(conn, ardess):
    while True:
       try:
           # 收消息，发消息
           mes = conn.recv(1024)
           if len(mes)==0:
               break
           conn.send(mes.upper())
           print(mes.decode('utf-8'))
       except Exception:
           break
if __name__ == '__main__':
    while True:
        #4取出链接请求
        conn, ardess = sk.accept()
        print(ardess)

        #5 数据传输
        p = Process(target=talk,args=(conn, ardess))
        p.start()
    #6关闭链接 服务结束
    conn.close()  #关闭当前链接
    sk.close()  #关闭服务端
