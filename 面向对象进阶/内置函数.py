class Fitst_A(object):
    def __init__(self,name):
        self.name = name
    @classmethod
    def fancier(cls):
        print('A','fucna')

class Second_B(Fitst_A):

    def __init__(self,name):
        self.name = name
        print(self.name)

    def fucnb(self):
        print('fucb')

    def __call__(self, *args, **kwargs):
        print('call')


obj1 = Fitst_A('xu')
obj2 = Second_B('sun')
obj2()
# obj2.fucna()
# print(isinstance(obj1,Fitst_A))  #判断obj1 是否是Fitst_A的对象
# print(issubclass(Second_B,Fitst_A)) #判断Second_B 是否是Fitst_A的派生类

# print(hasattr(Fitst_A,'fucna'))   # 判断对象obj1，中是否有一个fucna的属性
# res = getattr(Fitst_A,'fucna')    # 调用对obj1中的属性fucnb
# res()