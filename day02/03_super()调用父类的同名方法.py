# 需求：定义动物类（有姓名属性、有吃、叫、睡方法）
# 定义：狗和猫类，继承动物类，重写叫方法
# 1. 先定义类
class Animals(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("动物在吃...")

    def sleep(self):
        print("动物在睡...")

    def call(self):
        print("动物在叫...")


# 重写继承父类的方法
class Cat(Animals):
    # TODO 如何找父类的同名方法呢（super）
    # TODO 方法1 推荐
    def __init__(self, name, color, age):
        Animals.__init__(self, name)
        self.color = color
        self.age = age
    # # TODO 方法2: 不推荐，限制多，但考试考
    # def __init__(self, name, color, age):
    #     super().__init__(name)
    #     self.color = color
    #     self.age = age

    def call(self):
        print(f"{self.age}岁的{self.color}的{self.name}在叫...")


# 重写继承父类的方法
class Dog(Animals):
    # TODO 如何找父类的同名方法呢（super）
    def __init__(self, name, color, age):
        # super().__init__(name)
        # super(Dog, self).__init__(name)
        # 相同，这种方法更方便通用
        Animals.__init__(self, name)
        self.color = color
        self.age = age

    def call(self):
        super().call()
        print(f"{self.age}岁的{self.color}的{self.name}在叫...")


# 2 再根据类创建对象
# TODO 子类优先在本类中找，如果找不到再去父类中找
animal = Animals("大象")
animal.eat()
animal.sleep()
animal.call()
cat = Cat("小猫", "orange", 12)
cat.eat()
cat.sleep()
cat.call()
dog = Dog("小狗", "white", 8)
dog.eat()
dog.sleep()
dog.call()
