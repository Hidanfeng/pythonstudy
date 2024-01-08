'''
继承
'''

class people:
    x = 19
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self.name)

    def run(self):
        print('%s 正在跑' %self.name)


class Teacher(people):
    def __init__(self,name,age,higt):
        self.higt = higt
        super().__init__(name,age)


    def teaching(self):
        print('%s 正在教课'  %self.name)


xu = Teacher('xu',18,18)
print(xu.x)
xu.teaching()




class Z(object):
    def test(self):
        print('from Z')

class A():
    def test(self):
        print('from A')

class B():
    def test(self):
        print('from B')




class E(Z):
    def test1(self):
        print('from E')

class D(B):
    def test1(self):
        print('from D')

class C(A):
    def test(self):
        print('from C')

class F(C,D,E):
    pass

print(F.mro())
obj = F()
obj.test() # 结果为：from B
