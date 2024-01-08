l = ['aLx_dsb','lXX_dsb','WWs_dab']

l_up = [name.lower() for name in l ]
print(l_up)
l_dsb =[name.split('_')[0] for name in l]
print(l_dsb)





#字典生成式
dic = {key:None for  key in l}
print(dic)