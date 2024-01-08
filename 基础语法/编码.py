dict_a = {
    'file_name':'你好.py'
}


str_a = 'xxxiii'
import json
di = json.dumps(dict_a)

print(di.encode('utf-8'))
print(bytes(str(di),'utf-8').zfill(8))

print(type(str_a.encode('utf-8')))


header = {
                'file_name': 'hhhh',
                'file_size': 'sssss',
                'md5': 'hhhh'
            }
header_json = json.dumps(header)
#头部信息
header_bytes = header_json.encode('utf-8')
            #头部长度
header_h = bytes(str(len(header_bytes)),'utf-8').zfill(4)
print(header_h)

import subprocess
cmd = input()
file_list = cmd.split('/')
print(file_list)
cmd = file_list[0]
# file_path  = file_list[1]


res = subprocess.Popen(cmd,shell=True,
                       stderr=subprocess.PIPE,
                       stdout=subprocess.PIPE)
stderr = res.stderr.read()
stdout = res.stdout.read()

print(stdout+stderr)