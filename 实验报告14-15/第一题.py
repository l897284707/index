class Person(object):
    def __init__ (self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo (self):
        print('%s,性别：%s,年龄：%d'%(self.name,self.gender, \
                                self.age))
class Teacher(Person):
    def __init__ (self,name,age,gender,college,professional):
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional
    def personInfo (self):
        super().personInfo()
        print('是%s%s的老师'%(self.college,self.professional))
    def teachObj (self):
        return '今天讲了如何用面向对象设计程序'
class Student(Person):
    data_student=[]
    def data (self):
        Student.data_student.append('姓名:%s, 年龄:%d, 性别:%s, 学院:%s, 班级:%s'%(self.name,self.age,self.gender,self.college,self.banji))
    def __init__ (self,name,age,gender,college,banji):
        super().__init__(name,age,gender)
        self.college=college
        self.banji=banji
        Student.data(self)
    def personInfo (self):
        super().personInfo()
        print('是%s%s的学生'%(self.college,self.banji))
    def study (self):
        print('老师%s,我终于学会了！'%Teacher.teachObj(self))
    def __str__ (self):
        return '%s是%s%s的一位%d岁的%s同学'%(self.name,self.college, \
                                     self.banji,self.age,self.gender)
a=Student('田一杨',20,'男','家里蹲大学','三年二班')
a.personInfo()
a.study()
b=Student('刘聪聪',20,'女','家里蹲大学','三年二班')
b.personInfo()
a.study()
c=Student('曹建煌',20,'男','家里蹲大学','三年二班')
c.personInfo()
a.study()
d=Teacher('唐博文',30,'男','家里蹲大学','屋里系')
d.personInfo()
for i in Student.data_student:
    print(i)