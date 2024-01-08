from  multiprocessing import Process
import time

def task():
    print('任务开始')
    time.sleep(10)
    print('子进程结束')


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    time.sleep(8)
    print('主进程结束')