#返回文件后缀名子
# def get_file_exname(file_name ):
#     pos  = file_name.rfind('.')
#     index = pos
#     return file_name[index:]

def get_suffix(file_name,has_dot=False):
    '''
    获取文件后缀名字
    :param file_name:
    :param has_dot: 返回的后缀文件名是否带点
    :return:
    '''
    pos = file_name.rfind('.')
    #rfind 没有获取到索引返回-1
    if 0 < pos < len(file_name)-1:
        index = pos if has_dot else pos+1
        return file_name[index:]
    else:
        return ''


# def max2(numlist):
#     '''
#     传入列表返回最大和第二大的数
#     :param numlist:
#     :return:
#     '''
#     num1 = 0
#     num2 = 0
#     for i in numlist:
#         num1 = i if i>num1