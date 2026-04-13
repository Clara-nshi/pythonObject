# 需求：买个小汽车，用户买小汽车的颜色
class Animal(object):
    # TODO 魔法方法__init__()创建对象的时候自动调用
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def name_color(self):
        print(f'{self.name}的颜色是{self.color}')

    # __str__魔法方法：打印对象的时候，自动调用，并打印它返回的字符串
    # def get_content(self):
    #     return f"姓名：{self.name}, 颜色：{self.color}"
    # 非必须，自己写方法也可以调用出来
    def __str__(self):
        return f"姓名：{self.name}, 颜色：{self.color}"


# 再根据类创建对象
animal = Animal('panda', 'white and black')
animal1 = Animal('fox', 'orange')
animal.name_color()
animal1.name_color()

# animal.get_content()

# 默认打印对象打印的是地址，如果重写了__str__()打印的就是他返回的字符串
print(animal)
print(animal1)
# 自己写的自己调用
# print(animal.get_content())
