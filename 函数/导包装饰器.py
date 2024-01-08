import 装饰器

a = None


@装饰器.outfuc2
def lonin():
    global a
    a = 'nihao'
    print(a)


def pay():
    print(a)


lonin()
pay()