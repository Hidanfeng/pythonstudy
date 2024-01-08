class ftp(object):
    def put(self):
        print('正在上传数据。。')

    def get(self):
        print('正在下载数据。。')

    def interact(self):
        opt = input('>>>')
        # if hasattr(self,opt):
        getattr(self,opt,self.print_eror)()

    def print_eror(self):
        print('你输入的有误')



class f(ftp):
    pass

f = ftp()
# f.interact()
print(type(f))
# t=Teacher('Egon Lin')
# print(Teacher.__dict__)
# hasattr(object,'name')
#print(hasattr(t,'full_name'))# 按字符串'full_name'判断有无属性t.full_name

# getattr(object, 'name', default=None)
#print(getattr(t,'full_name',None))# 等同于t.full_name,不存在该属性则返回默认值None

# setattr(x, 'y', v)
#setattr(t,'age',18) # 等同于t.age=18

# delattr(x, 'y')
#delattr(t,'age') # 等同于del t.age