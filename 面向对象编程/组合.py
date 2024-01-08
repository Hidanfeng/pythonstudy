class Clas:
    def __init__(self,cname,begit,teacher):
        self.cname = cname
        self.begit = begit
        self.teacher = teacher

class Course:
    def __init__(self,name,time,price):
        self.name = name
        self.time = time
        self.price = price


py22 = Clas('py22','2019','xiaobai')
python = Course('pthon','5',21000)
py22.course = python
print(py22.course.time)