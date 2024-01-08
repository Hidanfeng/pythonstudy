from  threading import Thread,Lock
import time

num = 4
mutex = Lock()
def task():
    global num
    mutex.acquire()
    tump = num
    time.sleep(0.05)
    num = tump -1
    mutex.release()




if __name__ == '__main__':
    l = []
    for i in  range(num):
        t = Thread(target=task)
        l.append(t)
        t.start()
    for i in l:
        i.join()

    print(num)