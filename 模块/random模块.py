import random,time模块
# def get_code(size=4): # size为验证码长度
#     s = '9'
#     for i in range(size-1):
#         s += '9'
#         print(s)
#     s = f'%0{size}d' % random.randint(0, int(s))
#
#     return s
#
#
# code = get_code(6)
# print(code)
print('''
   ************************random常用方法****************
''')
list_choices = ['sun','xu','yoyo',('徐','孙')]
print('1: ',random.random())
print('2: ',random.uniform(1,10))
print('3: ',random.randint(1,10))
print('4: ',random.randrange(1,100))
print('5: ',random.choice(list_choices))
print('6: ',random.sample(list_choices,2))
'''
1:  0.3074350244096229
2:  3.4823533285618367
3:  8
4:  40
5:  ('徐', '孙')
6:  [('徐', '孙'), 'xu']
'''
print('''
  ***********************随机生成一个16位的密码，必须包含大、小写字母，数字和符号*************
''')


def pwd_generator(length = 16):
    if length<4:
        return ''
    while True:
        char_list = [[97,122],[65,90],[48,57],[33,47]]
        pwd = ''
        for _ in range(length):
            random_list = random.choice(char_list)
            random_char = chr(random.randint(*random_list))
            pwd += random_char
            l = [False for i in range(4)]
            for word in pwd:
                if 97 <= ord(word) <=122:
                    l[0] = True
                if 65 <= ord(word) <=90:
                    l[1] = True
                if 48<= ord(word) <=57:
                    l[2] = True
                if 33 <= ord(word) <= 47:
                    l[3] = True
            if l[0] and l[1] and l[2] and l[3]:
                    return pwd
            print(pwd,'密码不合法')

pwds = pwd_generator(6)
print(pwds)


