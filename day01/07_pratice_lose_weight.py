# 减肥：小明同学当前体重是100kg， 每当他跑步一次时，则会减少0.5kg
# 每当他大吃大喝一次，则会增加2kg，请试着采用面向对象方式完成案例
# # TODO 非面向对象
#
# def run():
#     global weight
#     weight -= 0.5
#     print(f'跑步一次减0.5kg，还剩{weight}kg')
#
#
# def eat():
#     global weight
#     weight += 2
#     print(f'大吃大喝一次增重2kg，还剩{weight}kg')
#
#
# weight = 100
# print(f"初始体重为{weight}")
# run()
# run()


# 减肥：小明同学当前体重是100kg， 每当他跑步一次时，则会减少0.5kg
# 每当他大吃大喝一次，则会增加2kg，请试着采用面向对象方式完成案例
# TODO 面向对象
# 2. 采用面向对象的方法
# class Lose_weight(object):
#     # 特征/属性
#     # 行为/方法
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def run(self):
#         self.weight -= 0.5
#         print(f'{self.name}跑步一次减0.5kg，还剩{self.weight}kg')
#
#     def eat(self):
#         self.weight += 2
#         print(f'{self.weight}大吃大喝一次增重2kg，还剩{self.weight}kg')
#
#
# clara = lose_weight = Lose_weight('clara', 60)
# clara.run()
# clara.run()
# clara.run()
# clara.run()
# clara.eat()
# mike = lose_weight1 = Lose_weight('mike', 100)


# 减肥：小明同学当前体重是100kg， 每当他跑步一次时，则会减少0.5kg
# 每当他大吃大喝一次，则会增加2kg，请试着采用面向对象方式完成案例
# TODO 面向对象
# 2. 采用面向对象的方法


#
# 减肥：小明同学当前体重是100kg， 每当他跑步一次时，则会减少0.5kg
# 每当他大吃大喝一次，则会增加2kg，请试着采用面向对象方式完成案例
# TODO 面向对象
# 2. 采用面向对象的方法
class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 减肥：小明同学当前体重是100kg， 每当他跑步一次时，则会减少0.5kg
    def run(self):
        self.weight -= 0.5
        print(f"{self.name}跑步一次，减0.5kg，目前{self.weight}kg")

    # 每当他大吃大喝一次，则会增加2kg，请试着采用面向对象方式完成案例
    # 减肥：小明同学当前体重是100kg， 每当他跑步一次时，则会减少0.5kg
    def eat(self):
        self.weight += 2
        print(f"{self.name}跑步一次，减2kg，目前{self.weight}kg")


# TODO 面向对象
# 2. 采用面向对象的方法
person = Person('mike', 100)
person.run()
person.run()
person.run()
person.eat()