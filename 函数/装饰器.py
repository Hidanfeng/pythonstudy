# import time
x =1
# def text(text):
#     def outfuc(fuc):
#         def inerfuc(*args,**kwargs):
#             print('%s %s()' % (text,fuc.__name__))
#             return fuc(*args,**kwargs)
#         return inerfuc
#     return outfuc

def outfuc2(fuc):
    print('lib',globals())
    print('lib',locals())
    def inerfuc2(*args,**kwargs):
        print('4',globals())
        print('4',locals())
        # start_time = time.time()
        # print(' %s()' % (fuc.__name__))
        res = fuc(*args, **kwargs)
        # exit_time = time.time() - start_time
        # print(exit_time)
        return res
    return inerfuc2
print(outfuc2.__dir__)
print('coo',locals())
print('---------coo-----------')


@outfuc2   # fuc111 = outfuc2(fuc111)
def fuc111():
    print('jjjj')


print('3',globals())
print('3',locals())
print('xxxxxxxxxxxxxxxxxxx')

if __name__ == '__main__':
    print('******************')

    fuc111()
#     print(globals())
#     print(locals())


