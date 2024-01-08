import time
import datetime
#time
#1时间戳
print(time.time())
#2按某种格式显示时间，字符串格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#3结构化的时间
res =time.localtime()
print(res)
#4 时间标准时间
print(time.gmtime())
#datetime
print(datetime.datetime.now()+datetime.timedelta(days=1))

