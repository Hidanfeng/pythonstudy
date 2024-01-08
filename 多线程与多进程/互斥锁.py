import multiprocessing
from multiprocessing import Process,Lock
import json
import random
import time

def search_ticket(name):
    with open('tickets','r',encoding='utf-8') as f:
        dic  = json.load(f)
        print(f'用户{name}查询余票：{dic["tickets_num"]}')

def buy_ticket(name):
    with open('tickets','r',encoding='utf-8') as f:
        dic  = json.load(f)
        time.sleep(random.randint(1,5))
        if dic.get("tickets_num") >0:
            dic['tickets_num'] -=1
            with open('tickets','w',encoding='utf-8') as f:
                json.dump(dic,f)
                print(f'用户{name}买票成功')
        else:
            print(f'余票不足，用户{name}买票失败')

def task(name,mutex):

    search_ticket(name)
    mutex.acquire()
    buy_ticket(name)
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in  range(1,9):
        multiprocessing.set_start_method('fork')
        p = Process(target=task,args=(i, mutex))
        p.start()