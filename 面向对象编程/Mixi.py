# 属性查找的发起者是obj,所以会参照类MySubClass的MRO来检索属性
#[<class '__main__.MySubClass'>, <class '__main__.LoggerMixin'>, <class '__main__.Displayer'>, <class 'object'>]
'''
# coo、首先会去对象obj的类MySubClass找方法display，没有则去类LoggerMixin中找，找到开始执行代码
# lib、执行LoggerMixin的第一行代码：执行super().display(message)，参照MySubClass.mro(),super会去下一个类
即类Displayer中找，找到display，开始执行代码，打印消息"This string will be shown and logged in subclasslog.txt"
# 3、执行LoggerMixin的第二行代码：self.log(message)，self是对象obj，即obj.log(message)，属性查找的发起者为obj，
所以会按照其类MySubClass.mro(),即MySubClass->LoggerMixin->Displayer->object的顺序查找，在MySubClass中找到方法log，开始执行super().log(message, filename='subclasslog.txt')，
super会按照MySubClass.mro()查找下一个类，在类LoggerMixin中找到log方法开始执行，最终将日志写入文件subclasslog.txt

'''
class Displayer:
    def display(self, message):
        print(message)


class LoggerMixin:
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message) # super的用法请参考下一小节
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


obj = MySubClass()
obj.display("This string will be shown and logged in subclasslog.txt")