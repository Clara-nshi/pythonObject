# # 1. 先定义类
# class Person(object):
#     # 属性
#     def __init__(self, name):
#         self.name = name
#         # 私有属性
#         self.__money = 100000000
#
#     # 对外提供公共方法用于修改和获取私有属性
#     def set_money(self, money):
#         if money >= 0:
#             self.__money += money
#         else:
#             print('对不起，money不能为负')
#
#     def get_money(self):
#         return f'您的余额为：{self.__money}元'
#
#
# # 2. 再根据类创建对象
# p1 = Person('clara')
# print(p1.name)
# p1.set_money(100)
# print(p1.get_money())


# 1. 先定义类
class Person(object):
    # 属性
    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__money = 10000000000

    # 对外提供公共方法用于修改和获取私有属性
    def set_money(self, money):
        if money >= 0:
            self.__money += money
            print(f'您已成功存入{money}元')
        else:
            print('存钱数需为非负数')

    def get_money(self):
        return f'您的余额为：{self.__money}元'


# 2. 再根据类创建对象
person = Person('clara')
person.set_money(100000000)
print(person.get_money())
