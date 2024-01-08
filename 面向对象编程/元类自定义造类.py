'''
自定义类
'''
#1 类名称
import time

class_name = 'ftp'
#2基类
class_bases = (object,)
#3、执行类子代码，产生名称空间
class_dict = {}
class_body = '''
def __init__(self,score,name):
    self.name =name   
    self.score = score

def name_str(self):
    print(self.name)
'''
exec(class_body,{},class_dict)
print(class_dict)

#4 调用元类
ftp = type(class_name,class_bases,class_dict)
print(ftp.__dict__)
obj = ftp(29,'xu')
obj.name_str()

print('****************************自定义元类***************************')
'''
自定义元类
'''

class Mytype(type):
    def __call__(self, *args, **kwargs):
        print(self)
        human_obj  = self.__new__(self)
        self.__init__(human_obj,*args,**kwargs)
        return human_obj

#Mytype(class_name,class_bases,class_dict)
#调用了内置元类type的call方法
#1调用Mymeta的__new__方法，产生一个空对象
#2调用Mymeta 的init方法，初始化对象StanfordTeacher
#3返回初始化好的类

class Human(metaclass=Mytype):
    '''
    这个类是
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print('%s 在说她的年纪是 %d' %(self.name,self.age) )

#
obj = Human('sun',18)
# print(obj)

