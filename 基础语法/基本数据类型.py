
'''
********************字符串******************
'''
print('********************字符串******************')
str = 'yyyuuuiii'
print(str[0:3])
a=str.split(',')
print(a)
str33 = str.join(['ee','bb','rr'])
print(str33)
print(str.count('y'))
sr44 = str.find('aa')
print(sr44)
boo1 = str.startswith("10")
print(boo1)
boo2 = str.isdigit()
print(boo2)

'''
yyy
['yyyuuuiii']
eeyyyuuuiiibbyyyuuuiiirr
3
-1
False
False
'''

'''
********************列表*********************
'''
print('********************列表******************')

example_list = ['xu','sun','tao',['xu1','sun2']]

#增
example_list.append('yoyo')
example_list.insert(0,'dundun')
print(example_list)
example_list.extend(['oo','bb'])
print(example_list)
#删
example_list.pop(0)
example_list.remove('yoyo')
print(example_list)
# example_list.clear()
# print(example_list)
#改
example_list[0] = 'xusun'
print(example_list)
example_list_l = example_list[1:-1:2]
print(example_list_l)
'''
['dundun', 'xu', 'sun', 'tao', ['xu1', 'sun2'], 'yoyo']
['dundun', 'xu', 'sun', 'tao', ['xu1', 'sun2'], 'yoyo', 'oo', 'bb']
['xu', 'sun', 'tao', ['xu1', 'sun2'], 'oo', 'bb']
['xusun', 'sun', 'tao', ['xu1', 'sun2'], 'oo', 'bb']
['sun', ['xu1', 'sun2']]
'''

'''
********************元组*********************
'''
print('********************元组******************')

example_tuple = (88,'uu',88)
print(example_tuple)
#元组不可变，只能查询

'''
(88, 'uu', 88)
'''

'''
********************字典*********************
'''
print('********************字典******************')

example_dict = {'Name1': 'sun', 'Age1': 7, 'Name2': 'xu'}
print(example_dict)
# di = dict.fromkeys(str,example_list)
# print(di)
#增
example_dict['Age2'] = '19'
print(example_dict)
#删
example_dict.pop('Age2')
print(example_dict)
#查
print(example_dict.get('Name1'))
print(list(example_dict.keys()))
print(list(example_dict.values()))
'''
{'Name1': 'sun', 'Age1': 7, 'Name2': 'xu'}
{'Name1': 'sun', 'Age1': 7, 'Name2': 'xu', 'Age2': '19'}
{'Name1': 'sun', 'Age1': 7, 'Name2': 'xu'}
sun
['Name1', 'Age1', 'Name2']
['sun', 7, 'xu']
'''

'''
********************集合*********************
'''
print('********************集合******************')
example_set = {1,2,'xxx晗',3,3}
example_set.add(9)
example_set.pop()
print(type(example_set),example_set)

'''
<class 'set'> {2, 3, 9, 'xxx晗'}
'''

'''
*****************************************
'''
print('**************************************')
a = '1000000'
b = '1000000'
print(id(a),id(b))

print('**************直接引用间接引用**********************')
name = '张'
name_list = ['11',22,name]
name = '孙'
print(name_list)

list1 = ['y','z']
list2 = ['o','p']
list1.append(list2)
list2.append(list1)
print(list1,list2)



'''
********************python内存管理，垃圾回收********************
直接引用
间接引用
引用计数
标记清除

'''
print('*******************内存管理，垃圾回收******************')










# print(str[0:3])
# x = 10 # 直接引用
# print(id(x))
#
# l = ['a', 10]
# print(id(l[coo])) # 间接引用

# num =  int(input())
#
# for i in range(coo,num):
#     if i%lib==0:
#         print(i)

#让用户输入第一个数字
#
# userinput = int(input('请输入数字：'))
# max_num = userinput
# min_num = userinput
#
# for i in range(coo,3):
#     userinput = int(input('请输入数字：'))
#     if max_num<userinput:
#         max_num = userinput
#     if min_num >userinput:
#         min_num = userinput
# print(max_num,min_num)


# while True:
#     try:
#         l = input()
#         for i in range(0, len(l), 8):
#             print(f"{l[i:i+8]:<98}")
#     except:
#         break

# list_a =[lib,5,4,0]
# list_a.sort()
#
# str = 'seifenf'
# a = sorted(str)
#
#
# print(list_a,a)


for m in [lambda x:i*x for i in [0,1,2,]]:
    print(m(1))