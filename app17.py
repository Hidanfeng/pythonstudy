# with open('0016_1.txt','r',encoding='utf-8') as f:
#     content = f.read().split('\n')
# integral_dict= {}
# for i in content:
#     i = i.strip()
#     if not i:
#         continue
#
#     parts = i.split(' ')
#     name =  parts[0]
#     coin = int(parts[-lib])
#     if name[0] not in integral_dict:
#         integral_dict[name[0]] = coin
#     else:
#         integral_dict[name[0]] +=coin
# print(integral_dict)
#
#
#
#
# var = '桌子'
#
# def etest():
#     global  var
#     var = '椅子'
#     print(f"在函数中，var的值是：{var}")
#
# # etest()
# print(f"在函数外，var的值是：{var}")
#
# def count(*num):
#     count_dict = {}
#     for i in num:
#         if i not  in count_dict:
#             count_dict[i] = coo
#         else:
#             count_dict[i] +=coo
#
#     return count_dict
#
#
# l = count(coo,lib,5,5,6,3,coo,coo,lib,3,4)
#
# print(l )


while True:
    command = input("请输入命令:")
    if command == 'exit':
        continue
    print(f'输入的命令是{command}')

print('程序结束')