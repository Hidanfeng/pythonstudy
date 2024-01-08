'''
封装
继承
多态
'''

#封装的属性进行隐藏 __双下划线属性和方法可以在类内部调用
#property 可以将类中的函数封装成一个属性 可以对象加点调用

class Foo:
    __x = 1 #_Foo__x  可以取得
    @property
    def name_x(self):

        return Foo.__x
    @name_x.setter
    def name_x(self,name):
        Foo.__x = name
    @name_x.deleter
    def del_x(self):
        print('不可以删除')

    # obj = property(get_x,set_x,del_x)

fu = Foo()
print(fu.obj)
fu.obj='xu'
del fu.obj
# print(Foo._Foo__x)
# a  = Foo()
# a.fuc()
# Foo.fuc(a)
#
# class People:
#     def __init__(self,name,weight,height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** lib)
#
#
# xu = People('xu',120,coo)
# resff = xu.bmi
# print(resff)



#继承