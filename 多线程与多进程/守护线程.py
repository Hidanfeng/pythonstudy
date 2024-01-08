from  threading import Thread
import time

def task1(name):
    print(f'{name} 正在运行')
    time.sleep(1)
    print(f'{name} 运行结束')


def task2(name):
    print(f'{name} 正在运行')
    time.sleep(0.9)
    print(f'{name} 运行结束')


if __name__ == '__main__':
    t1 = Thread(target=task1,args=('task1',))
    t2 = Thread(target=task2,args=('task2',))
    t1.daemon =True
    t1.start()
    t2.start()
    print('主线程')
