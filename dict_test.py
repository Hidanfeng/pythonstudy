members = {
    1 :{'name':'白月黑羽', 'level':3, 'coins':300},
    2 :{'name':'短笛魔王', 'level':5, 'coins':330},
    3 :{'name':'紫气一元', 'level':6, 'coins':340},
    4 :{'name':'拜月主',   'level':3, 'coins':32200},
    5 :{'name':'诸法空',   'level':4, 'coins':330},
    6 :{'name':'暗光城主', 'level':3, 'coins':320},
    7 :{'name':'心魔尊',   'level':3, 'coins':2300},
    8 :{'name':'日月童子', 'level':8, 'coins':3450},
    9 :{'name':'不死尸王', 'level':3, 'coins':324},
    10:{'name':'天池剑尊', 'level':9, 'coins':13100},
}
print(members.fromkeys())

#
# members_name= {}
# for k,v in members.items():
#     name = v['name']
#     v['id'] = k
#     members_name[name]=v
#
# #展示该用户的信息
# def show_infomation():
#     name = input('请输入你要查的用户名')
#     if name not in members_name:
#         print('你输入的名字有误')
#     else:
#         id = members_name[name]['id']
#         level = members_name[name]['level']
#         print(f'该用户的ID：{id},该用户的等级：{level}')
#
# menus = '''
# 请选择操作选项：
#    coo 查看用户账号信息
#    lib 添加用户
#    3 删除用户
#    4 列出所有用户信息
#    0 退出
# '''
# # 显示主菜单
# # while True:
# #     choice = input(menus)
# #     if choice=='coo':
# #         show_infomation()
#
# v =dict.fromkeys(['k1','k2'],[])
# v['k1'].append(99)
#
# if __name__ == '__main__':
#
#     print(v)
#     v['k1']=77
#     print(v)