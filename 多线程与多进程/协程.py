'''
携程 也可以称为微线程，它是一种用户态内的上下文切换技术，简单说就是在单线程下实现并发

进程：资源单位
线程：执行单位
协程：程序员人为创造出来的，不存在（切换+保存状态）
就是通过代码来监听io，一旦程序遇到io，就在代码层面上自动切换，给cpu的感觉就是我们程序没有io
注意：切换不一定是提升效率，还可能降低效率 当遇到io时候切换会提升效率，对于计算密集型来说，切换会降低效率
'''

#计算密集型
import time
#
# def f1():
#     n = 0
#     for i in  range(10000000):
#         n +=1
#
#
#
# def f2():
#     n =0
#     for i in  range(10000000):
#         n +=1
#
#
# start = time.time()
# f1()
# f2()
# end = time.time()
# print(end-start)  # 1.176401138305664

#
# def f1():
#     n = 0
#     for i in  range(10000000):
#
#         n +=1
#         yield
#
#
# def f2():
#     g = f1()
#     n =0
#     for i in  range(10000000):
#         n +=1
#         next(g)
#
#
# start = time.time()
# f2()
# end = time.time()
# print(end-start)  # 2.333256959915161

#io密集型

from gevent import spawn
from gevent import monkey
monkey.patch_all()
def task1():
    for _ in range(2):
        print('task1')
        time.sleep(1)

def task2():
    for _ in  range(2):
        print('task2')
        time.sleep(1)



start = time.time()
# task1()
# task2()
g1 = spawn(task1)
g2 = spawn(task2)
g1.join()
g2.join()
end = time.time()
print(end-start)
