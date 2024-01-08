import time
from multiprocessing import Process,Manager
from time import sleep

def f(taskno,return_dict):
    sleep(2)
    # 存放计算结果到共享对象中
    return_dict[taskno] = taskno



class Systemcode(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print(self.name)



#
if __name__ == '__main__':
    p = Systemcode('xu')
    p.start()
#     manager = Manager()
#     # 创建 类似字典的 跨进程 共享对象
#     return_dict = manager.dict()
#     plist = []
#     for i in range(10):
#         p = Process(target=f, args=(i,return_dict))
#         p.start()
#         plist.append(p)
#
#     # for p in plist:
#     #     p.join()
#     time.sleep(3)
#
#
#     # 从共享对象中取出其他进程的计算结果
#     for k,v in return_dict.items():
#         print (k,v)
#     print('get result...')

#
#
# from multiprocessing import Process
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     global n
#     n=0
#     print('子进程内: ',n)
#
#
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     print('主进程内: ',n)
