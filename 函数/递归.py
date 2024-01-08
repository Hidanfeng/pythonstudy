l =[1,2,4 ,[5,6,[7,8,[9,10,[11,12,13]]]]]

def printlist(list_l):
    for i in list_l:
        if type(i) is list:
            printlist(i)
        else:
            print(i)

printlist(l)

s = 'abcd'
print(list(s))