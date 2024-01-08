#1时间格式的转换
#struct_time->时间戳
import time
#
# struct_time = time.localtime()
# print(struct_time)
# print('struct_time:',time.mktime(struct_time))
#
#
# tp_time = time.time()
# print('tp_time:',time.localtime(tp_time))
#
# sf_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
# print('sf_time:',sf_time)
#
# sruct_time=time.strptime('2023-12-07 11:46:38','%Y-%m-%d %H:%M:%S')
# stamp_time = time.mktime(sruct_time)
# end_stamp_time = stamp_time+7*86400
# st_time = time.localtime(end_stamp_time)
# format_time = time.strftime('%Y-%m-%d %H:%M:%S',st_time)
# print(format_time)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time.asctime())))



'''
将如上的时间2016-05-05 20:28:54转换成时间戳
'''
str_time = '2016-05-05 20:28:54'
#先转成结构化的时间
struc_time1 = time.strptime(str_time,'%Y-%m-%d %H:%M:%S')
print(struc_time1)
#再转成时间戳
chuo_time = time.mktime(struc_time1)
print(chuo_time)
print('''

*************************************************************

''')
'''
将时间戳转换成时间
'''
now_time = time.time()
print(now_time)
#将时间戳转换成结构化的时间
stuct_time2 = time.localtime(now_time)
print(stuct_time2)
#将结构化的时间转成时间
str_time2 = time.strftime('%Y-%m-%d %H:%M:%S',stuct_time2)
print(str_time2)