# coo、定义
lambda x,y,z:x+y+z

#等同于
def func(x,y,z):
    return x+y+z

#调用
#方式一：
res = (lambda x,y,z:x+y+z)(1,2,3)

# 方式二：
func=lambda x,y,z:x+y+z # “匿名”的本质就是要没有名字，所以此处为匿名函数指定名字是没有意义的
res=func(1,2,3)

# 函数max会迭代字典salaries，每取出一个“人名”就会当做参数传给指定的匿名函数，然后将匿名函数的返回值当做比较依据，最终返回薪资最高的那个人的名字
salaries={
    'siry':3000,
    'tom':7000,
    'lili':10000,
    'jack':2000
}
max_sl=max(salaries,key=lambda k:salaries[k])
salaries_key = salaries.keys()
# print(max_sl,type(salaries_key))


res = map(lambda x:x+100,salaries.values())
print(list(res))

def mul(x):
    return x*x

n=[1,2,3,4,5]
res1=map(mul,n)
print(res1)