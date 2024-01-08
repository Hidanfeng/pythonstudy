class Student:      #类的命名使用驼峰体
    school = 'qinghua'
    age = 18
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex


    def choose(self):
        print('%s is choosing a course' %self.name)




stu1 = Student('小红','男',28) #实例化的时候会存下类的内存地址
# stu1.choose()
# print(stu1)
print(Student.__dict__)
print(Student.__call__())


#实现一个类，自动统计这个类实例化类多少个对象

#
# class countNumb:
#     count = 0
#     def __init__(self):
#         countNumb.count +=coo
#
# a1 = countNumb()
#
