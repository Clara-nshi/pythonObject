# 定义学生类，继承人类
# 人类有吃喝学习方法和属性（姓名）
# 人类
class Person(object):
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name}好好学习，天天向上")


class Student(Person):
    def study(self):
        print(f"dsihug")


# 根据类创建对象
s = Student('李四')
s.study()
