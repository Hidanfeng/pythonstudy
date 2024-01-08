'''
文件复制
src_path = /Users/danfengxu/Desktop/pythonstudy/day202311/模块/backup
target_path
'''
import os
def copy(src,target):

    #1要看一下原文件路径下有哪些文件和文件夹
    wenj_list = os.listdir(src)
    for document in wenj_list:
        #2如果是文件夹就递归调用,如果是文件就写入目标文件夹
        if os.path.isfile(os.path.join(src,document)):
            with open(os.path.join(src,document),'rb') as f:
                cten = f.read()
                with open(os.path.join(target,document),'wb') as f2:
                    f2.write(cten)
        else:
            target_path = os.path.join(target,document)
            os.mkdir(target_path)
            return copy(os.path.join(src,document),target_path)



# copy('/Users/danfengxu/Desktop/pythonstudy/aa','/Users/danfengxu/Desktop/pythonstudy/bb')