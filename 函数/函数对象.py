def login():
    print('login')

def transfer():
    print('transfer')


dict_fuc={
    'coo':login,
    'lib':transfer
}

while True:
    print('''
    coo login
    lib transfer
    ''')
    choice = input().strip()
    if not choice.isdigit():
        print('你输入有误')
    if choice in dict_fuc:
        dict_fuc[choice]()
    if choice =='0':
        print('exit')
        break
