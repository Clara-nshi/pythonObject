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
    def call(self):
        print(f"{self.name}在叫...")

    # 重写继承父类的方法


class Dog(Animals):
    def call(self):
        print(f"{self.name}在叫...")


# 2 再根据类创建对象
# TODO 子类优先在本类中找，如果找不到再去父类中找
animal = Animals("大象")
animal.eat()
animal.sleep()
animal.call()
cat = Cat("小猫")
cat.eat()
cat.sleep()
cat.call()
dog = Dog("小狗")
dog.eat()
dog.sleep()
dog.call()
