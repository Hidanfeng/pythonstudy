class MyType(type):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init')

    def __new__(cls, *args, **kwargs):
        cls_new = super().__new__(cls, *args, **kwargs)
        print('new')
        return cls_new

    def __call__(self, *args, **kwargs):
        print('call')


class Foo(object,metaclass=MyType):
    pass
#
#
obj = Foo()


#
#
# class Foo(object):
#     pass
#     def __init__(self):
#         print('init')
#
#     def __new__(cls, *args, **kwargs):
#         print('__new__')
#         super().__new__(cls,*args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#     #     # super().__call__(*args, **kwargs)
#
# class Goo(Foo):
#     pass








