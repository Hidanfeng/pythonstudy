class Mymeta(type):
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self)
        self.__init__(obj,*args, **kwargs)
        print(obj)
        return obj

class StanfordTeacher(object,metaclass=Mymeta):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self.age)
    def say(self):
        print('%s 在说她的年纪是 %d' %(self.name,self.age) )
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)



# obj = Mymeta()
# obj.__call__('nihao','hhh',k1='v1',k2='v2')
# obj('nihao','hhh',k1='v1',k2='v2')

#
# t1 = StanfordTeacher('xu',18)
# print(t1)
# t1.say()
#
st2 = StanfordTeacher('xu',18)
print(st2)


