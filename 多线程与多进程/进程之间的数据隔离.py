from multiprocessing import Process
import time
x = 8
def func():
    global x
    x = 9
    time.sleep(3)
    print('func:',x)



if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.join()
    # time.sleep(3)
    print(x)