def createzhangSan():
    print('\n ***  1执行创建张三账号的代码 ***')
    zhangSan = {
        'username'   : 'zhangsan',
        'password'   : '111111',
        'invitecode' : 'abcdefg' # 这是系统创建用户产生的其它信息
    }
    while True:
        x = yield 22
        print('\n ***  2执行清除张三账号的代码 ***')
# from collections.abc import Iterable

a =createzhangSan()
res_a = next(a)
print('res: %s' %res_a)
# next(a)
res_b = a.send('kk')
print(res_b)
