# 定义烧烤类(属性：name， time， state， seasonings)
# （方法：烧烤，加调料）
# 调用烧烤类，开始烤地瓜和羊肉串
class Grill(object):
    # 初始化属性
    def __init__(self, name):
        self.name = name
        self.time = 0
        self.state = '生的'
        self.seasonings = []  

    # 烧烤
    def roast(self, time):
        self.time = time
        if 0 <= self.time <= 3:
            self.state = '生的'
        elif 3 < self.time <= 7:
            self.state = '半生不熟'
        elif 7 < self.time <= 12:
            self.state = '熟了'
        elif self.time > 12:
            self.state = '糊了'

    # 加调料
    def add_seasonings(self, s):
        self.seasonings.append(s)

    # 魔法方法 __str__
    def __str__(self):
        return f"{self.name}烤了{self.time}分钟，加了{self.seasonings}调料，{self.state}"


# 调用烧烤类，开始羊肉串和韭菜
grill = Grill('羊肉串')
print(grill)
grill.roast(12)
grill.seasonings.append("辣椒面")
print(grill)
grill = Grill('韭菜')
print(grill)
grill.roast(15)
grill.seasonings.append("孜然")
print(grill)


