l = ['aLx','lXX','WWs']


res = map(lambda name:name+'_asb',l)
lista =[]
for i in res:
    lista.append(i)
print(lista)

from  functools import reduce

la = [1,3,5,6]
a = reduce(lambda x,y:x+y,la)
print(a)