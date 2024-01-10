'''
属性隐藏，降低使用步骤
'''

class student():
    __x = 9 #类的隐藏
    def __init__(self,score,name):
        self.__name =name    #对象的隐藏
        self.score = score

    @property
    def name(self):
        return self.__name
        # print(self.__name)

    @name.setter
    def name(self,new_name):
        if type(new_name) is not str:
            print('输入有误会')
        else:
            self.__name = new_name
            return self.__name
            # print(self.__name)
    @name.deleter
    def name(self):
        del self.name

    # name = property(get_name,set_name,del_name)

    #
    # def print_score(self):
    #     print('%s :%s'% (self.__name,self.score))



st1 = student(18,'sun')
# print(st1.__dict__)

st1.name = 'xu'
print(st1.name)

# print(student.__dict__)




class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()