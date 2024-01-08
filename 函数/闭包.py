def outer_func(x):
    loc_list = []
    def inner_func():
        loc_list.append(len(loc_list) + 1)
        print ('%s loc_list = %s' %(x, loc_list))
    return inner_func

#函数有被引用所以不会被释放
clo_func_0 = outer_func(7)
clo_func_0()
clo_func_0()
# clo_func_0('clo_func_0')
# clo_func_1 = outer_func()
# clo_func_1('clo_func_1')
# clo_func_0('clo_func_0')
# clo_func_1('clo_func_1')

