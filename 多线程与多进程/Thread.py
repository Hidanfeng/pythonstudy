from  threading import Thread
from  time import sleep

print('主线程程执行开始')

#定义一个函数，作为新线程的执行入口函数
def threadFunc(arg1,arg2):
    print('子线程 开始\n')
    sleep(5)
    print('子线程 结束')

# 创建一个Thread 类的实例对象
thread = Thread(
    target=threadFunc,
    args=('a','b')
)
thread.start()
# thread.join()
print('主线程结束')