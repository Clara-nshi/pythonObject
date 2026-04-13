# 1. 先定义类属性和成员属性
class Tool(object):
    count = 0

    # 定义类属性
    def __init__(self, name):
        # 定义成员属性
        self.name = name
        # 修改类属性： 类名.属性名 = 值
        Tool.count += 1


# 2. 访问类属性
print(Tool.count)
# 修改类属性: 类名.类属性名 = 值
# Tool.count = 1
# 访问类属性: 类名.类属性名
# print(Tool.count)
# 访问成员属性: 类名.类属性名
t = Tool('扳手')
print(t.name, t.count)
print(f'当前工具具有{Tool.count}个')
t1 = Tool('剪刀')
print(t1.name, t1.count)
print(f'当前工具具有{Tool.count}个')

