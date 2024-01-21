#装饰器实现单例模式
#
# def worenp(cls):
#     obj = None
#     def inner(*args,**kwargs):
#         nonlocal obj
#         if not obj:
#             obj = cls(*args,**kwargs)
#         return obj
#     return inner
#
# @worenp
# class Human():
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#
# person1 = Human('xu',18)
# person2 = Human('sun',18)
# print(person2,person1)

# __new__ 方法
#
# class Human():
#     obj = None
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = super().__new__(cls)
#         print('哈哈')
#         return cls.obj
#
#
# #类加括号
# person1 = Human('xu',18)
# person2 = Human('sun',18)
# print(person1.name)

#元类方法

class Mytype(type):
    obj = None
    def __call__(self, *args, **kwargs):
        if not self.obj:
            self.obj = self.__new__(self)
        self.__init__(self.obj,*args, **kwargs)
        return self.obj


class Human(metaclass=Mytype):

    def __init__(self,name,age):
        self.name= name
        self.age = age


person1 = Human('xu',18)
person2 = Human('sun',18)
print(person1.name)