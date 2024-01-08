from multiprocessing import Process,set_start_method
import time
def task(name,age):
    print(name,'还活着','年龄',age)
    time.sleep(18)
    print(name,'正常死亡')


if __name__ == '__main__':
    set_start_method('fork')
    p1 = Process(target=task,args=('苏妲己',18))
    # p2 = Process(target=task,args=('西施',18))
    # p.daemon = True
    p1.start()
    # p2.start()
    time.sleep(10)
    print('纣王死了')