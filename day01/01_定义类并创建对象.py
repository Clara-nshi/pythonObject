# 需求：定义学生类， 学生类有学习方法
# 1. 先定义类(类名：建议首字母大写)
# class Student(object):
# 默认继承，可以省略（object）
class Student:
    pass


# 2. 再根据类创建对象
clara = Student()
mike = Student()

print(clara)   # 默认十六进制地址
print(mike)    # 默认十六进制地址

print(id(clara))    # id获取十进制地址



