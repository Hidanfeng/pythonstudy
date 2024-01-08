def deco1(fuc1):
    def wraper1(*args,**kwargs):
        print('wraper1')
        res = fuc1(*args,**kwargs)
        return res
    return wraper1

def deco2(fuc2):
    def wraper2(*args,**kwargs):
        print('wraper2')
        res = fuc2(*args,**kwargs)
        return res
    return wraper2

def deco3(x):
    def outter(fuc3):
        def wraper3(*args,**kwargs):
            print('wraper3')
            res = fuc3(*args,**kwargs)
            return res
        return wraper3
    return outter



@deco1      # index = deco1(index) ==> index = deco2(wraper2) fuc1 =wraper2的内存地址 ==> index = wraper1
@deco2      # index = deco2(index) ==> index = deco2(wraper3) fuc2 =wraper3的内存地址 ==> index = wraper2
@deco3(11)  # @outter              ==> index = outter(index)  fuc3 =index的内存地址   ==> index = wraper3
def index(x):
    print('index')
    return x

a = index(8)   # wraper1(8) ==>wraper2(8) ==> wraper3(8)==> index(8)
print(a)