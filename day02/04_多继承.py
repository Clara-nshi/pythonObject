# 1. 先定义类
class Father(object):
    def __init__(self, name):
        print('Father中的魔法方法')
        self.name = name


class Mother(object):
    def __init__(self, name):
        print('Mother中的魔法方法')
        self.name = name


class Child(Father, Mother):
    def __init__(self, name):
        Mother.__init__(self, name)
        Father.__init__(self, name)
        # TODO super()只能调用第一个父类的同名方法
        # super().__init__(name)
        print('Child中的魔法方法')


# 2. 再根据类创建对象
# TODO 优先从自己里找， 然后 Father, Mother
c = Child('zhangsan')

print(Child.mro())
print(Child.__mro__)

