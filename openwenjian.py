# f = open('0016_1.txt','a+',encoding='utf-8')
# while True:
#     tx = f.readline()
#     print(tx.strip())
#     if not tx:
#         break
# print(f.read())
# tx = f.readlines()
# tx = f.readline()
# f.write('99')
# f.writelines(['ni','dfd'])


# f.close()

with open('0016_1.txt','rt',encoding='utf-8')as f:
    # print(type(f))
    # f.write('yy你好呀uu\n')
    print(f.readline())
    # print(type(f.readline()))
    print(f.readline())
    print(f.readline())
