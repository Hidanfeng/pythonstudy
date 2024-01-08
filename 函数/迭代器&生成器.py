#迭代器 就是重复取值，依赖上一次的取值。不依赖索引的迭代取值方式
#可迭代对象 ：内置有__iter__() 方法的就可以称为可迭代对象，调用__iter__()方法之后就变成可迭代器了。可以转换成迭代器的对象，就称之为可迭代对象。
str = 'kkk'
iterobj = str.__iter__()
iter_self = iterobj.__iter__()
print(iterobj is iter_self) #True


print('''
******************************
''')
def fuc():
    print('uu')
    y = yield 1
    print('xxx',y)
    y = yield 2
#
res = fuc()
# a1 = res.__next__()
# print(a1)
# a2 = res.__next__()
# print(a2)

a = res.send(None)
print(a)

a1 = res.send('jj')
a2 = res.send('jj')
print(a1)