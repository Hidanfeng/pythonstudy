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