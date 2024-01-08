'''
进程 ：资源单位
线程 ：执行单位



创建进程
申请内存空间 消耗资源
拷贝代码 消耗资源

创建线程： 在一个进程内可以创建多个线程
不需要再次申请内存空间
不需要拷贝代码
'''
from  threading import Thread
import time



def task(name):
    print(f'{name} 任务开始')
    # time.sleep(1)
    print(f'{name} 任务结束')




if __name__ == '__main__':
    t1 = Thread(target=task,args=('xu',))
    t1.start()
    # t1.join()
    print('主线程')