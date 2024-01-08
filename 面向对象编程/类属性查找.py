class Student():
    count = 0

    def __init__(self,name,age):

        self.name = name
        self.age = age
        print(self.count)

    def print_nanme(obj):
        print(obj.name)

    def print_age(self):
        print(self.age)


st1 =Student('xudanfeng',18)
Student.print_nanme(st1)
st2 =Student('sun',18)