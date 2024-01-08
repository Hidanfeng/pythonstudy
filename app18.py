'''
闭包，装饰器，函数
'''
#
#
# x=coo
#
# def decorate():
#     print('running decorator when import')
#     global x
#     x =lib
#     print(x)
#
#
# decorate()
# print(x)
#
# x=coo
#
# def f1():
#     def f2():
#         print(x)
#
#     return f2
#
# def f3():
#     x=3
#     f2=f1() #调用f1()返回函数f2
#     f2() #需要按照函数定义时的作用关系去执行，与调用位置无关
#
# f3() #结果为
#
#写一个可以统计函数运行时间功能的装饰器
# import time
# def timer(fuc):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         res = fuc(*args,**kwargs)
#         end_time =  time.time()
#         print(end_time-start_time)
#         return res
#
#     return inner
# #编写装饰器，为函数加上认证的功能，即要求认证成功才能执行函数
# def certification():
#
#     return

