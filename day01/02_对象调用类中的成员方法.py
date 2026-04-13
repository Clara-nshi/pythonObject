# 需求：定义学生类（要有学习的方法），创建2个学生对象并调用学生方法
# 定义类
class Student:
    def study_method(self):
        print("听课，记笔记")
        print(self)


# 再根据类创建对象
clara = Student()
clara.study_method()
print(clara)


"""
结果：
好好学习，天天向上
<__main__.Student object at 0x0000027B59BD4C10>
<__main__.Student object at 0x0000027B59BD4C10>
这里的self就是调用方法的clara
"""