'''
io密集形
'''
from multiprocessing import Process
from threading import Thread
import time

def task():
    # time.sleep(1)              #io密集型
    for i in range(2000000):    #计算密集型
        count =0
        count  +=1


if __name__ == '__main__':
    start_time = time.time()
    l = []
    for i in range(100):
        p = Process(target=task)
        # t = Thread(target=task)
        p.start()
        # t.start()
        l.append(p)

    for i in l:
        i.join()
    end_time = time.time()
    print(end_time-start_time)
