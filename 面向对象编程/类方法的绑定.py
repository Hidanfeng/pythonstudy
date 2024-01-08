name ='xu'
age = 18
class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def new_obj(cls):
        print(name)
        return cls(name,age)

    # @staticmethod
    def static_fuc(self):
        an = 'sun'
        print(an)
        return an

    def func(self):
        print(self.name)


obj1=people('sun',18)
# res = obj1.new_obj()
# people.new_obj()
people.func(obj1)



# print(res.__dict__)
# obj2=people.new_obj()
# print(obj2.__dict__)


