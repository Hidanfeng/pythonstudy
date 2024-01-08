import os
import sys
#获取当前文件所属的文件夹
# path1 =os.path.dirname(__file__)
# print(path1)
#
# #获取当前文件的绝对路径
path2 = os.path.abspath(__file__)
print(path2)
#
# #python工作路径
path3 = os.getcwd()
print(path3)
#
# result = os.path.split(path2)
# print(result)
#
# wenjian = os.path.split(path2)
# print(wenjian)
# size = os.path.getsize('/模块/c1.txt')
# print(size)


# list_wen = os.listdir('./模块/os模块的')
# print(list_wen)
# os.makedirs('aa/bb')
# os.mknod('aa/bb/11.text')
# os.removedirs('/Users/danfengxu/Desktop/pythonstudy/bb')
# print(os.path.isfile(path1))


# print(sys.path)
# mast_path =os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# print(mast_path)
# sys.path.append(mast_path)
# print(sys.path)
from log.imgs import yy
