# Python面向对象
# 定义Student类
class Student:
    def getName(self):
        print("My Name is jianqiaanWu")
    age:int = 0

    def getAge(self):
        print("age: %s " %(self.age))

    def getTime(*format):
        print(type(format))
s = Student()
s.getName()
s.age = '10'
s.getAge()
s.getTime()