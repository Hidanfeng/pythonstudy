deic_a ={'a':'b','ni':'dfd'}
list_a = ['add','dfd','dfd']


import json

json_deic = json.dumps(deic_a)
json_list = json.dumps(list_a)

with open('1.txt','w+',encoding='utf-8')as f:
    # f.write(json_deic)
    # content = f.read()
    # content = json.loads(content)
    json.dump(list_a,f)

af = json.loads(b'["oo","opp","uhhj"]')
print(af)

# print(type(json.loads(json_list)))