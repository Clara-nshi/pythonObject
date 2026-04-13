# 1. 先定义类
class Tool(object):
    # 定义类属性,存储工具创建的个数
    COUNT = 0

    # 成员方法: 魔法方法
    def __init__(self, name):
        self.name = name
        # 修改类属性
        Tool.COUNT += 1

    # 成员方法: 自定义方法
    def use_tool(self):
        print(f'使用了{self.name}工具')

    # TODO 静态方法, 注意使用@staticmethod装饰器,静态方法主要用于解释说明
    @staticmethod
    def explain():
        print('这是一个说明书')

    # TODO: 类方法,可以通过类名调用注意: 使用@classmethod装饰器
    @classmethod
    def get_count(cls):
        print(f'工具被使用了{cls.COUNT}次')


# 2. 再根据类创建对象
tool = Tool('扳手')
tool1 = Tool('改锥')
tool2 = Tool('棋子')
# 调用静态方法
tool.explain()
# 调用类方法
Tool.get_count()
# 成员方法只能对象调用
tool.use_tool()
tool1.use_tool()
tool2.use_tool()

