"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成


知识点 封装 继承 多态 property
"""


from abc import ABCMeta,abstractmethod

class Employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salry(self):
        pass


class Manager(Employee):
    '''经理'''
    def get_salry(self):
        return 15000.0


class Programmer(Employee):
    '''程序员'''
    def __init__(self,name,work_hours=0):
        super().__init__(name)
        self._work_hours = work_hours

    @property
    def work_hours(self):
        return self._work_hours

    @work_hours.setter
    def work_hours(self,work_hours):
        self._work_hours = work_hours if work_hours>0 else 0


    def get_salry(self):
        return 150*self._work_hours


class Salesman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self,sales):
        self._sales  = sales if sales>0 else 0

    def get_salry(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for enp in emps:
        if isinstance(enp, Programmer):
            work_hours = int(input('请输入%s的工作时长：'%enp.name))
            enp.work_hours = work_hours
        elif isinstance(enp,Salesman):
            enp.sales = float(input('请输入%s本月销售额: ' % enp.name))
        print(f'{enp.name}本月的工资为：¥{enp.get_salry()}元')


if __name__ == '__main__':
    main()
