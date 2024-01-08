from multiprocessing import Process,Queue,set_start_method,JoinableQueue
import random
import time


'''
JoinableQueue
在Queue的基础上增加了一个计数的机制，每put一个数据就会加一
每调用一次task_done，计数就会减一
当计数为0的时候，就会走q.join 后面的代码
'''
#
# class MyProcess(Process):
#     count_consumer = 0
#     def __init__(self,group=None, target=None, name=None, args=(), kwargs={},daemon=None):
#         super().__init__(group, target, name, args, kwargs,daemon)
#         if str(target) == str(consumer):
#             MyProcess.count_consumer += MyProcess.count_consumer






def producer(name,food,q):
    for i in range(8):
        time.sleep(random.randint(1,3))
        print(f'{name}正在生产{food}{i}')
        q.put(f'{food}{i}')


def consumer(name,q):
    while True:
        food = q.get()
        time.sleep(random.randint(1,3))
        print(f'{name}正在吃{food}')
        q.task_done() # 告诉队列，已经拿走了一个数据，并且已经处理完了





if __name__ == '__main__':
    set_start_method('fork')
    q = JoinableQueue()

    p1 = Process(target=producer,args=('徐','炒饭',q))
    p2 = Process(target=producer,args=('孙','炒面',q))
    c1 = Process(target=consumer,args=('我是八戒',q))
    c2 = Process(target=consumer,args=('我是悟空',q))
    p1.start()
    p2.start()
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()


    p1.join()
    p2.join()
    q.join() #等待队列中的所有的数据被取完再执行，主进程走完了，消费者要和主进程一起死亡
    print('主进程结束了')
