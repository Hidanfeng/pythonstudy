'''
 池是用来保证计算机硬件安全的情况下，最大限度的利用计算机资源，降低了程序的运行效率，但是保证了计算机硬件的安全
'''


from  concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,os

pool = ThreadPoolExecutor(10)   #线程池
# pool = ProcessPoolExecutor(3)

def task(name):
    print(name)
    time.sleep(10)
    return name +1

def call_back(res):
    print('call_back',res.result())

if __name__ == '__main__':

    f_list = []
    for i in range(50):
        result = pool.submit(task,i).add_done_callback(call_back) #往线程池中提交任务
        print(f'{i} {result}')
        f_list.append(result)

    # pool.shutdown()       #关闭线程池，等待线程池中所有任务运行完毕
    # for f in f_list:
    #     print(f'任务结果 {f.result()} ')   # f.result()有个阻塞