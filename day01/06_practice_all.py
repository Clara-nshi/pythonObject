# 需求：买个小汽车，用户买小汽车的颜色
class Car(object):
    # TODO 魔法方法__init__()创建对象的时候自动调用
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.name}买了一辆{self.color}色的车'

    # 自动调用
    def __del__(self):
        print(f"{self.name}已经删除...")


# 再根据类创建对象
car = Car('clara', 'pink')
car1 = Car('mike', 'black')
print(car)
print(car1)


