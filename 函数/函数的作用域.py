'''
函数查找变量时候按定义的时候来取，现在自己函数内部找，没有找到再去外层最最终找到全局和内置，最后如果没有找到就抛异常
'''



x = 11
def fuc1():
    def fuc2():
        print('fuc2',x)
    x = 22
    fuc2()
x=88

fuc1() #22

def fuc3():
    print(x)

#
# fuc3()
#
#
#


#
# X=coo
# def out1(i):
#     X=lib
#     Y='a'
#     print(X)
#     print(i)
#     def in1(n):
#         print(n)
#         print(X,Y)
#     in1(3)
# out1(lib) # lib lib 3 lib a


