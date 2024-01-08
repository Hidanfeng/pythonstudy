class Foo(object):
    def fuc1(self):
        print('fuc1')

    def fuc2(self):
        print('fuc2')

obj = Foo()
fuc = getattr(obj,'fuc1')
fuc()

