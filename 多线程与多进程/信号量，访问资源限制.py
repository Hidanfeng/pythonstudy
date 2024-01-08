import time
from threading import Thread,Semaphore
import random
sp = Semaphore(5)


def task(name):
    sp.acquire()
    print(f'{name} 抢到车位')
    time.sleep(random.randint(2,4))
    print(f'{name} 出停车厂')
    sp.release()


if __name__ == '__main__':
    for i in range(8):
        t = Thread(target=task, args=(f'宝马{i+1}',))
        t.start()